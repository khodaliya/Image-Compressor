from PIL import Image
import os

# def compress_webp(input_path = 'images/', output_path = 'compress_image/', quality=58):
#     try:
#         image = Image.open(input_path)
#         output_folder = os.path.dirname(output_path)

#         if not os.path.exists(output_folder):
#             os.makedirs(output_folder)

#         image.save(output_path, 'webp', quality=quality)
#         print(f"Image compressed and saved as {output_path}")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# if __name__ == "__main__":
#     input_image_path = "images/"  # Change this to the path of your input image
#     output_image_path = "compress_image/"  # Change this to the desired output path

#     compress_webp(input_image_path, output_image_path)

def compress_existing_webp(input_path, output_path, quality=45):
    try:
        image = Image.open(input_path)
        if image.format != 'WEBP':
            print(f"Input image {input_path} is not in WebP format. Skipping.")
            return
        
        image.save(output_path, 'webp', quality=quality)
        print(f"Image compressed and saved as {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_folder = "images/"  # Change this to the path of your input folder containing WebP images
    output_folder = "compress_image/"  # Change this to the desired output folder

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".webp"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            compress_existing_webp(input_path, output_path)