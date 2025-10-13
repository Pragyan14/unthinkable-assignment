import numpy as np
from PIL import Image
import io
import requests
from typing import List, Optional, Dict
import logging
from sklearn.metrics.pairwise import cosine_similarity

logger = logging.getLogger(__name__)

# Load CLIP model lazily
_model = None
_processor = None

def get_model_and_processor():
    """Lazy load CLIP model and processor"""
    global _model, _processor
    if _model is None:
        try:
            from transformers import CLIPProcessor, CLIPModel
            _model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
            _processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
            logger.info("CLIP model loaded successfully")
        except Exception as e:
            logger.error(f"Failed to load CLIP model: {str(e)}")
            raise
    return _model, _processor

def load_image(image_data: bytes = None, image_url: str = None) -> Optional[Image.Image]:
    """Load image from bytes or URL"""
    try:
        if image_data:
            return Image.open(io.BytesIO(image_data)).convert("RGB")
        elif image_url:
            response = requests.get(image_url, timeout=10)
            response.raise_for_status()
            return Image.open(io.BytesIO(response.content)).convert("RGB")
    except Exception as e:
        logger.error(f"Failed to load image: {str(e)}")
    return None

def compute_embedding(image_data: bytes = None, image_url: str = None) -> Optional[List[float]]:
    """Compute CLIP embedding for an image"""
    try:
        image = load_image(image_data=image_data, image_url=image_url)
        if image is None:
            return None
        
        model, processor = get_model_and_processor()
        
        inputs = processor(images=image, return_tensors="pt")
        import torch
        with torch.no_grad():
            image_features = model.get_image_features(**inputs)
        
        # Normalize and convert to list
        embedding = image_features[0].cpu().numpy()
        embedding = embedding / np.linalg.norm(embedding)
        return embedding.tolist()
    
    except Exception as e:
        logger.error(f"Error computing embedding: {str(e)}")
        return None

def find_similar_products(
    embedding: List[float],
    products: List[Dict],
    top_n: int = 10,
    min_similarity: float = 0.5
) -> List[Dict]:
    """Find similar products using cosine similarity"""
    try:
        embedding_array = np.array(embedding).reshape(1, -1)
        
        similarities = []
        for product in products:
            if "embedding" not in product or product["embedding"] is None:
                continue
            
            product_embedding = np.array(product["embedding"]).reshape(1, -1)
            similarity = cosine_similarity(embedding_array, product_embedding)[0][0]
            
            if similarity >= min_similarity:
                similarities.append({
                    **product,
                    "similarity_score": float(similarity)
                })
        
        # Sort by similarity score and return top_n
        similarities.sort(key=lambda x: x["similarity_score"], reverse=True)
        return similarities[:top_n]
    
    except Exception as e:
        logger.error(f"Error finding similar products: {str(e)}")
        return []