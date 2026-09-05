from PIL import Image
img = Image.open('assets/images/samchat_logo_clean.png')
w, h = img.size
p = img.load()
for y in range(h):
    for x in range(w):
        c = p[x,y]
        # check if it's not orange and not transparent
        if c[3] > 100:
            if c[0] < 200 or c[1] > 100 or c[2] > 100:
                # it's not orange
                if c[0] > 200 and c[1] > 200 and c[2] > 200:
                    pass # white S
                else:
                    print(f"Found weird color {c} at {x},{y}")
                    break
