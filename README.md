# ReceiptPrinter
Converts images to ESC/POS control commands for a TM-T90 receipt printer
![scan_eih20jc_2025-01-06-15-34-20-1](https://github.com/user-attachments/assets/c63e7d4f-fa43-4968-a936-e3aae6bf6477)

To make an image to send:  
- use 'https://www.simpleimageresizer.com/upload' to resize images and 'https://app.dithermark.com/' to dither images  
- the width should be divisible by 256  

To convert an image to commands:  
- change folder paths in program
- change scaling to suit image
- run program labelled "Fog" for one image
- run program labelled "FogAnim" for an animation, I recommend creating a file for the many txt's
- run program labelled "FogName" for text

To send the commands:   
- downlaod Epson Virtual Port Assignment  
- open cmd and cd into \SenddatV120
- run 'senddat -b192 OutputForImage.txt com2' for images and text
- run 'runner.bat' for animations
