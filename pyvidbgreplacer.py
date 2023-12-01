import numpy as np
import mediapipe as mp
import cv2

def replace_video_bg_with_image_ishow(bg_img_path,video_path=''):

    segmentation = mp.solutions.selfie_segmentation.SelfieSegmentation(model_selection=1)
    print(segmentation)

    background = cv2.imread(bg_img_path)
    if video_path != '':
        cap = cv2.VideoCapture(video_path)
    else:
        cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, frame = cap.read()
        height, width, channel = frame.shape
        RGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        
        results = segmentation.process(RGB)
        mask = results.segmentation_mask
        
        rsm  = np.stack((mask,)*3,axis= -1)
        condition = rsm > 0.6
        condition = np.reshape(condition,(height,width,3))
        
        background = cv2.resize(background,(width,height))
        
        output = np.where(condition,frame,background)
        
        cv2.imshow("output",output)
        
        k = cv2.waitKey(30) & 0xFF
        if k == (27):
            break
        
        
    cap.release()
    
def replace_video_bg_with_image_save_output(bg_img_path,video_path,output_path):

    segmentation = mp.solutions.selfie_segmentation.SelfieSegmentation(model_selection=1)
    print(segmentation)

    background = cv2.imread(bg_img_path)
    if video_path != '':
        cap = cv2.VideoCapture(video_path)
    else:
        cap = cv2.VideoCapture(0)
        
    # Get video properties
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Create VideoWriter object to save output
    
    '''
    Codecs: mp4=H264 , avi=XVID
    '''
    fourcc = cv2.VideoWriter_fourcc(*'H264')  # Change codec as needed 
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    while cap.isOpened():
        ret, frame = cap.read()
        if ret is None or frame is None:
            break
        height, width, channel = frame.shape
        RGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        
        results = segmentation.process(RGB)
        mask = results.segmentation_mask
        
        rsm  = np.stack((mask,)*3,axis= -1)
        condition = rsm > 0.6
        condition = np.reshape(condition,(height,width,3))
        
        background = cv2.resize(background,(width,height))
        
        output = np.where(condition,frame,background)
        # Save frame to output video
        out.write(output)
        
        
    cap.release()
    
    return output_path
    
    
    
    
