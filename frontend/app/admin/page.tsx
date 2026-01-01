'use client'

export default function AdminPortal() {
  return (
    <div className="min-h-screen bg-gray-50">
      <nav className="bg-white shadow">
        <div className="container mx-auto px-4 py-4">
          <h1 className="text-2xl font-bold text-purple-600">Admin Portal</h1>
        </div>
      </nav>

      <div className="container mx-auto px-4 py-8">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8">
          <div className="bg-white p-6 rounded-lg shadow">
            <p className="text-gray-600 text-sm">Total Users</p>
            <p className="text-3xl font-bold text-blue-600">125</p>
          </div>
          <div className="bg-white p-6 rounded-lg shadow">
            <p className="text-gray-600 text-sm">Teacher Adoption Rate</p>
            <p className="text-3xl font-bold text-green-600">78%</p>
          </div>
          <div className="bg-white p-6 rounded-lg shadow">
            <p className="text-gray-600 text-sm">Platform Uptime</p>
            <p className="text-3xl font-bold text-purple-600">99.8%</p>
          </div>
        </div>

        <div className="bg-white p-6 rounded-lg shadow">
          <h2 className="text-xl font-bold mb-4">System Metrics</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <h3 className="font-semibold mb-3">Mastery Rate Trend</h3>
              <div className="h-40 bg-gray-100 rounded flex items-center justify-center">
                <span className="text-gray-500">Chart Placeholder</span>
              </div>
            </div>
            <div>
              <h3 className="font-semibold mb-3">Engagement Distribution</h3>
              <div className="h-40 bg-gray-100 rounded flex items-center justify-center">
                <span className="text-gray-500">Chart Placeholder</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
