import pygame
import os
import time
from PIL import Image
from io import BytesIO
import pymupdf
from config import OUTPUT_PDF, ZOOM_LEVEL, SLIDE_DURATION


def run_slideshow():
    """Continuous slideshow with auto-refresh"""
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    width, height = screen.get_size()

    def load_images():
        """Load images with quality rendering"""
        images = []
        try:
            doc = pymupdf.open(OUTPUT_PDF)
            for page in doc:
                pix = page.get_pixmap(matrix=pymupdf.Matrix(ZOOM_LEVEL, ZOOM_LEVEL), alpha=False)
                img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
                img_bytes = BytesIO()
                img.save(img_bytes, "PNG")
                img_bytes.seek(0)
                images.append(pygame.image.load(img_bytes))
            return images
        except:
            return []

    images = []
    current_slide = 0
    last_modified = 0
    last_change = 0

    while True:
        # Check for updates every 30 seconds
        if os.path.exists(OUTPUT_PDF):
            new_mtime = os.path.getmtime(OUTPUT_PDF)
            if new_mtime > last_modified:
                images = load_images()
                current_slide = 0
                last_modified = new_mtime
                print("Slides reloaded")

        # Handle slides
        if images:
            if time.time() - last_change > SLIDE_DURATION:
                current_slide = (current_slide + 1) % len(images)
                last_change = time.time()

            img = images[current_slide]
            scaled = pygame.transform.smoothscale(img, (width, height))
            screen.blit(scaled, (0, 0))
            pygame.display.flip()

        # Handle exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                    event.type == pygame.KEYDOWN and event.key in [pygame.K_ESCAPE, pygame.K_q]):
                pygame.quit()
                return

        pygame.time.Clock().tick(30)