from PIL import Image,ImageEnhance,ImageFilter
import os
print(os.getcwd())
path = "./imgs"
pathOut = "/editedImgs"

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    # edit = img.filter(ImageFilter.SHARPEN).convert('L').filter(ImageFilter.GaussianBlur)
    edit = img.filter(ImageFilter.SHARPEN).filter(ImageFilter.SMOOTH)
    factor = 1.5
    enchancer = ImageEnhance.Contrast(edit)
    edit = enchancer.enhance(factor)
    clean_name = os.path.splitext(filename)[0]

    edit.save(f'.{pathOut}/{clean_name}_edited.jpg')