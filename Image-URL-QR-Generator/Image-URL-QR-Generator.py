# Import necessary libraries
from pathlib import Path
from urllib.parse import urlsplit
import qrcode

# Get the URL from the user and remove surrounding whitespace
url = input("Enter a URL: ").strip()

# Parse the URL and add HTTPS if the protocol is missing
parsed_url = urlsplit(url if "://" in url else f"https://{url}")

# Validate the URL by checking whether it contains a website name
if not parsed_url.hostname:
    raise ValueError("Please enter a valid URL with a website name.")

# Extract the website name and remove the 'www.' prefix
website_name = parsed_url.hostname.removeprefix("www.")

# Generate a QR code from the URL
img = qrcode.make(url)

# Create the output path using the website name as the filename
output_path = Path(__file__).parent / "QRcode" / f"{website_name}.png"

# Create the output directory if it does not exist
output_path.parent.mkdir(exist_ok=True)

# Save the generated QR code image to the output path
img.save(output_path)

# Display a confirmation message showing where the QR code was saved
print(f"QR code generated and saved as '{output_path}'")
