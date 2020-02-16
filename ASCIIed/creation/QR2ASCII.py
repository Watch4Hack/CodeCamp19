from PIL import Image

def QR2ASCII(size, imageName):
	im = Image.open(imageName)
	pix = im.load();

	for i in range(0, im.height):
		line = ""
		for j in range(0, im.width):
			line += str(pix[i,j])
		print line

QR2ASCII(150, "qrcode.png")
