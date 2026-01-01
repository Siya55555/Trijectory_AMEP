'use client'

export default function StudentApp() {
  return (
    <div className="min-h-screen bg-gray-50">
      <nav className="bg-white shadow">
        <div className="container mx-auto px-4 py-4">
          <h1 className="text-2xl font-bold text-blue-600">Student Portal</h1>
        </div>
      </nav>

      <div className="container mx-auto px-4 py-8">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {/* Mastery Profile */}
          <div className="bg-white p-6 rounded-lg shadow">
            <h2 className="text-xl font-bold mb-4">My Mastery Profile</h2>
            <div className="space-y-3">
              <div className="flex justify-between">
                <span>Algebra</span>
                <div className="w-32 bg-gray-200 rounded-full h-2">
                  <div className="bg-blue-600 h-2 rounded-full" style={{width: '75%'}}></div>
                </div>
              </div>
              <div className="flex justify-between">
                <span>Geometry</span>
                <div className="w-32 bg-gray-200 rounded-full h-2">
                  <div className="bg-green-600 h-2 rounded-full" style={{width: '60%'}}></div>
                </div>
              </div>
              <div className="flex justify-between">
                <span>Calculus</span>
                <div className="w-32 bg-gray-200 rounded-full h-2">
                  <div className="bg-orange-600 h-2 rounded-full" style={{width: '45%'}}></div>
                </div>
              </div>
            </div>
          </div>

          {/* Adaptive Assignments */}
          <div className="bg-white p-6 rounded-lg shadow">
            <h2 className="text-xl font-bold mb-4">Adaptive Assignments</h2>
            <div className="space-y-3">
              <div className="p-3 border-l-4 border-orange-500 bg-orange-50">
                <p className="font-semibold">Calculus Practice - Level 2</p>
                <p className="text-sm text-gray-600">5 problems assigned</p>
              </div>
              <div className="p-3 border-l-4 border-green-500 bg-green-50">
                <p className="font-semibold">Algebra Mastery Test</p>
                <p className="text-sm text-gray-600">Completed</p>
              </div>
            </div>
          </div>

          {/* PBL Projects */}
          <div className="bg-white p-6 rounded-lg shadow md:col-span-2">
            <h2 className="text-xl font-bold mb-4">Project-Based Learning</h2>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div className="p-4 border rounded-lg hover:shadow transition">
                <h3 className="font-bold text-blue-600">Smart City Design</h3>
                <p className="text-sm text-gray-600 mt-2">Team: 4 members | Due: 2 weeks</p>
                <div className="mt-3 w-full bg-gray-200 rounded-full h-2">
                  <div className="bg-blue-600 h-2 rounded-full" style={{width: '40%'}}></div>
                </div>
              </div>
              <div className="p-4 border rounded-lg hover:shadow transition">
                <h3 className="font-bold text-green-600">Climate Change Analysis</h3>
                <p className="text-sm text-gray-600 mt-2">Team: 3 members | Due: 3 weeks</p>
                <div className="mt-3 w-full bg-gray-200 rounded-full h-2">
                  <div className="bg-green-600 h-2 rounded-full" style={{width: '20%'}}></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
