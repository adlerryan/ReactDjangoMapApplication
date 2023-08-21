import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Map from './Map';

function App() {
  const [spots, setSpots] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    console.log('Fetching spots data...');
    // Fetch all spots
    axios.get('http://127.0.0.1:8000/spot/') 
      .then(response => {
        const spots = response.data.map(spot => ({
          ...spot,
          latitude: parseFloat(spot.latitude),
          longitude: parseFloat(spot.longitude)
        }));

        setSpots(spots);
        setIsLoading(false);
      })
      .catch(error => {
        console.error(error);
        setIsLoading(false);
      });
  }, []);

  return (
    <div className="App" style={{ overflowX: 'hidden', position: 'relative' }}>
      {isLoading ? (
        <div>Loading...</div>
      ) : (
        <div style={{ overflow: 'hidden', height: '100vh', width: '100vw', position: 'relative' }}>
          <Map spots={spots} />
        </div>
      )}
    </div>
  );
}

export default App;
