#RBM-Meta_Analyze
import os
from PIL import Image
from PIL.ExifTags import TAGS
import piexif

def extract_metadata(image_path):
    try:
        image = Image.open(image_path)
        exif_data = image._getexif()
        print(".............................................................................")
        if not exif_data:
            print(f"No metadata found for file: {image_path}")
            print(".............................................................................")
            return

        print(f"Metadata for file: {image_path}")
        print(".............................................................................")

        for tagid in exif_data:
            tagname = TAGS.get(tagid, tagid)
            value = exif_data.get(tagid)
            print(f"{tagname:25}: {value}")

        print(".............................................................................")
    except Exception as e:
        print(f"Failed to extract metadata for file: {image_path}")
        print(e)

def main():
    file_path = input("Enter the file path to analyze: ").strip()
    
    if not os.path.isfile(file_path):
        print("The provided path is not a valid file.")
        return

    extract_metadata(file_path)

if __name__ == "__main__":
    main()