from pdf2image import convert_from_path

pdf_file = "smallbook.pdf"

images = convert_from_path(pdf_file)

for i, image in enumerate(images):
    image.save(f"./data/strona_{i+1}.png", "PNG")