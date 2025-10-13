'use client'

export default function LoadingSpinner() {
  return (
    <div className="flex flex-col items-center justify-center py-12">
      <div className="relative w-16 h-16 mb-4">
        {/* Outer ring */}
        <div className="absolute inset-0 rounded-full border-4 border-slate-700"></div>

        {/* Rotating border */}
        <div className="absolute inset-0 rounded-full border-4 border-transparent border-t-blue-500 border-r-cyan-500 animate-spin"></div>
      </div>

      <p className="text-slate-400 font-medium">Processing image...</p>
      <p className="text-slate-500 text-sm mt-1">This may take a few seconds on first run</p>
    </div>
  )
}