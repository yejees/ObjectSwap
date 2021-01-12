import os
from tqdm import tqdm

#video -> frame
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

#frame -> video
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
