from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from app.utils.embedding import compute_embedding, find_similar_products
from app.utils.database import load_products
from app.models.product import SearchResponse, SimilarProduct
import logging
import io

logger = logging.getLogger(__name__)
router = APIRouter()

@router.post("/search")
async def search_similar_products(
    file: UploadFile = File(None),
    image_url: str = Form(None),
    min_similarity: float = Form(0.5),
    top_n: int = Form(10)
):
    """
    Search for similar products based on uploaded image or URL
    """
    try:
        if not file and not image_url:
            raise HTTPException(
                status_code=400,
                detail="Either file or image_url must be provided"
            )
        
        if min_similarity < 0 or min_similarity > 1:
            raise HTTPException(
                status_code=400,
                detail="min_similarity must be between 0 and 1"
            )
        
        if top_n < 1 or top_n > 100:
            raise HTTPException(
                status_code=400,
                detail="top_n must be between 1 and 100"
            )
        
        # Compute embedding for input image
        if file:
            image_data = await file.read()
            embedding = compute_embedding(image_data=image_data)
            query_image_url = None
        else:
            embedding = compute_embedding(image_url=image_url)
            query_image_url = image_url
        
        if embedding is None:
            raise HTTPException(
                status_code=400,
                detail="Failed to process image. Ensure it's a valid image format."
            )
        
        # Load products and find similar ones
        products = load_products()
        similar = find_similar_products(
            embedding=embedding,
            products=products,
            top_n=top_n,
            min_similarity=min_similarity
        )
        
        similar_products = [
            SimilarProduct(
                id=p["id"],
                name=p["name"],
                category=p["category"],
                image_url=p["image_url"],
                similarity_score=round(p["similarity_score"], 4),
                description=p.get("description")
            )
            for p in similar
        ]
        
        return SearchResponse(
            query_image_url=query_image_url,
            similar_products=similar_products,
            total_matches=len(similar_products)
        )
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error during search: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Search failed: {str(e)}")