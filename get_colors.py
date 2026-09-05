from PIL import Image
img = Image.open('assets/images/samchat_logo_clean.png')
p = img.load()
w, h = img.size
cx, cy = w//2, h//2

def find_orange(start_y, step):
    y = start_y
    while 0 <= y < h:
        r, g, b, a = p[cx, y]
        if a > 250:
            cmax = max(r,g,b)
            cmin = min(r,g,b)
            if cmax - cmin > 100 and cmax > 200: # vivid orange
                return r, g, b
        y += step
    return None

top = find_orange(cy - 200, -1)
bottom = find_orange(cy + 200, 1)

print(f"Top: {top}")
print(f"Bottom: {bottom}")

# create background
out = Image.new('RGBA', (w, h))
op = out.load()
r1, g1, b1 = top
r2, g2, b2 = bottom

for y in range(h):
    ratio = y / h
    r = int(r1 + (r2 - r1) * ratio)
    g = int(g1 + (g2 - g1) * ratio)
    b = int(b1 + (b2 - b1) * ratio)
    for x in range(w):
        op[x, y] = (r, g, b, 255)

out.save('assets/images/launcher_bg.png')
print("launcher_bg.png created")
