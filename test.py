import langchain
print(langchain.__version__)



import os
from PIL import Image

def convert_png_to_jpg(source_dir):
    # Create "JPG FORMAT" directory if it doesn't exist
    output_dir = os.path.join(source_dir, "JPG FORMAT")
    os.makedirs(output_dir, exist_ok=True)
    
    # Loop through all files in the source directory
    for filename in os.listdir(source_dir):
        if filename.lower().endswith('.png'):
            # Open the PNG image
            png_path = os.path.join(source_dir, filename)
            img = Image.open(png_path)
            
            # Convert to RGB (JPG doesn't support transparency)
            rgb_img = img.convert('RGB')
            
            # Define the output JPG path (same name but .jpg extension)
            jpg_filename = os.path.splitext(filename)[0] + '.jpg'
            jpg_path = os.path.join(output_dir, jpg_filename)
            
            # Save as JPG
            rgb_img.save(jpg_path, 'JPEG', quality=95)  # Adjust quality as needed (1-100)
            print(f"Converted: {filename} → {jpg_filename}")
    
    print("\nConversion complete! Check the 'JPG FORMAT' folder.")

# Example usage
source_directory = "/Users/shoeb/Desktop/tmp SS/runnable_part2"
convert_png_to_jpg(source_directory)