#미숫가루 영상에 합성하기
#original image path와 seg_masked path, 최종 저장 위치만 변경해주면 됨.

def misu_syn():
    frame_path = 'E:\\yejee\\hackathon\\cartshow\\frame2' #original image path
    img_list = os.listdir(frame_path)
    datalen = len(img_list)
    os.makedirs('E:\\yejee\\hackathon\\1217_5\\syn', exist_ok=True)

    for i in tqdm(range(1,datalen+1)):
        image = cv2.imread(os.path.join(frame_path,'%03d.jpg' % i))
        fake_B = cv2.imread("E:\\yejee\\hackathon\\1217_5\\seq_masked\\%04d.png" % i) #seg_masked path
        #fake_B = cv2.resize(fake_B,(512,512),interpolation=cv2.INTER_AREA)
        if i <= 85: #frame 1 to frame 85
            #fake_B = cv2.add(fake_B, (0, 5, 5, 0)) #color control
            image[430-256:430+256,665-256:665+256,:] = np.zeros((512,512,3)) 
            image[430-256:430+256,665-256:665+256,:] = fake_B
        elif i <= 128: #frame 86 to frame 128
            #fake_B = cv2.add(fake_B, (12, 12, 15, 0))
            image[450 - 256:450 + 256, 400 - 256:400 + 256, :] = np.zeros((512, 512, 3))
            image[450 - 256:450 + 256, 400 - 256:400 + 256, :] = fake_B
        elif i <= 184: #frame 129 to frame 184
            #fake_B = cv2.add(fake_B, (22, 15, 15, 0))
            image[380 - 256:380 + 256, 520 - 256:520 + 256, :] = np.zeros((512, 512, 3))
            image[380 - 256:380 + 256, 520 - 256:520 + 256, :] = fake_B
        elif i <= 224: #frame 185 to frame 224
            #fake_B = cv2.add(fake_B, (22, 15, 15, 0))
            image[380 - 256:380 + 256, 480 - 256:480 + 256, :] = np.zeros((512, 512, 3))
            image[380 - 256:380 + 256, 480 - 256:480 + 256, :] = fake_B
        elif i <= 375: #frame 224 to frame 375
            #fake_B = cv2.add(fake_B, (22, 15, 15, 0))
            image[330 - 256:330 + 256, 290 - 256:290 + 256, :] = np.zeros((512, 512, 3))
            image[330 - 256:330 + 256, 290 - 256:290 + 256, :] = fake_B
        else:
            #fake_B = cv2.add(fake_B, (11, 11, 10, 0))
            image[350 - 256:350 + 256, 450 - 256:450 + 256, :] = np.zeros((512, 512, 3))
            image[350 - 256:350 + 256, 450 - 256:450 + 256, :] = fake_B

        cv2.imwrite("E:\\yejee\\hackathon\\1217_5\\syn\\new%04d.jpg" % i, image)
       

#물병 영상에 합성하기
def icis_syn():
    frame_path = 'E:/yejee/hackathon/cartshow/frame11' #original image path
    img_list = os.listdir(frame_path)
    datalen = len(img_list)
    os.makedirs('E:\\yejee\\hackathon\\1228\\syn', exist_ok=True)

    for i in tqdm(range(1,datalen+1)):
        image = cv2.imread(os.path.join(frame_path,'%03d.jpg'%i))
        fake_B = cv2.imread("E:\\yejee\\hackathon\\1228\\seq\\%04d.png" % i)
        #fake_B = cv2.resize(fake_B,dsize=(256,256),interpolation=cv2.INTER_AREA) #resize 필요한 경우

        if i <= 76:
            image[518-128:518+128,900-128:900+128,:] = np.zeros((256,256,3))
            #fake_B = cv2.add(fake_B, (15, 15, 18, 0))
            image[518-128:518+128,900-128:900+128,:] = fake_B
        elif i <= 140 :
            #fake_B = cv2.add(fake_B, (15, 10, 10, 0))
            image[580 - 128:580 + 128, 880 - 128:880 + 128, :] = 0
            image[580 - 128:580 + 128, 880 - 128:880 + 128, :] = fake_B
        elif i <= 175 :
            #fake_B = cv2.add(fake_B, (0, 5, 10, 0))
            image[580 - 128:580 + 128, 880 - 128:880 + 128, :] = 0
            image[580 - 128:580 + 128, 880 - 128:880 + 128, :] = fake_B
        elif i <= 218 :
            #fake_B = cv2.add(fake_B, (18, 17, 18, 0))
            image[420 - 128:420 + 128, 215 - 128:215 + 128, :] = 0
            image[420 - 128:420 + 128, 215 - 128:215 + 128, :] = fake_B
        cv2.imwrite("E:\\yejee\\hackathon\\1228\\syn\\frame%04d.jpg" % i, image)
        
