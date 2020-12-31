# SiamMask / pysot
 

우리 비디오 영상에서 원하는 사물을 지정하면 그것을 기준으로 video tracking을 통해 segmentation 및 localization한다. 



   
## Getting Started / Step-by-step
**[환경설정하기]**

https://github.com/STVIR/pysot.git 를 참고했습니다.
```
conda create --name pysot python=3.7
conda activate pysot
```
```
git clone https://github.com/STVIR/pysot.git

conda install numpy
conda install pytorch=0.4.1 torchvision cuda90 -c pytorch
pip install opencv-python
pip install pyyaml yacs tqdm colorama matplotlib cython tensorboardX
python setup.py build_ext --inplace
```




   
### Pretrained model download
https://github.com/STVIR/pysot/blob/master/MODEL_ZOO.md
<img src="https://user-images.githubusercontent.com/75197237/100544850-f6fc9480-329b-11eb-921c-7a394b38663e.PNG"></img>
+ siammask_r50_l3을 다운받는다.

+ model.pth를 pysot/experiments/siammask_r50_l3 경로에 넣어준다.                                                                                                           


   
## Running the demo
```
python tools/demo.py \
    --config experiments/siammask_r50_l3/config.yaml \
    --snapshot experiments/siammask_r50_l3/model.pth
    --video demo/우리 영상.mp4 
```



   
### segmentation과 localization값을 추출하고 싶다면?

변경된 demo.py로 돌린다.(chameleon/yj/demo.py)
