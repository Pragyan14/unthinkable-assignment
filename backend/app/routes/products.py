from fastapi import APIRouter, HTTPException
from app.utils.database import load_products
import logging

logger = logging.getLogger(__name__)
router = APIRouter()

@router.get("/products")
async def get_products(skip: int = 0, limit: int = 50):
    """Get list of all products"""
    try:
        products = load_products()
        total = len(products)
        paginated = products[skip:skip + limit]
        
        # Remove embeddings from response for efficiency
        for product in paginated:
            product.pop("embedding", None)
        
        return {
            "products": paginated,
            "total": total,
            "skip": skip,
            "limit": limit
        }
    except Exception as e:
        logger.error(f"Error fetching products: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/products/{product_id}")
async def get_product(product_id: int):
    """Get a specific product by ID"""
    try:
        products = load_products()
        product = next((p for p in products if p["id"] == product_id), None)
        
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        
        # Remove embedding from response
        product.pop("embedding", None)
        return product
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error fetching product: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))