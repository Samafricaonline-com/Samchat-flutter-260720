from PIL import Image
from collections import Counter

img = Image.open('assets/images/samchat_logo_clean.png')
pixels = img.load()
width, height = img.size

colors = []
for y in range(height):
    for x in range(width):
        r, g, b, a = pixels[x, y]
        if a > 200:
            if r > 200 and g > 200 and b > 200:
                continue # ignore white S
            colors.append(f"#{r:02x}{g:02x}{b:02x}")

counter = Counter(colors)
for c, count in counter.most_common(5):
    print(c, count)
