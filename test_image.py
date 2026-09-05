from PIL import Image

img = Image.open('assets/images/samchat_logo_clean.png')
print(f"Mode: {img.mode}")
w, h = img.size
p = img.load()
if img.mode == 'RGBA':
    print(f"Top edge (RGBA): {p[w//2, 0]}")
    print(f"Center (RGBA): {p[w//2, h//2]}")
else:
    print(f"Top edge (RGB): {p[w//2, 0]}")
    print(f"Center (RGB): {p[w//2, h//2]}")
