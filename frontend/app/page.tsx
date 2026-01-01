import 'next/image'

export default function Home() {
  return (
    <main className="min-h-screen bg-gradient-to-br from-blue-600 to-indigo-800">
      <div className="container mx-auto px-4 py-20">
          <h1 className="text-5xl font-bold text-white mb-4">AMEP Platform</h1>
        <p className="text-xl text-blue-100 mb-8">
          Adaptive Mastery & Engagement Platform
        </p>
        
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-12">
          <a href="/student" className="bg-white p-8 rounded-lg shadow-lg hover:shadow-xl transition">
            <h2 className="text-2xl font-bold text-blue-600 mb-2">Student App</h2>
            <p className="text-gray-600">View assignments and track your mastery</p>
          </a>
          
          <a href="/teacher" className="bg-white p-8 rounded-lg shadow-lg hover:shadow-xl transition">
            <h2 className="text-2xl font-bold text-green-600 mb-2">Teacher Dashboard</h2>
            <p className="text-gray-600">Monitor class engagement and assessments</p>
          </a>
          
          <a href="/admin" className="bg-white p-8 rounded-lg shadow-lg hover:shadow-xl transition">
            <h2 className="text-2xl font-bold text-purple-600 mb-2">Admin Portal</h2>
            <p className="text-gray-600">Manage platform and analytics</p>
          </a>
        </div>
      </div>
    </main>
  )
}
