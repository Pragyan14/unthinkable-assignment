import json
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

SAMPLE_PRODUCTS = [
    {"name": "Wireless Headphones", "category": "Electronics", "image_url": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400"},
    {"name": "Running Shoes", "category": "Footwear", "image_url": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400"},
    {"name": "Coffee Maker", "category": "Appliances", "image_url": "https://images.unsplash.com/photo-1608354580875-30bd4168b351?w=400"},
    {"name": "Backpack", "category": "Bags", "image_url": "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=400"},
    {"name": "Desk Lamp", "category": "Lighting", "image_url": "https://images.unsplash.com/photo-1621447980929-6638614633c8?w=400"},
    {"name": "Water Bottle", "category": "Hydration", "image_url": "https://images.unsplash.com/photo-1602143407151-7111542de6e8?w=400"},
    {"name": "Keyboard", "category": "Electronics", "image_url": "https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=400"},
    {"name": "Mouse", "category": "Electronics", "image_url": "https://images.unsplash.com/photo-1527814050087-3793815479db?w=400"},
    {"name": "Monitor", "category": "Electronics", "image_url": "https://images.unsplash.com/photo-1588200908342-23b585c03e26?w=400"},
    {"name": "Webcam", "category": "Electronics", "image_url": "https://images.unsplash.com/photo-1623949556303-b0d17d198863?w=400"},
    {"name": "Phone Stand", "category": "Accessories", "image_url": "https://images.unsplash.com/photo-1617975316514-69cd7e16c2a4?w=400"},
    {"name": "USB Hub", "category": "Accessories", "image_url": "https://images.unsplash.com/photo-1616578273461-3a99ce422de6?w=400"},
    {"name": "External SSD", "category": "Storage", "image_url": "https://plus.unsplash.com/premium_photo-1721133260774-84f57d69cb82?w=400"},
    {"name": "Portable Charger", "category": "Electronics", "image_url": "https://images.unsplash.com/photo-1609091839311-d5365f9ff1c5?w=400"},
    {"name": "HDMI Cable", "category": "Cables", "image_url": "https://images.unsplash.com/photo-1756576357688-c637013d3483?w=400"},
    {"name": "Extension Cord", "category": "Accessories", "image_url": "https://images.unsplash.com/photo-1650501386688-41f6d0251875?w=400"},
    {"name": "Router", "category": "Electronics", "image_url": "https://images.unsplash.com/photo-1606904825846-647eb07f5be2?w=400"},
    {"name": "Gaming Chair", "category": "Accessories", "image_url": "https://images.unsplash.com/photo-1670946839270-cc4febd43b09?w=400"},
    {"name": "Charger", "category": "Accessories", "image_url": "https://images.unsplash.com/photo-1583863788434-e58a36330cf0?w=400"},
    {"name": "Phone Case", "category": "Accessories", "image_url": "https://images.unsplash.com/photo-1623393945964-8f5d573f9358?w=400"},
    {"name": "Gaming Mouse", "category": "Gaming", "image_url": "https://images.unsplash.com/photo-1527814050087-3793815479db?w=400"},
    {"name": "Gaming Keyboard", "category": "Gaming", "image_url": "https://images.unsplash.com/photo-1637243218672-d338945efdf7?w=400"},
    {"name": "Gaming Headset", "category": "Gaming", "image_url": "https://images.unsplash.com/photo-1710265029735-434f63c672c4?w=400"},
    {"name": "Desk Organizer", "category": "Office", "image_url": "https://images.unsplash.com/photo-1644463589256-02679b9c0767?w=400"},
    {"name": "Wireless Charger", "category": "Electronics", "image_url": "https://images.unsplash.com/photo-1591290619618-904f6dd935e3?w=400"},
    {"name": "Bluetooth Speaker", "category": "Audio", "image_url": "https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=400"},
    {"name": "Smart Watch", "category": "Wearables", "image_url": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400"},
    {"name": "Fitness Tracker", "category": "Wearables", "image_url": "https://images.unsplash.com/photo-1575311373937-040b8e1fd5b6?w=400"},
    {"name": "Camera", "category": "Photography", "image_url": "https://images.unsplash.com/photo-1502920917128-1aa500764cbd?w=400"},
    {"name": "Microphone", "category": "Audio", "image_url": "https://images.unsplash.com/photo-1521424159246-e4a66f267e4b?w=400"},
    {"name": "Tripod", "category": "Photography", "image_url": "https://images.unsplash.com/photo-1657741164019-98bd2bf3fc45?w=400"},
    {"name": "Ring Light", "category": "Lighting", "image_url": "https://images.unsplash.com/photo-1673196649671-eb09066ad6c1?w=400"},
    {"name": "Studio Light", "category": "Lighting", "image_url": "https://images.unsplash.com/photo-1595406236320-a9aa2a54a00e?w=400"},
    {"name": "Green Screen", "category": "Photography", "image_url": "https://plus.unsplash.com/premium_photo-1711061959382-0de7a4bddccf?w=400"},
    {"name": "Printer", "category": "Accessories", "image_url": "https://images.unsplash.com/photo-1612815154858-60aa4c59eaa6?w=400"},
    {"name": "Table Clock", "category": "Accessories", "image_url": "https://images.unsplash.com/photo-1634375272898-a63e01c49ca7?w=400"},
    {"name": "Laptop Stand", "category": "Accessories", "image_url": "https://images.unsplash.com/photo-1629317480872-45e07211ffd4?w=400"},
    {"name": "Webcam Ring Light", "category": "Lighting", "image_url": "https://images.unsplash.com/photo-1600298881974-6be191ceeda1?w=400"},
    {"name": "GPU", "category": "Gaming", "image_url": "https://images.unsplash.com/photo-1624701928517-44c8ac49d93c?w=400"},
    {"name": "Mousepad", "category": "Accessories", "image_url": "https://images.unsplash.com/photo-1650566301820-ded93a1bb635?w=400"},
    {"name": "Laptop Sleeve", "category": "Bags", "image_url": "https://images.unsplash.com/photo-1611461527944-1a718332613b?w=400"},
    {"name": "Laptop Backpack", "category": "Bags", "image_url": "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=400"},
    {"name": "Earphone", "category": "Accessories", "image_url": "https://plus.unsplash.com/premium_photo-1668418188837-d40b734ed6d2?w=400"},
    {"name": "Gaming Controller", "category": "Accessories", "image_url": "https://images.unsplash.com/flagged/photo-1580234820596-0876d136e6d5?w=400"},
    {"name": "Earbuds", "category": "Accessories", "image_url": "https://images.unsplash.com/photo-1630331384146-a8b2a79a9558?w=400"},
    {"name": "Watch", "category": "Accessories", "image_url": "https://images.unsplash.com/photo-1549972574-8e3e1ed6a347?w=400"},
    {"name": "Audio Mixer", "category": "Audio", "image_url": "https://images.unsplash.com/photo-1679931942077-0be253938a30?w=400"},
    {"name": "Amplifiers", "category": "Audio", "image_url": "https://images.unsplash.com/photo-1646072609959-0893c1a841d0?w=400"},
    {"name": "Lamp", "category": "Accessories", "image_url": "https://images.unsplash.com/photo-1580130281320-0ef0754f2bf7?w=400"},
    {"name": "Tablet", "category": "Accessories", "image_url": "https://images.unsplash.com/photo-1636614178501-e03f25a87516?w=400"},
]

def generate_sample_data(output_file: str) -> bool:
    """Generate sample product data"""
    try:
        products = []
        for idx, product_data in enumerate(SAMPLE_PRODUCTS, 1):
            product = {
                "id": idx,
                "name": product_data["name"],
                "category": product_data["category"],
                "image_url": product_data["image_url"],
                "description": f"High-quality {product_data['name'].lower()} for professionals and enthusiasts",
                "embedding": None  # Will be computed by precompute_embeddings.py
            }
            products.append(product)
        
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        with open(output_file, "w") as f:
            json.dump(products, f, indent=2)
        
        logger.info(f"✓ Generated {len(products)} sample products at {output_file}")
        return True
    
    except Exception as e:
        logger.error(f"Error generating sample data: {str(e)}")
        return False

if __name__ == "__main__":
    output_file = os.path.join(os.path.dirname(__file__), "products.json")
    generate_sample_data(output_file)