from PIL import Image
import os

path = os.getcwd()
print(path)

# Settings
canvas_width = 6000  # Width of the output canvas
canvas_height = 8000  # Height of the output canvas
logo = f"{path}/Flicker-Engineering_watermark_/Flicker_Engineering.png"  # Path to the watermark image
watermark_height = 30  # Desired height of each watermark
gap = 200  # Gap between watermarks
rotation_angle = 45  # Rotation angle for each watermark


# Load and resize the watermark image
watermark = Image.open(logo).convert("RGBA")

# Resize the watermark to the specified height, maintaining aspect ratio
aspect_ratio = watermark.width / watermark.height
new_width = int(watermark_height * aspect_ratio)
watermark = watermark.resize((new_width, watermark_height), Image.LANCZOS)

# Rotate the watermark by the specified angle
watermark = watermark.rotate(rotation_angle, expand=True)

# Create a transparent background canvas
canvas = Image.new("RGBA", (canvas_width, canvas_height), (0, 0, 0, 0))

# Paste rotated watermark in a repeated pattern with gaps
watermark_width, watermark_height = watermark.size

for y in range(0, canvas_height, watermark_height + gap):
    for x in range(0, canvas_width, watermark_width + gap):
        canvas.paste(watermark, (x, y), watermark)

# Save the final output as a PNG file with transparency
canvas.save(
    f"{path}/Flicker-Engineering_watermark_/Flicker-Engineering_watermark_output.png",
    "PNG",
)

print("Watermark created successfully as 'Flicker-Engineering_watermark_output.png'")
