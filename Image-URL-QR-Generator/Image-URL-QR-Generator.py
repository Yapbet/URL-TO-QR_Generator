from pathlib import Path
from urllib.parse import urlsplit
import qrcode

url = input("Enter a URL: ").strip()
parsed_url = urlsplit(url if "://" in url else f"https://{url}")
if not parsed_url.hostname:
    raise ValueError("Please enter a valid URL with a website name.")

website_name = parsed_url.hostname.removeprefix("www.")
img = qrcode.make(url)
output_path = Path(__file__).parent / "QRcode" / f"{website_name}.png"
output_path.parent.mkdir(exist_ok=True)
img.save(output_path)

print(f"QR code generated and saved as '{output_path}'")