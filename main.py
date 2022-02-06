from PIL import Image, ImageDraw, ImageFont

print("San-Andreas National Guard 2022")
print("By Pavel Rose #65001 (Void)")
print("")

image = Image.open('files/usaf.png')
avatar = Image.open('files/avatar.png')
font = ImageFont.truetype('files/Gilroy-Semibold.ttf', size=18)

staticId = input("[1] Введите staticID игрока: ")
name = input("[2] Введите Имя Фамилию игрока: ")
age = input("[3] Введите возраст игрока: ")
gender = input("[4] Введите гендер (M/W): ")
call_sign = input("[5] Введите позывной игрока: ")

image.paste(avatar, (40, 100), avatar)

draw_text = ImageDraw.Draw(image)
draw_text.text(
    (210, 123),
    staticId,
    font=font,
    fill='#6E9654'
)
draw_text.text(
    (294, 123),
    age,
    font=font,
    fill='#6E9654'
)
draw_text.text(
    (374, 123),
    gender,
    font=font,
    fill='#6E9654'
)
draw_text.text(
    (210, 174),
    name,
    font=font,
    fill='#6E9654'
)
draw_text.text(
    (210, 225),
    call_sign,
    font=font,
    fill='#6E9654'
)
image.show()

image.save(staticId + '_license.png')

