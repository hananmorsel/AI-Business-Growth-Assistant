
from utils.gemini_client import generate_image_prompt, generate_image_bytes

def generate_image(product,audience,style,custom):
    style_text = custom if style=="Custom" else style
    prompt = generate_image_prompt(product,audience,style_text)
    return generate_image_bytes(prompt)
