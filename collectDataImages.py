import cv2
import os
import time

def Capture_Video(n, delay):
    webcam = cv2.VideoCapture(0)
    images_from_video =[]
    if webcam.isOpened():

        while len(images_from_video)<n:
            time.sleep(delay)
            success, imageframe = webcam.read() # get frame per frame from the webcam

            if success:
                cv2.imshow('My webcam', imageframe) # show the frame
                images_from_video.append(imageframe)
            else:
                print('No image available')
            keystroke = cv2.waitKey(20) # Wait for Key press
            #wait for 20 miliseconds and destroys window if no key is pressed
            if (keystroke == 27):
                break # if key pressed is ESC then escape the loop

        webcam.release()
        cv2.destroyAllWindows()  
    return images_from_video

def save_images(im_list, path):
    for ind, img in enumerate(im_list):
        if not cv2.imwrite(os.path.join(path , '%s.jpg' %str(ind)), img):
            print("Error")


#im = Capture_Video(50, 1)
#path = r'C:/Users/ribal/Desktop/INF573/project/INF573/data/DROITE/D/'
#save_images(im, path)



