
import os, requests, base64

API_KEY=os.getenv("GEMINI_API_KEY")
BASE="https://generativelanguage.googleapis.com/v1beta/models"

def generate_text(prompt, model="gemini-1.5-flash"):
    url=f"{BASE}/{model}:generateContent?key={API_KEY}"
    r=requests.post(url,json={"contents":[{"parts":[{"text":prompt}]}]})
    r.raise_for_status()
    return r.json()["candidates"][0]["content"]["parts"][0]["text"]

def generate_image_prompt(product,audience,style):
    return f"Generate a marketing image for {product}, audience {audience}, style {style}."

def generate_image_bytes(prompt, model="gemini-1.5-flash"):
    url=f"{BASE}/{model}:generateContent?key={API_KEY}"
    r=requests.post(url,json={"contents":[{"parts":[{"text":prompt}]}]})
    r.raise_for_status()
    img=r.json()["candidates"][0]["content"]["parts"][0].get("inline_data",{}).get("data",None)
    if not img:
        raise Exception("No image returned.")
    return base64.b64decode(img)
