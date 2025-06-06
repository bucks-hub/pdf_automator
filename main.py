import os
import schedule
import time
from threading import Thread
from downloader import download_pdf
from extractor import extract_section
from display import run_slideshow
from config import DOWNLOAD_FOLDER, EXTRACTED_FOLDER


def hourly_task():
    """Scheduled task to update content"""
    print("\n--- Running hourly update ---")
    new_pdf = download_pdf()
    if new_pdf:
        if extract_section(new_pdf):
            print("Update successful!")
        else:
            print("No section found - keeping previous slides")


def scheduler_thread():
    """Background scheduling thread"""
    schedule.every().hour.at(":00").do(hourly_task)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    # Create needed directories
    os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)
    os.makedirs(EXTRACTED_FOLDER, exist_ok=True)

    # Initial content download
    hourly_task()

    # Start background scheduler
    Thread(target=scheduler_thread, daemon=True).start()

    # Start slideshow (blocking)
    run_slideshow()