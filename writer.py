from PIL import Image, ImageFont, ImageDraw, ImageFilter
import os
def write_text(id,title_text,lan,font="NerkoOne-Regular.ttf"):
    parametrlar = {
        "1.jpg": [[500, 755], "#023047", 45, 90],
        "2.jpg": [[460, 675], "#d6ccc2", 50, 80],
        "3.jpg": [[495, 555], "#e7c6ff", 50, 100],
        "4.jpg": [[495, 565], "#344e41", 45, 100],
        "5.jpg": [[510, 755], "#feeafa", 50, 100],
        "6.jpg": [[475, 605], "#dde5b6", 45, 60],
        "7.jpg": [[520, 725], "#e9edc9", 45, 90],
    }

    n = 0
    for photo in os.listdir("photos"):
        n+=1
        my_image = Image.open('photos/'+photo)
        title_font = ImageFont.truetype('fonts/'+font, parametrlar[photo][3])
        image_editable = ImageDraw.Draw(my_image)
        image_editable.text((parametrlar[photo][0][0]-((len(title_text)*parametrlar[photo][2])/2), parametrlar[photo][0][1]), title_text, parametrlar[photo][1], font=title_font)
        my_image.save("base/"+str(id)+'/photos/'+str(n)+".jpg")
    print("acc: writer_text")