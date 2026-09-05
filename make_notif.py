from PIL import Image

img = Image.open('assets/images/samchat_logo_clean.png').convert('RGB')
width, height = img.size

out = Image.new('RGBA', (width, height), (0,0,0,0))
pixels_in = img.load()
pixels_out = out.load()

for y in range(height):
    for x in range(width):
        r, g, b = pixels_in[x, y]
        # Orange is 252, 72, 4. Whiteness is min(G, B).
        # White is 255, 255, 255.
        whiteness = min(g, b)
        
        if whiteness <= 72:
            alpha = 0
        elif whiteness >= 240:
            alpha = 255
        else:
            alpha = int((whiteness - 72) * (255 / (255 - 72)))
            
        if alpha > 0:
            pixels_out[x, y] = (255, 255, 255, alpha)

bbox = out.getbbox()
if bbox:
    notif = out.crop(bbox)
    notif.save('android/app/src/main/res/drawable/ic_notification.png')

print("Notification silhouette created from new logo!")
