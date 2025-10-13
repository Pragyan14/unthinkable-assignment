from pydantic import BaseModel
from typing import List, Optional

class ProductBase(BaseModel):
    name: str
    category: str
    image_url: str
    description: Optional[str] = None

class Product(ProductBase):
    id: int
    embedding: Optional[List[float]] = None

class SimilarProduct(BaseModel):
    id: int
    name: str
    category: str
    image_url: str
    similarity_score: float
    description: Optional[str] = None

class SearchRequest(BaseModel):
    min_similarity: float = 0.5
    top_n: int = 10

class SearchResponse(BaseModel):
    query_image_url: Optional[str] = None
    similar_products: List[SimilarProduct]
    total_matches: int