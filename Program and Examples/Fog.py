#Epson Virtual Port Assignment
#cd C:\Users\jrfcr\Downloads\SenddatV120_e\SenddatV120
#senddat -b192 OutputForImage.txt com2

import cv2
import math
import os


fileName = "OT1.png" #must include file format
dotDensity = 1 #0 and 1 are 8 high, 32 and 33 are 24 high  #1 works best
scaling = 8 # 8
xscalingFactor = 1
yscalingFactor = 0.1

#Reciept Workflow (W x H)
#-----------------------------
#The width is 256 pixels/74mm (~1mm = 3.46 pixels), if an image is made up of multiple 
#reciepts the number should cleanly divide by 256 opt:  256-512-768-1023
# the width cannot be 1024 or greater, I think)

#The height is 256 pixels/492mm (~1mm = 1.92pixels) hence 0.555 scaling factor
#The width should generally be the shorter side to introduce fewer break lines so
#rotate landscape images

#an 880w x 1200h image is 250mm x 625mm with 8 scaling, 250mm x 310mm with 16 scaling
#8 scaling skips no lines images should ideally have no scaling in this step as it skips chunks

#Cubic interpolation can be done with the commented out function but its almost blurry and
#cause scaling skips in chunk, resizing the image beofre with scaling factor on height and
#width in factors of 256

data = ""
thresh = 140 #140
numRec = 1
frameOrder = 0
stringFrame = 0
#print(f"GS \"(L\" {lower}   {higher}  48  67  48   \"G1\"   1 128   0 120   0  49")

chunkWidth = 256
chunkNum = 0
img = cv2.imread(f"C:/Users/jrfcr/Desktop/Sleuth (2)/{fileName}", cv2.IMREAD_GRAYSCALE)


#-------------------o-o-o-o-o-o-o-o-o-o-o-------------------
#img = cv2.resize(img, None, fx= xscalingFactor, fy= yscalingFactor, interpolation= cv2.INTER_CUBIC)
#-------------------o-o-o-o-o-o-o-o-o-o-o-------------------

height = img.shape[0]
width = img.shape[1]

nH = int(width/256)
nL = width % 256

for row in range(height):          # Loop through all rows
    for col in range(256):         # Loop through the first 256 columns
            target_col = (256*chunkNum) + col  # Destination column (e.g., starting at column 512)
            if target_col < width:  # Ensure it doesn't go out of bounds
                img[row, col] = img[row, target_col]  # Copy the pixel value



with open(f"C:/Users/jrfcr/Downloads/SenddatV120_e/SenddatV120/OutputForImage.txt", "w") as file:
    file.write("ESC @ \n")
    
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


            

    


