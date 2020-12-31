from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
import argparse

import cv2
import torch
import numpy as np
from glob import glob

from pysot.core.config import cfg
from pysot.models.model_builder import ModelBuilder
from pysot.tracker.tracker_builder import build_tracker
import pandas as pd
torch.set_num_threads(1)

parser = argparse.ArgumentParser(description='tracking demo')
parser.add_argument('--config', type=str, help='config file')
parser.add_argument('--snapshot', type=str, help='model name')
parser.add_argument('--video_name', default='', type=str,
                    help='videos or image files')
args = parser.parse_args()


def get_frames(video_name):
    if not video_name:
        cap = cv2.VideoCapture(0)
        # warmup
        for i in range(5):
            cap.read()
        while True:
            ret, frame = cap.read()
            if ret:
                yield frame
            else:
                break
    elif video_name.endswith('avi') or \
        video_name.endswith('mp4'):
        cap = cv2.VideoCapture(args.video_name)
        while True:
            ret, frame = cap.read()
            if ret:
                yield frame
            else:
                break
    else:
        images = glob(os.path.join(video_name, '*.jp*'))
        images = sorted(images,
                        key=lambda x: int(x.split('/')[-1].split('.')[0]))
        for img in images:
            frame = cv2.imread(img)
            yield frame


def main():
    # load config
    cfg.merge_from_file(args.config)
    cfg.CUDA = torch.cuda.is_available() and cfg.CUDA
    device = torch.device('cuda' if cfg.CUDA else 'cpu')

    # create model
    model = ModelBuilder()

    # load model
    model.load_state_dict(torch.load(args.snapshot,
        map_location=lambda storage, loc: storage.cpu()))
    model.eval().to(device)

    # build tracker
    tracker = build_tracker(model)

    first_frame = True
    if args.video_name:
        video_name = args.video_name.split('/')[-1].split('.')[0]
    else:
        video_name = 'webcam'

    cv2.namedWindow(video_name, cv2.WND_PROP_FULLSCREEN)

    save = 'C:\\Users\\biosi\\pysot\\demo'
    video_names = 'vita2'

    os.makedirs('%s/%s' % (save,video_names),exist_ok=True)
    os.makedirs('%s/%s/video' % (save,video_names), exist_ok=True)
    os.makedirs('%s/%s/mask' % (save,video_names), exist_ok=True)
    os.makedirs('%s/%s/crop' % (save,video_names),exist_ok=True)

    filename = 'vita2_output.mp4'

    #image2video write
    out = cv2.VideoWriter(os.path.join('%s\\%s\\video\\%s' % (save,video_names,filename)),cv2.VideoWriter_fourcc(*'mp4v'), 29.97, (int(list(get_frames(args.video_name))[0].shape[1]), int(list(get_frames(args.video_name))[0].shape[0])))

    x1 = []
    x2 = []
    x3 = []
    x4 = []
    y1 = []
    y2 = []
    y3 = []
    y4 = []


    for idx,frame in enumerate(get_frames(args.video_name)):
        if first_frame:
            try:
                init_rect = cv2.selectROI(video_names, frame, False, False)
            except:
                exit()
            tracker.init(frame, init_rect)
            first_frame = False
        else:
            outputs = tracker.track(frame)
            if 'polygon' in outputs:
                polygon = np.array(outputs['polygon']).astype(np.int32)
                polygon = polygon.reshape((-1, 1, 2))
                cv2.polylines(frame, [polygon],
                              True, (0, 255, 0), 3)
                mask = ((outputs['mask'] > cfg.TRACK.MASK_THERSHOLD) * 255)
                mask = mask.astype(np.uint8)
                mask = np.stack([mask, mask*255, mask]).transpose(1, 2, 0)
                cv2.imwrite("%s\\%s\\mask\\%04d.png"%(save, video_names, int(idx+1)),mask)
                #frame = cv2.addWeighted(frame, 0.77, mask, 0.23, -1)
                x = []
                y = []
                for i in range(4):
                    y.append(polygon[i, 0, 1])
                    x.append(polygon[i, 0, 0])

                x1.append(x[0])
                x2.append(x[1])
                x3.append(x[2])
                x4.append(x[3])

                y1.append(y[0])
                y2.append(y[1])
                y3.append(y[2])
                y4.append(y[3])

                x_max = x[0]
                x_min = x[0]
                y_max = x[0]
                y_min = x[0]
                if x[0] < 0:
                    x_max = 0
                    x_min = 0
                if y[0] < 0:
                    y_max = 0
                    y_min = 0

                for i in range(4):
                    x_max = max(x_max, x[i])
                    x_min = min(x_min, x[i])
                    y_max = max(y_max, y[i])
                    y_min = min(y_min, y[i])
                    if x_min < 0:
                        x_min = 0
                    if y_min < 0:
                        y_min = 0

                #x1.append(bbox[0])
                #y1.append(bbox[1])
                #x2.append(bbox[0] + bbox[2])
                #y2.append(bbox[1] + bbox[3])

                #crop frame
                #crop = frame[bbox[1]:bbox[1]+bbox[3],bbox[0]:bbox[0]+bbox[2],:]
                crop = mask[int(y_min):int(y_max),int(x_min):int(x_max),:]
                print(y_min,y_max,x_min,x_max)
                cv2.imwrite("%s\\%s\\crop\\%04d.png" % (save, video_names, int(idx + +1)), crop)

                frame = cv2.addWeighted(frame, 0.77, mask, 0.23, -1)
            else:
                bbox = list(map(int, outputs['bbox']))

                cv2.rectangle(frame, (bbox[0], bbox[1]),
                              (bbox[0]+bbox[2], bbox[1]+bbox[3]),
                              (0, 255, 0), 3)


            dataframe = pd.DataFrame({'y1':y1,'x1':x1,'y2':y2, 'x2':x2,'y3':y3,'x3':x3,'y4':y4, 'x4':x4})
            dataframe.to_csv(os.path.join('%s\\%s\\crop\\%s' % (save, video_names, "vita2_output.csv")),index=False)

            out.write(frame)
            cv2.imshow(video_names, frame)
            cv2.waitKey(40)


if __name__ == '__main__':
    main()
