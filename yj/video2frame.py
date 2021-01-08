import os
import cv2

def video2frame():
    videofile_path = "E:\\yejee\\hackathon\\1229"
    video = "vita.mp4"
    path = os.path.join(videofile_path,video)
    vidcap = cv2.VideoCapture(path)
    vidcap.set(cv2.CAP_PROP_FPS,29.97)

    output_path = "E:\\yejee\\hackathon\\1229\\frame"
    success, image = vidcap.read()
    count = 1
    while success:
        cv2.imwrite(os.path.join(output_path,'frame%03d.jpg' % count),image)
        success, image = vidcap.read()
        print('Read a new frame: ', success)
        count += 1
