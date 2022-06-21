# Adapted from https://stackoverflow.com/a/47877930/extract-images-from-pdf-without-resampling-in-python, kateryna, 2017-12-18

import os
import fitz  # pip install --upgrade pip; pip install --upgrade pymupdf
from tqdm import tqdm # pip install tqdm
import logging
import re

def export_images_from_document(doc: fitz.Document, base_name: str, output_directory: str): 
    image_counter = 0
    exported_files = []
    for i in tqdm(range(len(doc)), desc=base_name):
        page_images = doc.get_page_images(i)
        for img in page_images:
            image_counter += 1
            xref = img[0]
            pix = fitz.Pixmap(doc, xref)
            if not pix.colorspace.name in (fitz.csGRAY.name, fitz.csRGB.name):
                pix = fitz.Pixmap(fitz.csRGB, pix)
            page_number = i + 1
            file_name = "%s_p%s-n%s-x%s.png" % (base_name, page_number, image_counter, xref)
            output_path = os.path.join(output_directory, file_name)
            # Pixmap.save() does not override already existing files (it silently fails), so we have to provde a warning.
            exported_files.append({
                "file_name": file_name,
                "page_id": page_number,
                "image_id": image_counter,
                "xref_id": xref,
            })
            if os.path.exists(output_path):
                logging.warn("Skipping image '%s' because file already exists. " % file_name)
                continue
            pix.save(output_path)
    return exported_files


def export_images_from_pdf_files_in_directory(input_directory: str, output_directory: str):
    for path in os.listdir(input_directory):
        if not ".pdf" in path:
            continue
        doc_path = os.path.join(input_directory, path)
        doc = fitz.Document(doc_path)
        file_name, ext = os.path.splitext(path)
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)
        exported_images = export_images_from_document(doc, file_name, output_directory)
        create_html_preview(exported_images, output_directory, file_name)


def populate_html_interpolation(raw_string: str, interpolation_id: str, inserted_string: str):
    interpolation = "<!-- TEMPLATE: %s -->" % interpolation_id
    return re.sub(interpolation, inserted_string, raw_string)


def create_html_preview(images: dict, output_directory: str, output_name: str):
    template_path = "src\\preview-template.html"
    output_path = os.path.join(output_directory, output_name + ".html")
    image_tags = []
    for image in images:
        caption = "Page %s, Image %s (Id %s)" % (image["page_id"], image["image_id"], image["xref_id"])
        image_tags.append("<img src=\"./%s\" alt=\"%s\">" % (image["file_name"], caption))
    with open(template_path, "r") as f:
        template = f.read()
        processed_template = template
        image_tags_markup = "\n".join(image_tags)
        processed_template = populate_html_interpolation(processed_template, "Title", output_name)
        processed_template = populate_html_interpolation(processed_template, "Images", image_tags_markup)
    with open(output_path, "w") as f:
        f.write(processed_template)


export_images_from_pdf_files_in_directory("src", "dist")
