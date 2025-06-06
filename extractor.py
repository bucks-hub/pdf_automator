import pymupdf
import os
from config import SECTION_NAME, EXTRACTED_FOLDER, OUTPUT_PDF


def extract_section(input_path):
    """Extract target section from PDF"""
    try:
        doc = pymupdf.open(input_path)
        start_page = None
        absence_count = 0

        # Find section start
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            if SECTION_NAME.lower() in page.get_text().lower():
                start_page = page_num
                break

        if start_page is None:
            return False

        # Find section end
        end_page = len(doc) - 1
        for page_num in range(start_page, len(doc)):
            page = doc.load_page(page_num)
            if SECTION_NAME.lower() not in page.get_text().lower():
                absence_count += 1
                if absence_count >= 2:
                    end_page = page_num - absence_count
                    break
            else:
                absence_count = 0

        # Save extracted section
        extracted = pymupdf.open()
        extracted.insert_pdf(doc, from_page=start_page, to_page=end_page)
        os.makedirs(EXTRACTED_FOLDER, exist_ok=True)
        extracted.save(OUTPUT_PDF)
        print(f"Updated slides: {OUTPUT_PDF}")
        return True

    except Exception as e:
        print(f"Extraction failed: {e}")
        return False