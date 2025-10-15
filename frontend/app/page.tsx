'use client'

import { useState } from 'react'
import UploadBox from './components/UploadBox'
import ProductGrid from './components/ProductGrid'
import SimilarityFilter from './components/SimilarityFilter'
import LoadingSpinner from './components/LoadingSpinner'
import Toast from './components/Toast'
import { useSearch } from './hooks/useSearch'

export default function Home() {
  const [minSimilarity, setMinSimilarity] = useState(0.7)
  const [topN, setTopN] = useState(5)
  const [toastMessage, setToastMessage] = useState('')
  const [toastType, setToastType] = useState<'success' | 'error'>('success')
  const [showToast, setShowToast] = useState(false)

  const { isLoading, queryImage, results, error, search } = useSearch()

  const handleSearch = async (imageData: string | File, isUrl: boolean) => {
    try {
      const success = await search(imageData, isUrl, minSimilarity, topN)

      if (success) {
        setToastMessage(`Found ${results.length} similar products!`)
        setToastType('success')
        setShowToast(true)
        setTimeout(() => setShowToast(false), 3000)
      }
    } catch (err) {
      setToastMessage(error || 'An error occurred during search')
      setToastType('error')
      setShowToast(true)
      setTimeout(() => setShowToast(false), 3000)
    }
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900">
      {/* Header */}
      <header className="border-b border-slate-700 backdrop-blur-md bg-slate-900/50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-3">
              <div>
                <h1 className="text-3xl font-bold text-white">Visual Product Matcher</h1>
                <p className="text-sm text-slate-300 mt-1">Find visually similar products using AI</p>
              </div>
            </div>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="grid lg:grid-cols-3 gap-8">
          {/* Left Column - Upload */}
          <div className="lg:col-span-1">
            <div className="sticky top-8 space-y-6">
              <UploadBox onSearch={handleSearch} isLoading={isLoading} />

                {queryImage && (
                  <div className="bg-slate-800 rounded-lg p-4 border border-slate-700">
                    <h3 className="text-sm font-semibold text-slate-300 mb-3">Query Image</h3>
                    <div className="rounded-lg overflow-hidden bg-slate-900">
                      <img
                        src={queryImage}
                        alt="Query"
                        className="w-full h-48 object-cover"
                      />
                    </div>
                  </div>
                )}
              {/* Search Parameters - Always visible */}
              <div className="space-y-4">


                {/* Similarity Filter */}
                <SimilarityFilter
                  minSimilarity={minSimilarity}
                  onChange={setMinSimilarity}
                />

                {/* Top N Results */}
                <div className="bg-slate-800 rounded-lg p-4 border border-slate-700">
                  <h3 className="text-sm font-semibold text-slate-300 mb-4">Results Limit</h3>
                  <div className="space-y-2">
                    <label className="block text-xs font-medium text-slate-400">
                      Show top: <span className="text-white font-bold">{topN}</span> results
                    </label>
                    <input
                      type="range"
                      min="1"
                      max="10"
                      step="1"
                      value={topN}
                      onChange={(e) => setTopN(parseInt(e.target.value))}
                      className="w-full h-2 bg-slate-700 rounded-lg appearance-none cursor-pointer accent-purple-500"
                    />
                    <div className="flex gap-2 mt-3">
                      {[3, 5, 7, 10].map((n) => (
                        <button
                          key={n}
                          onClick={() => setTopN(n)}
                          className={`flex-1 px-2 py-1 rounded text-xs font-medium transition ${
                            topN === n
                              ? 'bg-purple-600 text-white'
                              : 'bg-slate-700 text-slate-300 hover:bg-slate-600'
                          }`}
                        >
                          {n}
                        </button>
                      ))}
                    </div>
                  </div>
                </div>
              </div>

            </div>
          </div>

          {/* Right Column - Results */}
          <div className="lg:col-span-2">
            {isLoading && <LoadingSpinner />}

            {!isLoading && results.length === 0 && queryImage && (
              <div className="text-center py-12">
                <p className="text-slate-400">No results found. Try adjusting the similarity threshold.</p>
              </div>
            )}

            {!isLoading && results.length > 0 && (
              <div>
                <div className="mb-6">
                  <h2 className="text-2xl font-bold text-white">
                    Similar Products ({results.length})
                  </h2>
                  <p className="text-slate-400 mt-1">Based on visual similarity</p>
                </div>
                <ProductGrid products={results} />
              </div>
            )}

            {!isLoading && !queryImage && (
              <div className="text-center py-12 bg-slate-800/50 rounded-lg border border-slate-700">
                <p className="text-slate-400 text-lg">
                  Upload an image to get started
                </p>
              </div>
            )}
          </div>
        </div>
      </main>

      {/* Toast Notification */}
      {showToast && <Toast message={toastMessage} type={toastType} />}

      {/* Footer */}
      <footer className="border-t border-slate-700 bg-slate-900/50 mt-16">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 text-center text-slate-400 text-sm">
          <p>Made with 🩵 by <a href="https://github.com/Pragyan14" className="hover:underline" target="_blank">Pragyan</a> </p>
        </div>
      </footer>
    </div>
  )
}