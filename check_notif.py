from PIL import Image
img = Image.open('android/app/src/main/res/drawable/ic_notification.png')
w, h = img.size
p = img.load()
colors = {}
for y in range(0, h, 10):
    for x in range(0, w, 10):
        c = p[x,y]
        colors[c] = colors.get(c, 0) + 1
for k, v in sorted(colors.items(), key=lambda item: item[1], reverse=True)[:5]:
    print(k, v)
