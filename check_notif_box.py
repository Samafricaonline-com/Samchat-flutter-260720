from PIL import Image
img = Image.open('android/app/src/main/res/drawable/ic_notification.png')
w, h = img.size
p = img.load()
for y in range(h):
    for x in range(w):
        if p[x,y][3] > 100:
            # print first opaque pixel to see where it starts
            print(f"Opaque at {x},{y}")
            break
    else:
        continue
    break
