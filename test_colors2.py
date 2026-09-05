from PIL import Image
img = Image.open('assets/images/samchat_logo_clean.png')
w, h = img.size
p = img.load()
colors = {}
for y in range(0, h, 100):
    for x in range(0, w, 100):
        c = p[x,y]
        if c[3] > 0: # only opaque
            colors[c] = colors.get(c, 0) + 1
# Print top 5 colors
for k, v in sorted(colors.items(), key=lambda item: item[1], reverse=True)[:5]:
    print(k, v)
