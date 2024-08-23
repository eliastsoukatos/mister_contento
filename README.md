# Flux Image Generator

This Python script generates images using the Flux model based on user prompts.

## Setup

1. Create a virtual environment:
   ```
   python -m venv venv
   ```

2. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root directory and add your Replicate API token:
   ```
   REPLICATE_API_TOKEN=your_api_token_here
   ```

## Usage

Run the script:
```
python main.py
```

Enter your prompt when prompted, and the script will generate an image based on your input. The generated image will be saved as 'generated_image.png' in the project directory.

## Note

Make sure to keep your API token confidential and do not share it publicly.
