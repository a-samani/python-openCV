import cv2
import os

os.system("cls")
file_name = input('please Enter your file name : \n')
image = cv2.imread(file_name)


def checkScale(image):
    for i in image[0]:
            if i[0]==i[1] and i[1]==i[2]:
                return 'Gray Scale'
            else:
                return 'Colored'

while True:

    userInput = input("\
        press 'g' for grey scale\n\
        press 'c' for color scale\n\
        press 'i' for info\n\
        press 'm' to move some part\n\
        press '0' to exit\n   \n")


#close
    if userInput == '0':
        exit(0)

# gray scale
    elif userInput =='g':
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Grayscale', gray_image)
        cv2.waitKey(0) 
        os.system("cls")


#  original 
    elif userInput =='c':
        cv2.imshow('color Scale',image)
        cv2.waitKey(0)
        os.system("cls")


# image info 
    elif userInput =='i':
         
        scale = checkScale(image)
        
        height = image.shape[0]
        width = image.shape[1]
        print('Image scale        : ',scale)
        print('Image Height       : ',height)
        print('Image Width        : ',width)    

    elif userInput =='m':
        height = image.shape[0]
        width = image.shape[1]
        part1 = image[0:int(height/5)]
        part2 = image[int(height)-len(part1):]
        
        image[int(height)-len(part1):] = part1
        cv2.imshow('color Scale',image)
        cv2.waitKey(0)
        os.system("cls")
