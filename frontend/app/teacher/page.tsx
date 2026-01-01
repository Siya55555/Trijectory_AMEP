'use client'

export default function TeacherDashboard() {
  return (
    <div className="min-h-screen bg-gray-50">
      <nav className="bg-white shadow">
        <div className="container mx-auto px-4 py-4">
          <h1 className="text-2xl font-bold text-green-600">Teacher Dashboard</h1>
        </div>
      </nav>

      <div className="container mx-auto px-4 py-8">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-8">
          <div className="bg-white p-6 rounded-lg shadow">
            <p className="text-gray-600 text-sm">Class Engagement</p>
            <p className="text-3xl font-bold text-blue-600">85%</p>
          </div>
          <div className="bg-white p-6 rounded-lg shadow">
            <p className="text-gray-600 text-sm">Avg Mastery</p>
            <p className="text-3xl font-bold text-green-600">72%</p>
          </div>
          <div className="bg-white p-6 rounded-lg shadow">
            <p className="text-gray-600 text-sm">Confusion Index</p>
            <p className="text-3xl font-bold text-orange-600">18%</p>
          </div>
          <div className="bg-white p-6 rounded-lg shadow">
            <p className="text-gray-600 text-sm">At Risk Students</p>
            <p className="text-3xl font-bold text-red-600">3</p>
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {/* Real-time Poll */}
          <div className="bg-white p-6 rounded-lg shadow">
            <h2 className="text-xl font-bold mb-4">Live Poll</h2>
            <div className="space-y-4">
              <p className="font-semibold">Do you understand this concept?</p>
              <div>
                <div className="flex justify-between mb-1">
                  <span>Strongly Agree</span>
                  <span className="font-bold">8 (32%)</span>
                </div>
                <div className="w-full bg-gray-200 rounded-full h-2">
                  <div className="bg-green-600 h-2 rounded-full" style={{width: '32%'}}></div>
                </div>
              </div>
              <div>
                <div className="flex justify-between mb-1">
                  <span>Agree</span>
                  <span className="font-bold">12 (48%)</span>
                </div>
                <div className="w-full bg-gray-200 rounded-full h-2">
                  <div className="bg-blue-600 h-2 rounded-full" style={{width: '48%'}}></div>
                </div>
              </div>
              <div>
                <div className="flex justify-between mb-1">
                  <span>Disagree</span>
                  <span className="font-bold">5 (20%)</span>
                </div>
                <div className="w-full bg-gray-200 rounded-full h-2">
                  <div className="bg-orange-600 h-2 rounded-full" style={{width: '20%'}}></div>
                </div>
              </div>
            </div>
          </div>

          {/* Disengaged Students */}
          <div className="bg-white p-6 rounded-lg shadow">
            <h2 className="text-xl font-bold mb-4">Students Needing Support</h2>
            <div className="space-y-3">
              <div className="p-3 border-l-4 border-red-500 bg-red-50">
                <p className="font-semibold">John Smith</p>
                <p className="text-sm text-gray-600">Low engagement • Algebra weakness</p>
              </div>
              <div className="p-3 border-l-4 border-orange-500 bg-orange-50">
                <p className="font-semibold">Sarah Johnson</p>
                <p className="text-sm text-gray-600">High confusion index</p>
              </div>
              <div className="p-3 border-l-4 border-yellow-500 bg-yellow-50">
                <p className="font-semibold">Mike Chen</p>
                <p className="text-sm text-gray-600">Low participation rate</p>
              </div>
            </div>
          </div>

          {/* PBL Management */}
          <div className="bg-white p-6 rounded-lg shadow md:col-span-2">
            <h2 className="text-xl font-bold mb-4">Active Projects</h2>
            <div className="overflow-x-auto">
              <table className="min-w-full">
                <thead className="bg-gray-100">
                  <tr>
                    <th className="px-4 py-2 text-left">Project</th>
                    <th className="px-4 py-2 text-left">Teams</th>
                    <th className="px-4 py-2 text-left">Progress</th>
                  </tr>
                </thead>
                <tbody>
                  <tr className="border-t">
                    <td className="px-4 py-2">Smart City Design</td>
                    <td className="px-4 py-2">3 teams</td>
                    <td className="px-4 py-2">
                      <div className="w-32 bg-gray-200 rounded-full h-2">
                        <div className="bg-blue-600 h-2 rounded-full" style={{width: '60%'}}></div>
                      </div>
                    </td>
                  </tr>
                  <tr className="border-t">
                    <td className="px-4 py-2">Climate Analysis</td>
                    <td className="px-4 py-2">4 teams</td>
                    <td className="px-4 py-2">
                      <div className="w-32 bg-gray-200 rounded-full h-2">
                        <div className="bg-green-600 h-2 rounded-full" style={{width: '40%'}}></div>
                      </div>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
