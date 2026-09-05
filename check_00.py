from PIL import Image
img = Image.open('assets/images/samchat_logo_clean.png')
print(img.load()[0,0])
