from PIL import Image

img = Image.open('assets/images/samchat_logo_clean.png')
pixels = img.load()
width, height = img.size

# Sample a pixel along the vertical center axis that is highly saturated
cx = width // 2

top_color = None
for y in range(height):
    r, g, b, a = pixels[cx, y]
    if a > 250:
        cmax = max(r, g, b)
        cmin = min(r, g, b)
        if cmax - cmin > 50: # saturated
            top_color = (r, g, b)
            break

bottom_color = None
for y in range(height-1, -1, -1):
    r, g, b, a = pixels[cx, y]
    if a > 250:
        cmax = max(r, g, b)
        cmin = min(r, g, b)
        if cmax - cmin > 50: # saturated
            bottom_color = (r, g, b)
            break

print(f"Top: {top_color}, Bottom: {bottom_color}")

# Create a gradient background
out = Image.new('RGBA', (width, height))
out_pixels = out.load()

r1, g1, b1 = top_color
r2, g2, b2 = bottom_color

for y in range(height):
    ratio = y / height
    r = int(r1 + (r2 - r1) * ratio)
    g = int(g1 + (g2 - g1) * ratio)
    b = int(b1 + (b2 - b1) * ratio)
    for x in range(width):
        out_pixels[x, y] = (r, g, b, 255)

# Paste the logo on top
out.paste(img, (0,0), img)
out.save('assets/images/samchat_logo_seamless.png')
print("Fast seamless image created!")
