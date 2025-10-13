'use client'

import { useState, useRef } from 'react'

interface UploadBoxProps {
  onSearch: (imageData: string | File, isUrl: boolean) => Promise<void>
  isLoading: boolean
}

export default function UploadBox({ onSearch, isLoading }: UploadBoxProps) {
  const [imageUrl, setImageUrl] = useState('')
  const [urlError, setUrlError] = useState('')
  const fileInputRef = useRef<HTMLInputElement>(null)

  const handleFileUpload = async (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0]
    if (file) {
      if (!file.type.startsWith('image/')) {
        alert('Please select a valid image file')
        return
      }
      await onSearch(file, false)
    }
  }

  const handleUrlSubmit = async () => {
    setUrlError('')
    if (!imageUrl.trim()) {
      setUrlError('Please enter an image URL')
      return
    }

    try {
      new URL(imageUrl)
    } catch {
      setUrlError('Please enter a valid URL')
      return
    }

    await onSearch(imageUrl, true)
  }

  const handleDrop = (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault()
    const file = e.dataTransfer.files?.[0]
    if (file && file.type.startsWith('image/')) {
      onSearch(file, false)
    }
  }

  return (
    <div className="space-y-4">
      {/* File Upload */}
      <div
        onDrop={handleDrop}
        onDragOver={(e) => e.preventDefault()}
        onClick={() => fileInputRef.current?.click()}
        className="border-2 border-dashed border-slate-600 rounded-lg p-8 text-center cursor-pointer hover:border-slate-500 transition bg-slate-800/30 hover:bg-slate-800/50"
      >
        <input
          ref={fileInputRef}
          type="file"
          accept="image/*"
          onChange={handleFileUpload}
          disabled={isLoading}
          className="hidden"
        />
        <div className="text-4xl mb-3">📁</div>
        <p className="text-white font-semibold">Click to upload or drag and drop</p>
        <p className="text-slate-400 text-sm mt-1">PNG, JPG, GIF up to 10MB</p>
      </div>

      {/* URL Input */}
      <div className="space-y-2">
        <label className="block text-sm font-medium text-slate-300">Or paste image URL</label>
        <div className="flex gap-2">
          <input
            type="text"
            value={imageUrl}
            onChange={(e) => {
              setImageUrl(e.target.value)
              setUrlError('')
            }}
            placeholder="https://example.com/image.jpg"
            disabled={isLoading}
            className="flex-1 px-4 py-2 bg-slate-700 border border-slate-600 rounded-lg text-white placeholder-slate-500 focus:outline-none focus:border-slate-500 transition"
            onKeyPress={(e) => {
              if (e.key === 'Enter') {
                handleUrlSubmit()
              }
            }}
          />
          <button
            onClick={handleUrlSubmit}
            disabled={isLoading}
            className="px-4 py-2 bg-blue-600 hover:bg-blue-700 disabled:bg-slate-600 text-white rounded-lg font-medium transition"
          >
            Search
          </button>
        </div>
        {urlError && <p className="text-red-400 text-sm">{urlError}</p>}
      </div>
    </div>
  )
}