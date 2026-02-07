import os
import requests
from fastapi import HTTPException

# ==================================================
# Property API Service
# ==================================================

RAPIDAPI_HOST = "zillow-com1.p.rapidapi.com"
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")  # from environment variables


def get_property_details(address: str, citystatezip: str | None = None):
    """
    Fetch property details (bedrooms, baths, square footage, Zestimate, etc.)
    using RapidAPI's Zillow endpoint or fallback dummy data if not available.
    """
    if not RAPIDAPI_KEY:
        # fallback stub data if API key unavailable
        return {
            "address": address,
            "bedrooms": 3,
            "bathrooms": 2,
            "sqft": 1500,
            "zestimate": 245000,
            "year_built": 1988,
            "status": "Mock data (no API key configured)"
        }

    url = f"https://{RAPIDAPI_HOST}/propertyExtendedSearch"
    querystring = {"location": citystatezip or address}

    headers = {
        "x-rapidapi-host": RAPIDAPI_HOST,
        "x-rapidapi-key": RAPIDAPI_KEY,
    }

    try:
        response = requests.get(url, headers=headers, params=querystring, timeout=15)
        response.raise_for_status()
        data = response.json()

        if not data.get("props"):
            raise HTTPException(status_code=404, detail="No properties found for query.")

        property_data = data["props"][0]
        return {
            "address": property_data.get("address", address),
            "bedrooms": property_data.get("bedrooms"),
            "bathrooms": property_data.get("bathrooms"),
            "sqft": property_data.get("livingArea"),
            "zestimate": property_data.get("price"),
            "year_built": property_data.get("yearBuilt"),
            "status": "OK"
        }

    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error fetching property data: {e}")


def get_comparables(property_id: str):
    """
    Retrieves comparable home sales (comps) for a property by its Zillow ID.
    """
    if not RAPIDAPI_KEY:
        return {
            "property_id": property_id,
            "comparables": [
                {"address": "123 Maple Dr", "price": 230000, "sqft": 1450},
                {"address": "456 Oak St", "price": 250000, "sqft": 1600},
                {"address": "789 Pine Ln", "price": 240000, "sqft": 1500},
            ],
            "status": "Mock data (no API key configured)"
        }

    url = f"https://{RAPIDAPI_HOST}/propertyComps"
    querystring = {"zpid": property_id}
    headers = {
        "x-rapidapi-host": RAPIDAPI_HOST,
        "x-rapidapi-key": RAPIDAPI_KEY,
    }

    try:
        response = requests.get(url, headers=headers, params=querystring, timeout=15)
        response.raise_for_status()
        data = response.json()

        comps = [
            {
                "address": comp.get("address"),
                "price": comp.get("price", 0),
                "sqft": comp.get("livingArea", 0),
            }
            for comp in data.get("comparables", [])
        ]

        return {"property_id": property_id, "comparables": comps, "status": "OK"}

    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error fetching comparables: {e}")


def estimate_arv(property_data: dict) -> dict:
    """
    Estimate After‑Repair Value (ARV) and profit metrics using comps or fallback.
    """
    sqft = property_data.get("sqft", 1500)
    zestimate = property_data.get("zestimate", 250000)
    repair_cost = round(0.15 * zestimate, 2)
    arv = zestimate + repair_cost * 1.2
    profit_est = round(arv - (zestimate + repair_cost), 2)

    return {
        "address": property_data.get("address"),
        "bedrooms": property_data.get("bedrooms"),
        "bathrooms": property_data.get("bathrooms"),
        "sqft": sqft,
        "zestimate": zestimate,
        "estimated_repair_cost": repair_cost,
        "estimated_arv": arv,
        "potential_profit": profit_est,
    }