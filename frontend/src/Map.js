import React, { memo, useState } from 'react';
import { GoogleMap, LoadScript, MarkerF } from '@react-google-maps/api';
import Modal from '@mui/material/Modal';
import Backdrop from '@mui/material/Backdrop';
import Slide from '@mui/material/Slide';
import { styled } from '@mui/system';
import { CgProfile } from 'react-icons/cg'; // Importing icons
import { BsFilterRight } from 'react-icons/bs'
import { FaStar, FaDollarSign, FaMapMarkedAlt, FaCommentDots, FaUser, FaSearchLocation  } from 'react-icons/fa';
import { useTheme } from '@mui/material/styles';


const containerStyle = {
    width: '100%',
    height: 'calc(100vh - 55px)' // Adjust the height of the map container
};


const center = {
    lat: 40.7359, // Union Square, NYC
    lng: -73.9911
};

const StyledModal = styled(Modal)(({ theme }) => ({
    display: 'flex',
    alignItems: 'flex-end', // Align the modal to the bottom
    justifyContent: 'center',
    overflowY: 'auto', // Allow scrolling if content exceeds the modal's height
}));

const Content = styled('div')(({ theme }) => ({
    width: '100%', // Full width
    height: '70vh', // 70% of viewport height
    backgroundColor: 'white',
    borderTopLeftRadius: '20px', // Rounded corners at the top
    borderTopRightRadius: '20px',
    padding: '1em',
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    boxShadow: '0px -2px 10px rgba(0, 0, 0, 0.1)', // Shadow for a "lifted" effect
}));

const Image = styled('img')(({ theme }) => ({
    maxWidth: '90%', // Allow the image to take up to 90% of the modal's width
    maxHeight: '40vh', // Limit the image height to 40% of the viewport height
    objectFit: 'contain', // Ensure the entire image is displayed
    margin: '10px 0', // Add some margin around the image for spacing
}));

const IconContainer = styled('div')(({ theme }) => ({
    backgroundColor: 'rgba(0, 0, 0, 0.5)', // This gives a semi-transparent black background
    padding: '10px',
    borderRadius: '10px',
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    gap: '10px' // Space between icons
}));

const BottomMenuBar = styled('div')(({ theme }) => ({
    height: '38px',
    position: 'absolute',
    bottom: '0',
    left: '0',
    width: '100%',
    backgroundColor: '#5D3FD3', // Dark background for the menu bar
    padding: '10px 0',
    display: 'flex',
    justifyContent: 'space-around', // Distribute icons evenly
    alignItems: 'center',
    boxShadow: '0px -2px 5px rgba(0, 0, 0, 0.2)' // Optional shadow for a "lifted" effect
}));

const TransparentBackdrop = styled(Backdrop)(({ theme }) => ({
    backgroundColor: 'rgba(0, 0, 0, 0)', // Fully transparent backdrop
}));

const MenuIcon = styled('div')(({ theme }) => ({
    color: 'yellow',
    fontSize: '24px',
    cursor: 'pointer'
}));

const AdditionalContent = styled('div')(({ theme }) => ({
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    gap: '10px',
    marginTop: '20px'
}));

