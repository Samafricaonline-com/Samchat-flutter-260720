from PIL import Image

img = Image.open('assets/images/samchat_logo_clean.png').convert('RGBA')
pixels = img.load()
width, height = img.size

out = Image.new('RGBA', (width, height))
out_pixels = out.load()

# Find all non-transparent pixels to avoid searching the whole image blindly
opaque = []
for y in range(height):
    for x in range(width):
        if pixels[x, y][3] > 0:
            opaque.append((x, y, pixels[x, y]))

# For each pixel, if it's transparent, find the closest opaque pixel
# To make it fast, we can just do a multi-pass distance transform or simple iterative smear
# iterative smear:
import time
start = time.time()

# We can just fill outwards.
import collections

queue = collections.deque()
for x, y, p in opaque:
    out_pixels[x, y] = p
    queue.append((x, y))

visited = set((x, y) for x, y, _ in opaque)

directions = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,-1), (1,-1), (-1,1)]

while queue:
    x, y = queue.popleft()
    p = out_pixels[x, y]
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < width and 0 <= ny < height:
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                # copy color, make fully opaque
                out_pixels[nx, ny] = (p[0], p[1], p[2], 255)
                queue.append((nx, ny))

out.save('assets/images/samchat_logo_filled.png')
print("Smear complete!")
