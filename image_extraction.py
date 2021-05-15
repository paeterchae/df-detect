import cv2 
import os 

DATASET_PATHS = {
    'original': 'original_sequences/youtube/raw/',
    'Deepfakes': 'manipulated_sequences/Deepfakes/raw/',
    'Face2Face': 'manipulated_sequences/Face2Face/raw/',
    'FaceSwap': 'manipulated_sequences/FaceSwap/raw/'
}

BASE_PATH = "C:/Users/youngho.cha/OneDrive - West Point/Desktop/XE402/df_data/"

for path in DATASET_PATHS:
    video_path = BASE_PATH + DATASET_PATHS[path] + "videos/"
    for video in os.listdir(video_path):
        cam = cv2.VideoCapture(video_path + video)
        if not os.path.exists("extracted2/" + DATASET_PATHS[path] + "images/" + video[:-4]):
            os.makedirs("extracted2/" + DATASET_PATHS[path] + "images/" + video[:-4])
        for i in range(61):
            ret, frame = cam.read()
            #half second timestep
            if ret and i % 15 == 0:
                name = "./extracted2/" + DATASET_PATHS[path] + "images/" + video[:-4] + "/frame" + str(i) + ".jpg"
                cv2.imwrite(name, frame)
        print("5 frames extracted from " + video)
        cam.release()
        cv2.destroyAllWindows()