import os
from pathlib import Path
import qrcode

wifi_name = input("Enter Wi-Fi name (SSID): ").strip()
wifi_password = input("Enter Wi-Fi password: ").strip()

wifi_data = f"WIFI:S:{wifi_name};T:WPA;P:{wifi_password};;"
img = qrcode.make(wifi_data)
save_path = Path(__file__).parent / "QRcode" / f"{wifi_name}.png"
save_path.parent.mkdir(exist_ok=True)
img.save(save_path)

print(f"QR code generated and saved as '{save_path}'")
os.startfile(save_path)