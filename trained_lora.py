import os
import replicate
from dotenv import load_dotenv
from PIL import Image
import requests
from io import BytesIO

# Load environment variables
load_dotenv()

def generate_image(prompt):
    try:
        # Run the elias-face model
        output = replicate.run(
            "eliastsoukatos/elias-face:4be0e4995a2a8089907c1234c091e4f407b0496d35309982e9cbe2da074228c8",
            input={
                "prompt": prompt,
                "model": "dev",
                "lora_scale": 1,
                "num_outputs": 1,
                "aspect_ratio": "1:1",
                "output_format": "png",
                "guidance_scale": 3.5,
                "output_quality": 80,
                "num_inference_steps": 28
            }
        )
        
        print("API Response:", output)  # Debug print
        
        # Check if output is empty or None
        if not output:
            print("Error: Empty response from API")
            return

        # The output might be a list of URLs or a single URL string
        if isinstance(output, list):
            image_url = output[0]
        else:
            image_url = output

        print("Image URL:", image_url)  # Debug print

        # Check if the URL is valid
        if not image_url.startswith('http'):
            print(f"Error: Invalid URL returned by API: {image_url}")
            return

        # Download the image
        response = requests.get(image_url)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        img = Image.open(BytesIO(response.content))
        
        # Save the image
        img.save("generated_image.png")
        print("Image saved as 'generated_image.png'")
    
    except requests.exceptions.RequestException as e:
        print(f"Error downloading image: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    prompt = input("Enter your prompt for image generation: ")
    generate_image(prompt)

if __name__ == "__main__":
    main()