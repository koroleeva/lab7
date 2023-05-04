

def task1():

    from PIL import Image
    name = "sea.jpg"
    with Image.open(name) as img:
        img.load()

    img.show()
    width, height = img.size


    format = img.format


    mode = img.mode


    print("Ширина: ", width)
    print("Высота: ", height)
    print("Формат: ", format)
    print("Цветовая модель: ", mode)


def task2():
    from PIL import Image
    name = "sea.jpg"
    with Image.open(name) as img:
        img.load()
    newimg = img.resize((img.width // 3, img.height // 3))
    newimg.save("resized_sea.jpg")
    newimg = img.rotate(180)
    newimg.save("rotate_sea.jpg")
    newimg = img.transpose(Image.FLIP_LEFT_RIGHT)
    newimg.save("flip_sea.jpg")


def task3():
    from PIL import Image, ImageFilter
    names = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg']

    for file in names:
        with Image.open(file) as img:
            img.load()
            newimg = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
            newimg.show()
            newimg.save('new' + file)

pass

def task4():
    from PIL import Image

    water = 'watermark.png'
    with Image.open(water) as img_water:
        img_water.load()

    img_water = Image.open(water)
    img_water = img_water.resize((img_water.width // 2, img_water.height // 2))
    name = 'sea.jpg'
    with Image.open(name) as img:
        img.load()

    img.paste(img_water, (2800, 1300), img_water)
    img.save('watermark_sea.jpg')


task1()
task2()
task3()
task4()