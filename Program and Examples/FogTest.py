import cv2
import os

# Configuration
fileName = "enigmatriz5.png"  # must include file format
dotDensity = 0  # 0 and 1 are 8 high; 32 and 33 are 24 high; 1 works best
scaling = 8  # Height scaling for each step
thresh = 140  # Threshold for binarization
chunkWidth = 256  # Maximum width per chunk

# Load the image as grayscale
img = cv2.imread(f"C:/Users/jrfcr/Desktop/Sleuth (2)/{fileName}", cv2.IMREAD_GRAYSCALE)

height, width = img.shape

# Open the output file
with open(f"C:/Users/jrfcr/Downloads/SenddatV120_e/SenddatV120/OutputForImage.txt", "w") as file:
    file.write("ESC @ \n")  # Initialize printer
    
    # Iterate through image in vertical steps
    for i in range(0, height - scaling, scaling):
        # Process the image in horizontal slices of `chunkWidth`
        for start_col in range(0, width, chunkWidth):
            end_col = min(start_col + chunkWidth, width)  # Ensure not to exceed image width
            slice_width = end_col - start_col
            
            nH = slice_width // 256  # High byte of slice width
            nL = slice_width % 256  # Low byte of slice width
            
            data = ""  # Initialize data for this chunk
            
            # Process each row in the current vertical slice
            for k in range(8):  # Vertical pixel grouping (dot matrix height)
                if i + k >= height:  # Ensure we stay within image bounds
                    break
                for j in range(start_col, end_col):
                    if img[i + k, j] > thresh:
                        data += "00 "  # White pixel
                    else:
                        data += "FF "  # Black pixel
            
            # Write ESC command for this slice
            file.write(f"\nESC * {dotDensity} {nL} {nH} {data}")
        
        file.write("\nESC J 16")  # Line feed (adjust for printer spacing)
    
    # Finalize printing
    file.write("\n GS V 66 20")
