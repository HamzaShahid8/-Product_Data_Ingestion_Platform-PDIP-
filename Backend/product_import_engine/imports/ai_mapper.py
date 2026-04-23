import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()


# =========================
# GEMINI CLIENT (NEW SDK)
# =========================
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


# =========================
# AI COLUMN MAPPING
# =========================
def get_ai_column_mapping(headers):

    try:
        prompt = f"""
You are an Excel column mapping assistant.

Map these headers:
{headers}

To system fields:
sku, title, price, stock, description, image_url, brand

Return ONLY valid JSON:

{{
    "sku": "",
    "title": "",
    "price": "",
    "stock": "",
    "description": "",
    "image_url": "",
    "brand": ""
}}
"""

        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )

        text = response.text.strip()

        return json.loads(text)

    except Exception as e:
        print("Gemini Error:", str(e))
        return None


# =========================
# FALLBACK
# =========================
def default_column_mapping():
    return {
        "sku": "sku",
        "title": "title",
        "price": "price",
        "stock": "stock",
        "description": "description",
        "image_url": "image_url",
        "brand": "brand"
    }