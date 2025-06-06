import os
import requests
import time
from config import PDF_URL, DOWNLOAD_FOLDER


def download_pdf():
    """Download PDF with timestamped filename"""
    try:
        os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filename = f"pdf_{timestamp}.pdf"
        filepath = os.path.join(DOWNLOAD_FOLDER, filename)

        response = requests.get(PDF_URL)
        response.raise_for_status()

        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"Downloaded new PDF: {filepath}")
        return filepath

    except Exception as e:
        print(f"Download failed: {e}")
        return None