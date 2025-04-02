# generate_gallery.py
import os
import base64
from datetime import datetime

PLOTS_DIR = "plots"
OUTPUT_FILE = "index.html"

def image_to_base64(path: str) -> str:
  with open(path, "rb") as image_file:
    encoded = base64.b64encode(image_file.read()).decode("utf-8")
    return f"data:image/png;base64,{encoded}"

def generate_html():
  images = sorted(f for f in os.listdir(PLOTS_DIR) if f.endswith(".png"))

  html = [
    "<!DOCTYPE html>",
    "<html>",
    "<head><meta charset='utf-8'><title>Plots Gallery</title></head>",
    "<body style='font-family: sans-serif;'>",
    "<h1>Plots Gallery</h1>",
  ]

  for img in images:
    path = os.path.join(PLOTS_DIR, img)
    src = image_to_base64(path)

    try:
      parts = img.replace(".png", "").split("_")
      ts = parts[0]
      ts_str = datetime.strptime(ts, "%Y%m%d").strftime("%Y-%m-%d")
      label = ts_str + " – " + " ".join(parts[1:-1]).capitalize()
    except:
      label = img.replace("_", " ").replace(".png", "")

    html += [
      f"<div style='margin-bottom:40px'>",
      f"<h3>{label}</h3>",
      f"<img src='{src}' style='max-width:100%; height:auto; border:1px solid #ccc;'/>",
      "</div>"
    ]

  html.append("</body></html>")

  with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("\n".join(html))

  print(f"Base64 HTML gallery generated: {OUTPUT_FILE}")

if __name__ == "__main__":
  generate_html()