from PIL import Image

img = Image.open('assets/images/samchat_logo_clean.png')
p = img.load()
w, h = img.size

def get_outer_color(y):
    # scan left to right until opaque
    for x in range(w):
        if p[x, y][3] > 200:
            return p[x+5, y] # go 5 pixels in to avoid antialiasing
    return None

print(f"Top-ish edge: {get_outer_color(h//4)}")
print(f"Mid edge: {get_outer_color(h//2)}")
print(f"Bottom-ish edge: {get_outer_color(3*h//4)}")
