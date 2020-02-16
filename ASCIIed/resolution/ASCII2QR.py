from PIL import Image

def ASCII2QR(asciiSTR, size, imageName):
	im = Image.new("RGB", (size, size))
	pix = im.load();

	idx = 0
	for i in range(0, im.height):
		for j in range(0, im.width):
			if asciiSTR[idx] == '1':
				pix[i,j] = (0,0,0)
			else:
				pix[i,j] = (255,255,255)
			idx = idx + 1
	im.save(imageName)
	print "QR code saved to: " + imageName


with open('ASCIIed.txt', 'r') as file:
	asciiQR=file.read().replace('\n', '')
	ASCII2QR(asciiQR, 150, "QR.png")

