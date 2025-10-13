'use client'

interface SimilarityFilterProps {
  minSimilarity: number
  onChange: (value: number) => void
}

export default function SimilarityFilter({ minSimilarity, onChange }: SimilarityFilterProps) {
  return (
    <div className="bg-slate-800 rounded-lg p-4 border border-slate-700">
      <h3 className="text-sm font-semibold text-slate-300 mb-4">Filter Results</h3>

      <div className="space-y-3">
        <div>
          <label className="block text-xs font-medium text-slate-400 mb-2">
            Minimum Similarity: <span className="text-white font-bold">{(minSimilarity * 100).toFixed(0)}%</span>
          </label>
          <input
            type="range"
            min="0"
            max="1"
            step="0.1"
            value={minSimilarity}
            onChange={(e) => onChange(parseFloat(e.target.value))}
            className="w-full h-2 bg-slate-700 rounded-lg appearance-none cursor-pointer accent-blue-500"
          />
        </div>

        <div className="flex gap-2 mt-4">
          {[0, 0.3, 0.5, 0.7, 0.9].map((value) => (
            <button
              key={value}
              onClick={() => onChange(value)}
              className={`flex-1 px-2 py-1 rounded text-xs font-medium transition ${
                Math.abs(minSimilarity - value) < 0.01
                  ? 'bg-blue-600 text-white'
                  : 'bg-slate-700 text-slate-300 hover:bg-slate-600'
              }`}
            >
              {(value * 100).toFixed(0)}%
            </button>
          ))}
        </div>
      </div>
    </div>
  )
}