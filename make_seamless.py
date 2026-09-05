from PIL import Image
import math

img = Image.open('assets/images/samchat_logo_clean.png')
pixels = img.load()
width, height = img.size

# Find the center
cx, cy = width / 2, height / 2

# We know the logo is roughly circular. 
# Let's find the radius where transparency begins for each angle.
# Then we take the color at that boundary and stretch it outward.

out = Image.new('RGBA', (width, height), (0,0,0,0))
out_pixels = out.load()

for y in range(height):
    for x in range(width):
        dx = x - cx
        dy = y - cy
        dist = math.hypot(dx, dy)
        
        # Original pixel
        r, g, b, a = pixels[x, y]
        
        if a > 200:
            out_pixels[x, y] = (r, g, b, 255)
        else:
            # It's transparent. We need to extrapolate from the edge.
            # Walk towards the center until we hit an opaque pixel.
            if dist == 0:
                out_pixels[x, y] = (r, g, b, 255)
                continue
                
            ux, uy = dx / dist, dy / dist
            
            # Find the edge
            edge_r, edge_g, edge_b = 255, 255, 255
            found = False
            for d in range(int(dist), 0, -1):
                nx = int(cx + ux * d)
                ny = int(cy + uy * d)
                if 0 <= nx < width and 0 <= ny < height:
                    nr, ng, nb, na = pixels[nx, ny]
                    if na > 200:
                        edge_r, edge_g, edge_b = nr, ng, nb
                        found = True
                        break
            
            if found:
                out_pixels[x, y] = (edge_r, edge_g, edge_b, 255)
            else:
                out_pixels[x, y] = (r, g, b, 255)

out.save('assets/images/samchat_logo_seamless.png')
print("Seamless image created!")
