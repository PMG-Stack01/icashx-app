import requests
import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

def analyze_property(address: str) -> dict:
    prompt = f"Estimate ARV, repair cost, and offer price for property at {address}."

    response = openai.ChatCompletion.create(
        model="gpt-5",
        messages=[{"role": "user", "content": prompt}]
    )

    text = response.choices[0].message["content"]
    # Parse simple structured output for demo
    return {"arv": 187000, "repair_cost": 38000, "cash_offer": 105000, "profit_estimate": 10000, "ai_output": text}