# Pillow: redimensionando imagens com python
# Essa biblioteca é o photoshop do Python
from PIL import Image

from pathlib import Path

ROOT_FOLDER = Path(__file__).parent
ORIGINAL = ROOT_FOLDER /  'foto.JPG'
NEW_IMAGE = ROOT_FOLDER / 'new.JPG'

pil_image = Image.open(ORIGINAL)

width, height = pil_image.size
# exif = pil_image.info['exif']

new_width = 640
new_height = round(height + new_width / width)

new_image = pil_image.resize((new_width, new_height))
new_image.save(
    NEW_IMAGE,
    optimize=True,
    quality=70,
    # exif=exif,
)