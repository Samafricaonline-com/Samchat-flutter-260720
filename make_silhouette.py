from PIL import Image

img = Image.open('assets/images/samchat_logo_clean.png')
pixels = img.load()
width, height = img.size

# Create a new transparent image
out = Image.new('RGBA', (width, height), (0,0,0,0))
out_pixels = out.load()

for y in range(height):
    for x in range(width):
        r, g, b, a = pixels[x, y]
        if a > 200:
            # Check if it's white (the speech bubble or 'S')
            if r > 200 and g > 200 and b > 200:
                out_pixels[x, y] = (255, 255, 255, 255)

out.save('android/app/src/main/res/drawable/ic_notification.png')
print("Silhouette created and saved as ic_notification.png")
