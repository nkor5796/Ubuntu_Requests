"""
Ubuntu-Inspired Image Fetcher
--------------------------------
The Wisdom of Ubuntu: "I am because we are"

This program embraces Ubuntu principles by:
🌍 Community: Connecting to the global web to fetch shared images
🤝 Respect: Handling errors gracefully without crashing
📂 Sharing: Organizing fetched images in a common folder
🛠️ Practicality: A simple, useful tool for mindful image collection

Author: Your Name
Repository: Ubuntu_Requests
"""

import requests
import os
from urllib.parse import urlparse

# Directory to store images
SAVE_DIR = "Fetched_Images"


def create_directory():
    """Create the Fetched_Images directory if it does not exist."""
    os.makedirs(SAVE_DIR, exist_ok=True)


def get_filename_from_url(url):
    """
    Extract the filename from the URL.
    If none is found, return a default name.
    """
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)

    # Fallback if no filename is present in URL
    if not filename:
        filename = "downloaded_image.jpg"

    return filename


def fetch_image(url):
    """
    Download an image from the given URL and save it to Fetched_Images.
    Includes error handling and checks that content is an image.
    """
    try:
        # Fetch the image from the internet
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise error for bad status codes

        # Check the Content-Type header to ensure it's an image
        if "image" not in response.headers.get("Content-Type", ""):
            print(f"✗ Skipped: {url} (Not an image file)")
            return

        # Extract or generate a filename
        filename = get_filename_from_url(url)
        filepath = os.path.join(SAVE_DIR, filename)

        # Prevent overwriting duplicates
        if os.path.exists(filepath):
            print(f"⚠ Skipped duplicate: {filename}")
            return

        # Save the image in binary mode
        with open(filepath, "wb") as f:
            f.write(response.content)

        # Success messages
        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ An unexpected error occurred: {e}")


def main():
    """Main entry point for the Ubuntu Image Fetcher."""
    print("🌍 Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Create storage directory
    create_directory()

    # Ask for one or multiple URLs
    urls = input("Please enter one or more image URLs (separated by commas): ").split(",")
    urls = [u.strip() for u in urls if u.strip()]  # Clean and filter input

    if not urls:
        print("✗ No valid URLs provided. Please try again.")
        return

    # Process each URL
    for url in urls:
        fetch_image(url)

    print("\n🤝 Connection strengthened. Community enriched.")


if __name__ == "__main__":
    main()
