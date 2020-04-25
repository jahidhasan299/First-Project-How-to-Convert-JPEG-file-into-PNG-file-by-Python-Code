from PIL import Image, ImageFilter

img = Image.open("Tiger.png")
filtered_img = img.filter(ImageFilter.SHARPEN) #we can use here: BLUR
filtered_img = img.convert("L") #convert RGB to  Greyscale
rotating_img = filtered_img.rotate(180)
resizing_img = rotating_img.resize((800,800))
crop_size_box = (300,300,600,600)
cropping_img = resizing_img.crop(crop_size_box)
cropping_img.thumbnail((400,400))
cropping_img.save("Tiger_blur.png","png")
cropping_img.show()
