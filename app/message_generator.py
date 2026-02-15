
from utils.gemini_client import generate_text

def generate_message(product,audience,tone,platform):
    prompt=f"Create a {tone} marketing message for {product} targeting {audience} on {platform}."
    return generate_text(prompt)
