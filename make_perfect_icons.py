from PIL import Image

img = Image.open('assets/images/samchat_logo_clean.png').convert('RGB')
width, height = img.size

out_fg = Image.new('RGBA', (width, height), (0,0,0,0))
pixels_in = img.load()
pixels_fg = out_fg.load()

for y in range(height):
    for x in range(width):
        r, g, b = pixels_in[x, y]
        whiteness = min(g, b)
        
        if whiteness <= 140:
            alpha = 0
        elif whiteness >= 240:
            alpha = 255
        else:
            alpha = int((whiteness - 140) * (255 / 100))
            
        if alpha > 0:
            pixels_fg[x, y] = (255, 255, 255, alpha)

out_fg.save('assets/images/ic_foreground.png')

bbox = out_fg.getbbox()
if bbox:
    notif = out_fg.crop(bbox)
    notif.save('android/app/src/main/res/drawable/ic_notification.png')

print("Perfect transparent foreground recreated!")
