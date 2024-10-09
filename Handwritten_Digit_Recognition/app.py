import pygame, sys
from pygame.locals import *
import numpy as np
from keras.models import load_model
import cv2

predict= True
window_x = 720
window_y = 480
BOUNDRYINC= 5
img_cnt=1

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

img_save=False
iswriting = False
num_xcord= []
num_ycord = []
model = load_model("/home/girish/Handwritten_Digit_Recognition/bestmodel.h5")
labels = {0:"Zero", 1:"One",
          2:"Two", 3:"Three",
          4:"Four", 5:"Five",
          6:"Six", 7:"Seven",
          8:"Zero", 9:"Nine",}
pygame.init()

font = pygame.font.Font("freesansbold.tff",18)
DISPLAYSURF=pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption("Digit Board")

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == MOUSEMOTION and  iswriting:
            xcord, ycord = event.pos
            pygame.draw.circle(DISPLAYSURF, white, (xcord, ycord), 4, 0)
            num_xcord.append(xcord)
            num_ycord.append(ycord)
        
        if event.type == MOUSEBUTTONDOWN:
            iswriting= True
        
        if event.type == MOUSEBUTTONUP:
            iswriting=False
            num_xcord = sorted(num_xcord)
            num_ycord= sorted(num_ycord)

            rect_min_x, rect_max_x = max(num_xcord[0]-BOUNDRYINC,0), min(window_x, num_xcord[-1]+BOUNDRYINC)
            rect_min_y, rect_max_y = max(num_ycord[0]-BOUNDRYINC,0), min(window_y, num_ycord[-1]+BOUNDRYINC)

            num_xcord = []
            num_ycord =[]
            img_arr = np.array(pygame.PixelArray(DISPLAYSURF))[rect_min_x, rect_max_x, rect_min_y re].T.astype(np.float32)
            if img_save:
                cv2.imwrite("image.png")
                img_cnt += 1
            
            if predict:
                image = cv2.resize(img_arr,(28,28))
                image = np.pad(image, (10,10),'constant', constant_values=0)
                image = cv2.resize(image, (28,28))/255

                labels = str(labels[np.argmax(model.predict(image.reshape(1,28,28,1)))])

                text_surface = FONT.render(labels, True, red, white)
                text_recobj = testing.get_rect()
                text_recobj.left, text_recobj.bottom = rect_min_x, rect_max_y

                DISPLAYSURF.blit(text_surface, text_recobj)
            
            if event.type == KEYDOWN:
                if event.unicode == "n":
                    DISPLAYSURF.fill(black)
    
    pygame.display.get_allow_screensaverupdate()





