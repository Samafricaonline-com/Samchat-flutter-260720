from PIL import Image, ImageDraw
import math

img = Image.open('assets/images/samchat_logo.png').convert('RGBA')
pixels = img.load()
width, height = img.size

# We will implement a simple flood fill to make the background transparent
# We'll start from (0,0), (width-1, 0), (0, height-1), (width-1, height-1)

def is_background(r, g, b):
    # The checkerboard is usually white (255,255,255) and light grey (e.g. 200,200,200)
    # The orange logo has high saturation.
    cmax = max(r, g, b)
    cmin = min(r, g, b)
    diff = cmax - cmin
    # if it has low saturation and is relatively bright, it's background
    return diff < 40 and cmax > 100

to_visit = [(0,0), (width-1, 0), (0, height-1), (width-1, height-1)]
visited = set()

while to_visit:
    x, y = to_visit.pop()
    if (x, y) in visited:
        continue
    visited.add((x, y))
    
    r, g, b, a = pixels[x, y]
    if is_background(r, g, b):
        pixels[x, y] = (0, 0, 0, 0)
        
        # add neighbors
        if x > 0: to_visit.append((x-1, y))
        if x < width - 1: to_visit.append((x+1, y))
        if y > 0: to_visit.append((x, y-1))
        if y < height - 1: to_visit.append((x, y+1))

# Also crop to the non-transparent bounding box with some padding
min_x, min_y = width, height
max_x, max_y = 0, 0

for y in range(height):
    for x in range(width):
        r, g, b, a = pixels[x, y]
        if a > 0:
            if x < min_x: min_x = x
            if x > max_x: max_x = x
            if y < min_y: min_y = y
            if y > max_y: max_y = y

# Make a square crop
size = max(max_x - min_x, max_y - min_y)
# add 10% padding
padding = int(size * 0.1)
size += padding * 2

center_x = (min_x + max_x) // 2
center_y = (min_y + max_y) // 2

crop_box = (
    center_x - size // 2,
    center_y - size // 2,
    center_x + size // 2,
    center_y + size // 2
)

# create a new transparent image for the crop
out = Image.new('RGBA', (size, size), (0,0,0,0))
cropped = img.crop(crop_box)
out.paste(cropped, (0,0))
out.save('assets/images/samchat_logo_clean.png')
print("Cleaned and saved to samchat_logo_clean.png")
