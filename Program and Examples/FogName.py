#Epson Virtual Port Assignment
#C:\Users\jrfcr\Downloads\SenddatV120_e\SenddatV120>
#senddat -b192 Output.txt com2

import cv2
import math
import os

dotDensity = 1  #0 and 1 are 8 high, 32 and 33 are 24 high  #1 works best
scaling = 8 # 8
data = ""
thresh = 140
numRec = 1
frameOrder = 0
stringFrame = 0
#print(f"GS \"(L\" {lower}   {higher}  48  67  48   \"G1\"   1 128   0 120   0  49")

rawName = "Your Text Here" + "\n\n\n" + ""
name =rawName.replace(" ","_")
size = bytes([17])

with open(f"C:/Users/jrfcr/Downloads/SenddatV120_e/SenddatV120/OutputForImage.txt", "w") as file:
    file.write("ESC @ \n")

    #this list slicing cuts the first two and last charachters off because str or an ascii
    #encoding does the b"" thing so this removes it
    #https://download4.epson.biz/sec_pubs/pos/reference_en/escpos/gs_exclamation.html
    #size encoding is done in one byte :(
    file.write("GS ! 17\n")
   # file.write("ESC M 98\n")
    #this list slicing cuts the first two and last charachters off because str or an ascii
    #encoding does the b"" thing so this removes it
    file.write(str(name.encode("ascii"))[2:-1] + "\n")
    #print(str(name.encode("ascii"))[2:])
    file.write("\nESC J 16")
    file.write("\n GS V 66 20")


            

    


