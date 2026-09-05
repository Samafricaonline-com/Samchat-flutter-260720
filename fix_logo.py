from PIL import Image

img = Image.open('assets/images/samchat_logo.png').convert('RGBA')
pixels = img.load()
width, height = img.size

# Let's find the bounding box of the orange part
# We assume the checkerboard is grey/white (R, G, B are similar)
# Orange has high R, some G, low B

min_x, min_y = width, height
max_x, max_y = 0, 0

for y in range(height):
    for x in range(width):
        r, g, b, a = pixels[x, y]
        # Check if color is NOT grey/white (i.e. it's orange)
        if r > 150 and g < 150 and b < 50: # wait, orange is like 255, 165, 0
            pass
        # Better: check saturation
        cmax = max(r, g, b)
        cmin = min(r, g, b)
        diff = cmax - cmin
        if diff > 30: # it has some color
            if x < min_x: min_x = x
            if x > max_x: max_x = x
            if y < min_y: min_y = y
            if y > max_y: max_y = y

print(f"Logo bounds: {min_x}, {min_y} to {max_x}, {max_y}")
