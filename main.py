import qrcode

from PIL import Image

logo_path = "logo.png"

logo = Image.open(logo_path)

basewidth = 100

wpercent = basewidth / float(logo.size[0])

hsize = int((float(logo.size[1]) * float(wpercent)))

logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)

QRcode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)

url = "https://github.com/almazkun"

QRcode.add_data(url)

QRimg = QRcode.make_image(back_color="white").convert("RGB")

QRimg = QRcode.make_image(
    back_color="white").convert('RGB')

pos = ((QRimg.size[0] - logo.size[0]) // 2,
       (QRimg.size[1] - logo.size[1]) // 2)

QRimg.paste(logo, pos)

def main():
    QRimg.save("qr.png")


if __name__ == "__main__":
    main()
