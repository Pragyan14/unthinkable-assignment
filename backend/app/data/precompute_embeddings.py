import json
import os
import sys
import logging
from typing import List, Dict

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Add parent directory to path to import app modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))

from app.utils.embedding import compute_embedding

def precompute_embeddings(products_file: str) -> bool:
    """Precompute embeddings for all products"""
    try:
        with open(products_file, "r") as f:
            products = json.load(f)
        
        logger.info(f"Starting to precompute embeddings for {len(products)} products...")
        
        for idx, product in enumerate(products):
            try:
                if "embedding" in product and product["embedding"] is not None:
                    logger.info(f"[{idx+1}/{len(products)}] Embedding already exists for {product['name']}, skipping...")
                    continue
                
                logger.info(f"[{idx+1}/{len(products)}] Computing embedding for {product['name']}...")
                embedding = compute_embedding(image_url=product["image_url"])
                
                if embedding:
                    product["embedding"] = embedding
                    logger.info(f"✓ Embedding computed for {product['name']}")
                else:
                    logger.warning(f"✗ Failed to compute embedding for {product['name']}")
            
            except Exception as e:
                logger.error(f"Error processing {product['name']}: {str(e)}")
                continue
        
        # Save products with embeddings
        with open(products_file, "w") as f:
            json.dump(products, f, indent=2)
        
        logger.info("✓ All embeddings precomputed and saved")
        return True
    
    except Exception as e:
        logger.error(f"Error precomputing embeddings: {str(e)}")
        return False

if __name__ == "__main__":
    products_file = os.path.join(os.path.dirname(__file__), "products.json")
    precompute_embeddings(products_file)