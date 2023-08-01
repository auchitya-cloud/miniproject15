import cv2
import os

# Prepare the input and output directories
input_dir = '/Users/auchitya/VS pro/summer school/rand100'
output_dir = '/Users/auchitya/VS pro/summer school/rand200'
os.makedirs(output_dir, exist_ok=True)

def convert_to_grayscale(input_image_path, output_image_path):
    # Read the image
    image = cv2.imread(input_image_path)

    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Save the grayscale image
    cv2.imwrite(output_image_path, gray_image)

# List all files in the input directory
input_files = os.listdir(input_dir)

# Process the first 10 images and convert to grayscale
num_images_to_convert = 100
for i, filename in enumerate(input_files):
    if i >= num_images_to_convert:
        break

    input_image_path = os.path.join(input_dir, filename)
    output_image_path = os.path.join(output_dir, filename)

    convert_to_grayscale(input_image_path, output_image_path)
