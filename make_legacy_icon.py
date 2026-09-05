from PIL import Image

# Open the perfectly transparent foreground
fg = Image.open('assets/images/ic_foreground.png')
w, h = fg.size

# Create a solid background
bg = Image.new('RGBA', (w, h), "#fe6809")

# Paste foreground onto background
bg.paste(fg, (0, 0), fg)

# Save as legacy icon
bg.save('assets/images/ic_legacy.png')
print("ic_legacy.png created!")
