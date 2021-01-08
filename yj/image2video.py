import os
import cv2
from tqdm import tqdm

def image2video():
    v2 = 'E:\\yejee\\hackathon\\1229\\syn'
    save = 'E:\\yejee\\hackathon\\1229'
    os.makedirs('%s/video'%save,exist_ok=True)

    filename = 'vita1.mp4'

    video_folder_name = v2
    img_list = os.listdir(video_folder_name)
    print(img_list)
    datalen = len(os.listdir(video_folder_name))
    cap = cv2.imread(os.path.join(video_folder_name, img_list[0]))

    out = cv2.VideoWriter(os.path.join('%s\\video\\%s'%(save,filename)),
                          cv2.VideoWriter_fourcc(*'EIVX'), 15, (int(cap.shape[1]), int(cap.shape[0])))
    for i in tqdm(range(datalen)):
        image_dir = os.path.join(video_folder_name, img_list[i])
        frame = cv2.imread(image_dir)

        out.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    out.release()
