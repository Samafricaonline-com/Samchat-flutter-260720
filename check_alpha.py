from PIL import Image

img = Image.open('assets/images/samchat_logo_clean.png')
pixels = img.load()
width, height = img.size

# Let's count opaque and transparent pixels
transparent = 0
opaque = 0

for y in range(height):
    for x in range(width):
        r, g, b, a = pixels[x, y]
        if a < 10:
            transparent += 1
        else:
            opaque += 1

print(f"Transparent: {transparent}, Opaque: {opaque}")

# Check center pixels (the S)
r, g, b, a = pixels[width//2, height//2]
print(f"Center pixel: r={r} g={g} b={b} a={a}")
