# Visual Product Matcher

A production-ready web application that helps users find visually similar products based on uploaded images using AI-powered visual embeddings (CLIP).

## ✨ Features

- **Image Upload**: Drag & drop or click to upload images
- **URL Support**: Paste image URLs to search instantly
- **AI-Powered Search**: Uses OpenAI CLIP for visual embeddings
- **Real-time Results**: Instant similarity matching with 50+ products
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile
- **Interactive Filtering**: Adjustable similarity threshold and result limits
- **Fast Performance**: Precomputed embeddings for quick searches
- **Production Ready**: Clean code, error handling, logging, CORS setup

## 🏗️ Architecture

```
visual-product-matcher/
├── backend/                    # FastAPI Python Backend
│   ├── main.py                # Application entry point
│   ├── requirements.txt        # Python dependencies
│   ├── app/
│   │   ├── models/            # Pydantic models
│   │   ├── routes/            # API endpoints (products, search)
│   │   ├── utils/             # Utilities (embedding, database, error handling)
│   │   └── data/
│   │       ├── products.json          # Product database (generated)
│   │       ├── generate_sample_data.py
│   │       ├── precompute_embeddings.py
│   │       ├── clear_data.py
│   │       └── reset_all.py
│   └── README.md
│
├── frontend/                  # Next.js React Frontend
│   ├── package.json
│   ├── tsconfig.json
│   ├── tailwind.config.ts
│   ├── next.config.js
│   ├── .env.local
│   ├── app/
│   │   ├── page.tsx           # Main page
│   │   ├── layout.tsx         # Root layout
│   │   ├── components/        # React components (UploadBox, ProductGrid, etc.)
│   │   ├── hooks/             # Custom hooks (useSearch)
│   │   └── styles/            # Global styles
│   └── README.md
│
└── docs/
    ├── architecture.md        # Technical deep dive
    ├── setup_guide.md         # Deployment instructions
    └── approach_summary.md    # Design decisions (200 words)
```

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Frontend** | Next.js 14 | Server-rendered React app |
| **Frontend Styling** | Tailwind CSS | Utility-first CSS |
| **Frontend HTTP** | Axios | API communication |
| **Backend** | FastAPI | Python web framework |
| **ML Model** | CLIP (HuggingFace) | Image embeddings |
| **Similarity** | Scikit-learn | Cosine similarity computation |
| **Database** | JSON | Product storage |

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Node.js 18+
- Git

### Local Development Setup

#### 1. Clone Repository
```bash
git clone <your-repo-url>
cd visual-product-matcher
```

#### 2. Backend Setup
```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Generate sample product data
python app/data/generate_sample_data.py

# Precompute embeddings (takes 2-3 minutes)
python app/data/precompute_embeddings.py

# Run backend server
python main.py
```

Backend will be available at: **http://localhost:8000**

API Documentation: **http://localhost:8000/docs**

#### 3. Frontend Setup (in new terminal)
```bash
cd frontend

# Install dependencies
npm install

# Run development server
npm run dev
```

Frontend will be available at: **http://localhost:3000**

### Testing the Application

1. Open http://localhost:3000 in your browser
2. Upload an image or paste an image URL
3. Adjust similarity threshold and result limit if desired
4. View similar products with similarity scores

## 📊 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/health` | Health check |
| `GET` | `/api/products` | List all products (paginated) |
| `GET` | `/api/products/{id}` | Get specific product |
| `POST` | `/api/search` | Search for similar products |

## 🗄️ Data Management

### Generate Fresh Data
```bash
cd backend

# Generate sample products
python app/data/generate_sample_data.py

# Precompute embeddings
python app/data/precompute_embeddings.py
```

### Clear Old Embeddings
```bash
cd backend
python app/data/clear_data.py
```

### Complete Reset (Delete + Regenerate)
```bash
cd backend
python app/data/reset_all.py
```

### Add Custom Products

Edit `backend/app/data/generate_sample_data.py` and add to `SAMPLE_PRODUCTS` list:

```python
SAMPLE_PRODUCTS = [
    {
        "name": "Your Product",
        "category": "Category",
        "image_url": "https://your-image-url.com/image.jpg"
    },
    # ... more products
]
```

Then regenerate data:
```bash
python app/data/reset_all.py
```

## 📦 Build for Production

### Frontend Build
```bash
cd frontend
npm run build
npm start
```

### Backend Build
```bash
cd backend
pip install -r requirements.txt
python main.py
```

## 🔧 Environment Variables

### Frontend (.env.local)
```
NEXT_PUBLIC_API_URL=http://localhost:8000
```

### Backend (optional .env)
```
PORT=8000
DEBUG=false
```
