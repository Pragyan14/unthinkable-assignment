from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import logging
import os
from app.routes import products, search
from app.utils.error_handler import setup_error_handlers

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Visual Product Matcher API",
    description="Find visually similar products using image embeddings",
    version="1.0.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Setup error handlers
setup_error_handlers(app)

# Include routers
app.include_router(products.router, prefix="/api", tags=["products"])
app.include_router(search.router, prefix="/api", tags=["search"])

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "Visual Product Matcher API"}

@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Visual Product Matcher API", "version": "1.0.0"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    # debug = os.getenv("DEBUG", "False").lower() == "true"
    uvicorn.run(app, host="0.0.0.0", port=port)
