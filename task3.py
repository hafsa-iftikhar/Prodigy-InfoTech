import os
from PIL import Image

def load_image(image_path):
    # Check if the provided path is a file
    if not os.path.isfile(image_path):
        raise ValueError(f"The path {image_path} is not a file. Please provide a valid image file path.")
    return Image.open(image_path)

def main():
    image_path = input("Enter the path to the image: ")

    try:
        # Load the image
        image = load_image(image_path)
        print(f"Successfully loaded the image: {image_path}")
        # Perform image processing or encryption/decryption here

    except ValueError as ve:
        print(ve)
    except PermissionError as pe:
        print(f"Permission error: {pe}. Make sure the file is accessible.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
