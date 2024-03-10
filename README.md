# -TRINIT_KUCH-BHI_ML

# -VIDEO LINK
https://drive.google.com/file/d/1-2bcAlp6BbVEVZvPYr4zVmCSruxMz6hd/view?usp=sharing

# GRAPHS 
![Screenshot_20240310_070002](https://github.com/pratap-nitjsr/-TRINIT_KUCH-BHI_ML/assets/127110382/5c7a35dc-78b0-4e28-8416-bf02c4a28bf8)

# PRECISION
![Screenshot_20240310_065645](https://github.com/pratap-nitjsr/-TRINIT_KUCH-BHI_ML/assets/127110382/5c49aa45-d3fb-44c1-9ced-88aa0e3be445)

# RECALL
![Screenshot_20240310_065732](https://github.com/pratap-nitjsr/-TRINIT_KUCH-BHI_ML/assets/127110382/6144cddc-a090-4062-b236-16112ac182b8)

# How to run and check on local system
- Install all requirements listed in requirements.txt
- import all the requirements
- load the model 'best (4).pt' in python file using - ```python
    model = YOLO(best (4).pt)```
- to predict run from existing files (imgage or video files) - ```python
    model.predict(source='path to file', show=True)```
- to detect using live camera :
  ```python
  cap = cv2.VideoCapture(0)
  while(True):
    _, frame = cap.read()
    model.predict(source=frame, show=True)
    cv2.waitKey(1)```
- For more information kindly refer to documentation : https://docs.ultralytics.com/
