🌍 Ubuntu-Inspired Image Fetcher

The Wisdom of Ubuntu: "I am because we are"

This project is a Python tool that embraces the Ubuntu philosophy of community, respect, sharing, and practicality.
It connects to the wider web, fetches images respectfully, and organizes them for mindful use.

✨ Features

✅ Community → Connects to the global web to fetch shared images

✅ Respect → Handles errors gracefully without crashing

✅ Sharing → Saves all images into a common directory Fetched_Images/

✅ Practicality → Prevents duplicates and checks content type before saving

📂 Project Structure
Ubuntu_Requests/
│── ubuntu_fetcher.py   # Main Python script
│── Fetched_Images/     # Folder where images are stored (auto-created)
│── README.md           # Documentation (this file)

⚡ How It Works

Run the program:

python ubuntu_fetcher.py


Enter one or more image URLs (separated by commas):

Please enter one or more image URLs (separated by commas): 
https://example.com/ubuntu.jpg, https://example.com/logo.png


The program will:

Fetch the image(s) from the internet

Verify that the content is actually an image

Save them into Fetched_Images/

Skip duplicates politely

🖥️ Example Output
🌍 Welcome to the Ubuntu Image Fetcher
A tool for mindfully collecting images from the web

Please enter one or more image URLs (separated by commas): https://example.com/ubuntu.jpg

✓ Successfully fetched: ubuntu.jpg
✓ Image saved to Fetched_Images/ubuntu.jpg

🤝 Connection strengthened. Community enriched.

🛠️ Requirements

Python 3.x

Libraries:

requests (install via pip install requests)

📖 Ubuntu Principles in Action

Community: Fetching images shared by people worldwide.

Respect: Gracefully handling broken links, non-image content, and errors.

Sharing: Organizing all images in a central folder for later use.

Practicality: Providing a real tool that solves a real need.

"A person is a person through other persons." – Ubuntu Philosophy

🏆 Challenge Questions & Solutions
1️⃣ Multiple URLs at Once

✔ Implemented: User can input several URLs separated by commas.
The script loops through each URL and downloads them one by one.

2️⃣ Precautions for Downloading from Unknown Sources

✔ Implemented:

Uses a timeout (10 seconds) to avoid hanging requests

Checks Content-Type header to ensure the file is an image

Graceful handling of unsafe or invalid URLs

3️⃣ Preventing Duplicate Downloads

✔ Implemented:

If a file already exists in Fetched_Images/, the script skips it

Avoids wasting bandwidth and storage space

4️⃣ Checking Important HTTP Headers

✔ Implemented:

Content-Type is validated (must start with image/)

Content-Length (if provided) helps ensure response is not empty or suspicious

🚀 Future Improvements

Logging all downloads (success/failure) into a log.txt file

Support for downloading images from a text file list

Option to rename or auto-tag images with timestamps

👨‍💻 Author

Developed with ❤️ and Ubuntu spirit by [Your Name]