import sys
import os
from PIL import Image

# Grab the first(jpg_image_folder) and second (converted_PNG_img_folder) argument
jpg_Image_folder = sys.argv[1] # 0 agrs is JPGtoPNGconverter.py and 1 args is JPG_Image_Folder
png_output_folder = sys.argv[2] # 2 args is Converted_PNG_img_Folder
print(jpg_Image_folder,png_output_folder)
if not os.path.exists(png_output_folder):
    os.makedirs(png_output_folder)
for filename in os.listdir(jpg_Image_folder):
    img = Image.open(f"{jpg_Image_folder}{filename}")
    clean_name = os.path.splitext(filename)[0] # Firstly need to clean the image file until (.jpeg)
    img.save(f"{png_output_folder}{clean_name}.png", "png")
    print("You Converted Image JPG to PNG file Successfully !!!")