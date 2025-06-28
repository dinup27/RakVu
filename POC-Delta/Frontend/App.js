import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [nodes, setNodes] = useState([]);

  useEffect(() => {
    const fetchData = () => {
      axios.get('http://localhost:5000/api/nodes')
        .then(response => setNodes(response.data))
        .catch(error => console.error('Error fetching node data:', error));
    };

    fetchData();
    const interval = setInterval(fetchData, 5000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div className="min-h-screen bg-gray-100 p-10">
      <h1 className="text-4xl font-bold mb-8">Node Status Dashboard</h1>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {nodes.map((node, index) => (
          <div key={index} className="p-6 bg-white rounded-2xl shadow">
            <h2 className="text-2xl font-semibold">{node.name}</h2>
            <p className={`mt-2 text-lg ${node.status === 'Online' ? 'text-green-500' : 'text-red-500'}`}>
              {node.status}
            </p>
            <p className="mt-2">CPU: {node.cpu}</p>
            <p>Memory: {node.memory}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;