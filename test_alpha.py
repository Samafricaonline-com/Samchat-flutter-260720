from PIL import Image

img = Image.open('assets/images/ic_foreground.png')
pixels = img.load()
w, h = img.size

# check edges
print(f"Top edge alpha: {pixels[w//2, 0][3]}")
print(f"Bottom edge alpha: {pixels[w//2, h-1][3]}")
print(f"Center alpha: {pixels[w//2, h//2][3]}")
