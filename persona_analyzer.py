
from utils.gemini_client import generate_text

def build_persona(product,audience):
    prompt=f"Create a detailed marketing persona for a product: {product} targeting {audience}."
    return generate_text(prompt)
