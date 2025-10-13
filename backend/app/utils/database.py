import json
import os
import logging
from typing import List, Dict

logger = logging.getLogger(__name__)

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
PRODUCTS_FILE = os.path.join(DATA_DIR, "products.json")

def load_products() -> List[Dict]:
    """Load products from JSON file"""
    try:
        if not os.path.exists(PRODUCTS_FILE):
            logger.warning(f"Products file not found at {PRODUCTS_FILE}")
            return []
        
        with open(PRODUCTS_FILE, "r") as f:
            products = json.load(f)
        
        logger.info(f"Loaded {len(products)} products")
        return products
    
    except Exception as e:
        logger.error(f"Error loading products: {str(e)}")
        return []

def save_products(products: List[Dict]) -> bool:
    """Save products to JSON file"""
    try:
        os.makedirs(DATA_DIR, exist_ok=True)
        
        with open(PRODUCTS_FILE, "w") as f:
            json.dump(products, f, indent=2)
        
        logger.info(f"Saved {len(products)} products")
        return True
    
    except Exception as e:
        logger.error(f"Error saving products: {str(e)}")
        return False