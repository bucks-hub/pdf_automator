import os

# PDF Configuration
PDF_URL = "Link to the pdf file"
SECTION_NAME = "Key word to filter the slideshow pages"

# Path Configuration
DOWNLOAD_FOLDER = "folder to down the pdf file"
EXTRACTED_FOLDER = "folder to save the extracted pdf file"
OUTPUT_PDF = os.path.join(EXTRACTED_FOLDER, "current_slides.pdf")

# Display Settings
SLIDE_DURATION = 5  # Seconds per slide
ZOOM_LEVEL = 3.0     # Rendering quality
