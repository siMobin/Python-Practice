import os
from pdf2image import convert_from_path
from PIL import Image

path = os.getcwd()
# Load the PDF and convert each page to an image
pdf_path = f"{path}/ck2_output.pdf"  # Pdf path
images = convert_from_path(pdf_path)

# Ensure the number of pages is even (if not, add an empty page)
if len(images) % 2 != 0:
    images.append(
        Image.new("RGB", images[0].size, (255, 255, 255))
    )  # Add blank page if necessary

# Loop through the pages in pairs and save as a single JPG image
for i in range(0, len(images), 2):
    # Get the width and height of the new image
    width = max(images[i].width, images[i + 1].width)
    height = images[i].height + images[i + 1].height  # Stack vertically

    # Create a new blank image with the calculated dimensions
    new_image = Image.new("RGB", (width, height))

    # Paste the first image on top
    new_image.paste(images[i], (0, 0))

    # Paste the second image below the first
    new_image.paste(images[i + 1], (0, images[i].height))

    # Save the merged image as JPG
    new_image.save(f"output_page_{i // 2 + 1}.jpg")

print("Conversion complete!")
