#Epson Virtual Port Assignment
#C:\Users\jrfcr\Downloads\SenddatV120_e\SenddatV120>
#senddat -b192 Output.txt com2

import cv2
import math
import os

folder = "C:/Users/jrfcr/Desktop/RecVidConv"
fileName = "BOAT3.png" #must include file format
dotDensity = 1  #0 and 1 are 8 high, 32 and 33 are 24 high  #1 works best
scaling = 8 # 8
data = ""
thresh = 140
numRec = 1
frameOrder = 0
stringFrame = 0
#print(f"GS \"(L\" {lower}   {higher}  48  67  48   \"G1\"   1 128   0 120   0  49")


def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return(images)

scans = load_images_from_folder(folder)

height = scans[0].shape[0]
width = scans[0].shape[1]

nH = int(width/256)
nL = width % 256

# reads image 'opencv-logo.png' as grayscale
for q in range(len(scans)):
    #img = cv2.imread(scans[q], cv2.IMREAD_GRAYSCALE)
    img = cv2.cvtColor(scans[q], cv2.COLOR_BGR2GRAY)
    print(f"Frame {q}")
    stringFrame = str(q)
    frameOrder = [ord(stringFrame) for stringFrame in str(q)]
    frameOrderREP = str(frameOrder).replace("[","").replace("]","").replace(","," ")
    

    with open(f"C:/Users/jrfcr/Desktop/RecVidConv/TXTs/Output{q}.txt", "w") as file:
        file.write("ESC @ \n")
        file.write(f"{frameOrderREP}") #48 = 0 57 = 9
        file.write("\nESC J 16")
        for x in range(0, numRec):
                
            #file.write(f"\nESC * {dotDensity} {nL+4} {nH+5}  0xF5 0xF5 0xF5 0xF5 0xF5 0xF5")
            for i in range(0,height-scaling,scaling):
                data = ""
                for j in range(width):
                    
                    bitVal = [128, 64, 32, 16, 8, 4, 2, 1]

                    for k in range(0, 8):
                        if (img[(i+k)][j]  > thresh):
                            bitVal[k] = 0
                        else:
                            continue
                    data = data + hex(sum(bitVal)) + " "
                file.write(f"\nESC * {dotDensity} {nL} {nH} {data}")
            #file.write(f"\nESC * {dotDensity} {nL+4} {nH+5} {data}")
            file.write("\nESC J 16")
            file.write("\n GS V 66 20")


            

    