const Map = memo(({ spots }) => {
    const [isOpen, setIsOpen] = useState(false);
    const [selectedSpot, setSelectedSpot] = useState(null);

    const handleOpen = (spot) => {
        setSelectedSpot(spot);
        setIsOpen(true);
    };

    const handleClose = () => {
        setIsOpen(false);
    };

    const theme = useTheme(); // Get the default theme
    const slideDuration = theme.transitions.duration.enteringScreen; // Define a constant for the transition duration

    
    return (
        <LoadScript googleMapsApiKey="AIzaSyAoVICFhkTX654HmwVbQK8yjOUoTtObCzg">
            <div style={{ position: 'relative', width: '100%', height: '100vh' }}>
                <div style={{ position: 'absolute', top: '10px', left: '10px', color: 'yellow', fontSize: '24px', fontFamily: 'cursive' }}>
                    drycana
                </div>
                <div style={{ position: 'absolute', top: '10px', right: '10px', display: 'flex', flexDirection: 'column', alignItems: 'center', zIndex: 1000 }}>
                  <IconContainer>
                    <CgProfile size={24} style={{ marginBottom: '15px', color: 'yellow' }} />
                    <FaSearchLocation size={24} style={{ marginBottom: '15px', color: 'yellow' }} />
                    <BsFilterRight size={24} style={{ color: 'yellow' }} />
                  </IconContainer>
                </div>
              
                <GoogleMap
                    mapContainerStyle={containerStyle}
                    center={center}
                    zoom={15}
                    options={{ 
                        disableDefaultUI: true,
                        
                        styles: [
                            { elementType: "geometry", stylers: [{ color: "#242f3e" }] },
                            { elementType: "labels.text.stroke", stylers: [{ color: "#242f3e" }] },
                            { elementType: "labels.text.fill", stylers: [{ color: "#746855" }] },
                            {
                                featureType: "administrative.locality",
                                elementType: "labels.text.fill",
                                stylers: [{ color: "#d59563" }],
                            },
                            {
                                featureType: "poi", // Hides points of interest
                                stylers: [{ visibility: "off" }],
                            },
                            {
                                featureType: "poi.park",
                                elementType: "geometry",
                                stylers: [{ color: "#263c3f" }],
                            },
                            {
                                featureType: "poi.park",
                                elementType: "labels.text.fill",
                                stylers: [{ color: "#6b9a76" }],
                            },
                            {
                                featureType: "road",
                                elementType: "geometry",
                                stylers: [{ color: "#38414e" }],
                            },
                            {
                                featureType: "road",
                                elementType: "geometry.stroke",
                                stylers: [{ color: "#212a37" }],
                            },
                            {
                                featureType: "road",
                                elementType: "labels.text.fill",
                                stylers: [{ color: "#9ca5b3" }],
                            },
                            {
                                featureType: "road.highway",
                                elementType: "geometry",
                                stylers: [{ color: "#746855" }],
                            },
                            {
                                featureType: "road.highway",
                                elementType: "geometry.stroke",
                                stylers: [{ color: "#1f2835" }],
                            },
                            {
                                featureType: "road.highway",
                                elementType: "labels.text.fill",
                                stylers: [{ color: "#f3d19c" }],
                            },
                            {
                                featureType: "transit",
                                elementType: "geometry",
                                stylers: [{ color: "#2f3948" }],
                            },
                            {
                                featureType: "transit.station",
                                elementType: "labels.text.fill",
                                stylers: [{ color: "#d59563" }],
                            },
                            {
                                featureType: "water",
                                elementType: "geometry",
                                stylers: [{ color: "#17263c" }],
                            },
                            {
                                featureType: "water",
                                elementType: "labels.text.fill",
                                stylers: [{ color: "#515c6d" }],
                            },
                            {
                                featureType: "water",
                                elementType: "labels.text.stroke",
                                stylers: [{ color: "#17263c" }],
                            },
                            {
                                featureType: "administrative.neighborhood", // Show neighborhoods
                                elementType: "labels.text.fill",
                                stylers: [{ color: "#d59563" }],
                            },
                            {
                                featureType: "administrative.locality", // Show localities (towns and cities)
                                elementType: "labels.text.fill",
                                stylers: [{ color: "#d59563" }],
                            }
                        ],
                    }}
                >
                
                {spots.map(spot => (
                        <MarkerF
                            key={spot.id}
                            position={{ lat: spot.latitude, lng: spot.longitude }}
                            title={spot.name}
                            onLoad={() => console.log('Marker loaded')}
                            visible={true}
                            onClick={() => handleOpen(spot)}
                            options={{
                                icon: {
                                    url: "https://maps.google.com/mapfiles/ms/icons/yellow-dot.png",
                                },
                                zIndex: 999
                            }}
                        />
                    ))}
                </GoogleMap>
                
                    <BottomMenuBar>
                        <MenuIcon><FaStar /></MenuIcon>
                        <MenuIcon><FaDollarSign /></MenuIcon>
                        <MenuIcon><FaMapMarkedAlt /></MenuIcon>
                        <MenuIcon><FaCommentDots /></MenuIcon>
                        <MenuIcon><FaUser /></MenuIcon>
                    </BottomMenuBar>
               
                    <StyledModal
                open={isOpen}
                onClose={handleClose}
                closeAfterTransition
                BackdropComponent={TransparentBackdrop}
            >
                <Slide 
                    direction="up" 
                    in={isOpen}
                    timeout={{
                        enter: slideDuration,
                        exit: slideDuration
                    }}
                    style={{ 
                        transition: `transform ${slideDuration}ms ${theme.transitions.easing.easeInOut}`,
                        transitionDelay: isOpen ? slideDuration : 0 
                    }}
                >
                    <Content>
                        {selectedSpot && (
                            <React.Fragment>
                                <h2>{selectedSpot.name}</h2>
                                
                                {/* Display the main image if it exists */}
                                {selectedSpot.main_image && 
                                    <Image src={`http://127.0.0.1:8000${selectedSpot.main_image}`} alt={selectedSpot.name} />}

                                
                                <p>{selectedSpot.description}</p>

                                {/* Additional content starts here */}
                                <AdditionalContent>
                                    <h3>Additional Info</h3>
                                    <p>Placeholder text for additional information.</p>
                                    <button>Sample Button</button>
                                    <input type="text" placeholder="Sample Input" />
                                    <div>Another placeholder element</div>
                                </AdditionalContent>
                                {/* Additional content ends here */}
                            </React.Fragment>
                        )}
                    </Content>
                </Slide>
            </StyledModal>
        </div>
    </LoadScript>
);
});

export default Map;