import os
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

path = os.getcwd()


def generate_pdf_from_images(image_folder, output_pdf):
    # Create a canvas to generate the PDF
    c = canvas.Canvas(output_pdf, pagesize=letter)

    # Get the dimensions of the letter-sized page (8.5 x 11 inches)
    page_width, page_height = letter

    # Iterate through all the images in the folder
    for image_name in os.listdir(image_folder):
        # Only process image files
        if image_name.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):
            image_path = os.path.join(image_folder, image_name)

            # Open the image using PIL to get its size
            image = Image.open(image_path)
            img_width, img_height = image.size

            # Calculate scale to fit the image on the page
            scale = min(page_width / img_width, page_height / img_height)

            # Resize the image to fit the page
            img_width_scaled = img_width * scale
            img_height_scaled = img_height * scale

            # Draw the image onto the canvas
            c.drawImage(
                image_path, 0, 0, width=img_width_scaled, height=img_height_scaled
            )

            # End the page and start a new one for the next image
            c.showPage()

    # Save the generated PDF
    c.save()


# Specify the folder containing images and the output PDF filename
image_folder = f"{path}/ck2"
output_pdf = "ck2_output.pdf"  # Replace with desired output PDF filename

# Generate the PDF
generate_pdf_from_images(image_folder, output_pdf)

print(f"PDF generated successfully: {output_pdf}")
