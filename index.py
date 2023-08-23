import sys
from PIL import Image
import os

# Three images will be created from this image.
# The first image will be a 128x128 thumbnail
# The second will be medium quality image
# The third will be a high quality image
THUMBNAIL_WIDTH = 168
MEDIUM_SIZE_WIDTH = 900
HIGH_SIZE_WIDTH = 1800

# Compress image to reduce size
COMPRESSION_QUALITY = 80


def resize_image(image, width):
    aspect_ratio = image.width / image.height
    height = int(width / aspect_ratio)
    return image.resize((width, height))


def generate_scaled_image(original_image):
    thumbnail_image = resize_image(original_image, THUMBNAIL_WIDTH)
    medium_size_image = resize_image(original_image, MEDIUM_SIZE_WIDTH)
    high_size_image = resize_image(original_image, HIGH_SIZE_WIDTH)
    return thumbnail_image, medium_size_image, high_size_image


def main():
    if len(sys.argv) < 3:
        print("Usage: python script.py image_name input_image storage_path")
        return

    image_name = sys.argv[1]
    input_image = sys.argv[2]
    storage_path = sys.argv[3]

    if not os.path.exists(storage_path):
        os.makedirs(storage_path + '/thumbnail')
        os.makedirs(storage_path + '/medium')
        os.makedirs(storage_path + '/high')

    try:
        original_image = Image.open(input_image)
    except Exception as e:
        print("Error opening the input image:", e)
        return

    thumbnail_image_path = os.path.join(
        storage_path, 'thumbnail', image_name + '.jpg')
    medium_size_image_path = os.path.join(
        storage_path, 'medium', image_name + '.jpg')
    high_size_image_path = os.path.join(
        storage_path, 'high', image_name + '.jpg')

    thumbnail_image, medium_size_image, high_size_image = generate_scaled_image(
        original_image)

    try:
        thumbnail_image.save(thumbnail_image_path,
                             optimize=True, quality=COMPRESSION_QUALITY)
        medium_size_image.save(medium_size_image_path,
                               optimize=True, quality=COMPRESSION_QUALITY)
        high_size_image.save(high_size_image_path,
                             optimize=True, quality=COMPRESSION_QUALITY)
        print(image_name + '.jpg', "saved successfully")
    except Exception as e:
        print("Error saving images:", e)


if __name__ == "__main__":
    main()
