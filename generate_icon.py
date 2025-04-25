# generate_icon.py
from PIL import Image, ImageDraw, ImageFont
import os

# ensure assets folder exists
os.makedirs("assets", exist_ok=True)

# create 512×512 white image
size = (512, 512)
img = Image.new("RGB", size, "white")
draw = ImageDraw.Draw(img)

# draw black border
border = 10
draw.rectangle(
    [border, border, size[0] - border, size[1] - border],
    outline="black",
    width=border
)

# draw centered text "Icon"
try:
    font = ImageFont.truetype("arial.ttf", 64)
except IOError:
    font = ImageFont.load_default()
text = "Icon"
w, h = draw.textsize(text, font=font)
draw.text(((size[0] - w) / 2, (size[1] - h) / 2), text, fill="black", font=font)

# save to assets/icon.png
icon_path = "assets/icon.png"
img.save(icon_path)
print(f"✅ Created placeholder icon at {icon_path}")
