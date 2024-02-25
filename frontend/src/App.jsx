import React, { useState, useEffect } from 'react'

const App = () => {
  const [data, setData] = useState([])

  const fetchData = async () => {
    let response = await fetch('http://127.0.0.1:8000/api/v1/cars/')
    let data = await response.json()
    setData(data)
    console.log(data)
  }
  useEffect(() => {
    fetchData();
  }, [])

  return (
    <div className="text-3xl p-10">
      <div>Length: {data.length}</div>
      <hr />
      {data.map((data, i) => (
        <div key={i} className='mt-5'>
          {data.model}
        </div>
      ))}
    </div>
  )
}

export default App