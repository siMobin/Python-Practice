import os
from PIL import Image
from reportlab.pdfgen import canvas

path = os.getcwd()


def generate_pdf_from_images(image_folder, output_pdf):
    # Create a canvas to generate the PDF
    c = canvas.Canvas(output_pdf)

    # Iterate through all the images in the folder
    for image_name in os.listdir(image_folder):
        # Only process image files
        if image_name.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):
            image_path = os.path.join(image_folder, image_name)

            # Open the image using PIL to get its size
            image = Image.open(image_path)
            img_width, img_height = image.size

            # Set the PDF page size to match the image size
            c.setPageSize((img_width, img_height))  # Set page size to image size

            # Draw the image on the page
            c.drawImage(image_path, 0, 0, width=img_width, height=img_height)

            # Start a new page for the next image
            c.showPage()

    # Save the generated PDF
    c.save()


# Specify the folder containing images and the output PDF filename
image_folder = f"{path}/ev"
output_pdf = "output_ev.pdf"  # Replace with desired output PDF filename

# Generate the PDF
generate_pdf_from_images(image_folder, output_pdf)

print(f"PDF generated successfully: {output_pdf}")
