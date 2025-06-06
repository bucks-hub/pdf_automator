import os

# PDF Configuration
PDF_URL = "http://sw061240.bmwgroup.net/reporting/public/110_Intranet/05_Sensoren/Stunde/Sensorenberichte_alle_heute.pdf"
SECTION_NAME = "Sensoren (gruppiert)"

# Path Configuration
DOWNLOAD_FOLDER = "C:/Users/qxz60kx/Desktop/projects/pdf_automator/downloads"
EXTRACTED_FOLDER = "C:/Users/qxz60kx/Desktop/projects/pdf_automator/downloads"
OUTPUT_PDF = os.path.join(EXTRACTED_FOLDER, "current_slides.pdf")

# Display Settings
SLIDE_DURATION = 5  # Seconds per slide
ZOOM_LEVEL = 3.0     # Rendering quality