'use client'

interface ToastProps {
  message: string
  type: 'success' | 'error'
}

export default function Toast({ message, type }: ToastProps) {
  const bgColor = type === 'success' ? 'bg-green-600' : 'bg-red-600'
  const icon = type === 'success' ? '✓' : '✕'

  return (
    <div className="fixed bottom-6 right-6 animate-in fade-in slide-in-from-bottom-4 duration-300">
      <div className={`${bgColor} text-white px-6 py-3 rounded-lg shadow-lg flex items-center gap-3`}>
        <span className="text-xl font-bold">{icon}</span>
        <span className="font-medium">{message}</span>
      </div>
    </div>
  )
}