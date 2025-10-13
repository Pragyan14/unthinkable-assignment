'use client'

import Image from 'next/image'

interface Product {
  id: number
  name: string
  category: string
  image_url: string
  similarity_score: number
  description?: string
}

interface ProductGridProps {
  products: Product[]
}

export default function ProductGrid({ products }: ProductGridProps) {
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
      {products.map((product) => (
        <div
          key={product.id}
          className="bg-slate-800 rounded-lg overflow-hidden border border-slate-700 hover:border-slate-600 transition group"
        >
          {/* Image Container */}
          <div className="relative h-64 bg-slate-900 overflow-hidden">
            <img
              src={product.image_url}
              alt={product.name}
              className="w-full h-full object-cover group-hover:scale-105 transition duration-300"
            />
            {/* Similarity Score Badge */}
            <div className="absolute top-3 right-3 bg-gradient-to-r from-green-500 to-emerald-600 px-3 py-1 rounded-full text-white font-bold text-sm">
              {(product.similarity_score * 100).toFixed(0)}%
            </div>
          </div>

          {/* Content */}
          <div className="p-4">
            <div className="flex items-start justify-between mb-2">
              <div className="flex-1">
                <h3 className="text-lg font-bold text-white mb-1">{product.name}</h3>
                <span className="inline-block px-2 py-1 bg-slate-700 text-slate-200 text-xs rounded font-medium">
                  {product.category}
                </span>
              </div>
            </div>

            {product.description && (
              <p className="text-slate-400 text-sm mt-3 line-clamp-2">
                {product.description}
              </p>
            )}

            {/* Score Bar */}
            <div className="mt-4">
              <div className="flex justify-between items-center mb-2">
                <span className="text-xs text-slate-400">Similarity</span>
                <span className="text-xs font-semibold text-slate-300">
                  {(product.similarity_score * 100).toFixed(1)}%
                </span>
              </div>
              <div className="w-full bg-slate-700 rounded-full h-2 overflow-hidden">
                <div
                  className="bg-gradient-to-r from-blue-500 to-cyan-500 h-full rounded-full transition-all duration-500"
                  style={{ width: `${product.similarity_score * 100}%` }}
                />
              </div>
            </div>
          </div>
        </div>
      ))}
    </div>
  )
}