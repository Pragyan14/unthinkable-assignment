'use client'

import { useState, useCallback } from 'react'
import axios from 'axios'

interface Product {
  id: number
  name: string
  category: string
  image_url: string
  similarity_score: number
  description?: string
}

interface UseSearchReturn {
  isLoading: boolean
  queryImage: string | null
  results: Product[]
  error: string | null
  search: (imageData: string | File, isUrl: boolean, minSimilarity: number, topN: number) => Promise<boolean>
}

export function useSearch(): UseSearchReturn {
  const [isLoading, setIsLoading] = useState(false)
  const [queryImage, setQueryImage] = useState<string | null>(null)
  const [results, setResults] = useState<Product[]>([])
  const [error, setError] = useState<string | null>(null)

  const search = useCallback(
    async (
      imageData: string | File,
      isUrl: boolean,
      minSimilarity: number,
      topN: number
    ): Promise<boolean> => {
      setIsLoading(true)
      setError(null)

      try {
        const apiUrl = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'
        const formData = new FormData()

        if (isUrl) {
          formData.append('image_url', imageData as string)
          setQueryImage(imageData as string)
        } else {
          formData.append('file', imageData as File)
          // Create local preview
          const reader = new FileReader()
          reader.onload = (e) => {
            setQueryImage(e.target?.result as string)
          }
          reader.readAsDataURL(imageData as File)
        }

        formData.append('min_similarity', minSimilarity.toString())
        formData.append('top_n', topN.toString())

        const response = await axios.post(`${apiUrl}/api/search`, formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        })

        setResults(response.data.similar_products || [])
        return true
      } catch (err) {
        const errorMessage =
          err instanceof axios.AxiosError
            ? err.response?.data?.detail || err.message
            : 'An error occurred during search'

        setError(errorMessage)
        setResults([])
        return false
      } finally {
        setIsLoading(false)
      }
    },
    []
  )

  return {
    isLoading,
    queryImage,
    results,
    error,
    search,
  }
}
