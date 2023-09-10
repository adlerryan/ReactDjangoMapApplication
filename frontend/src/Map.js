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
import { useMediaQuery } from '@mui/material';
import Grid from '@mui/material/Grid';
import { FiPhoneCall } from 'react-icons/fi';
import { BsStar } from 'react-icons/bs';
import { TbWorldWww } from 'react-icons/tb'; // Please note: I'm not aware of a 'TbWorldWww' icon. Ensure this import is correct.
import { SiUber } from 'react-icons/si';
import { FaLyft } from 'react-icons/fa';
import { ImYelp } from 'react-icons/im';
import { BsInstagram } from 'react-icons/bs';
import { MdOutlineDirections } from 'react-icons/md';
import { CopyToClipboard } from 'react-copy-to-clipboard';
import { FiCopy } from 'react-icons/fi';
import Slider from '@mui/material/Slider';



const TitleSection = styled('div')(({ theme }) => ({
    width: '100%',
    backgroundColor: '#5D3FD3', // Color of the bottom menu bar
    padding: '10px 20px', // Padding for spacing
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'flex-start', // Align content to the left
    boxShadow: '0px 2px 5px rgba(0, 0, 0, 0.1)', // Optional shadow for a "lifted" effect
    borderTopLeftRadius: '30px', // Match the modal's border radius
    borderTopRightRadius: '30px',
    boxSizing: 'border-box',
    position: 'sticky',
    top: '0', // Stick to the top of the modal
    zIndex: 10, // Ensure it's above other content
}));

const TitleText = styled('h2')(({ theme }) => ({
    margin: '0', // Remove default margin
    marginLeft: '20px',
    color: '#fff', // White text color to contrast with the dark background
    fontSize: '1.5rem', // Adjust font size as needed
    boxSizing: 'border-box',
}));

const ReviewInputContainer = styled('div')(({ theme }) => ({
    width: '100%',
    marginTop: '40px',
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
}));

const ReviewTextArea = styled('textarea')(({ theme }) => ({
    width: '95%',
    minHeight: '100px',
    padding: '10px',
    borderRadius: '10px',
    border: '1px solid #ccc',
    fontFamily: 'Roboto, sans-serif',
    fontSize: '1rem',
    resize: 'vertical', // Allow vertical resizing
}));

const SubmitReviewButton = styled('button')(({ theme }) => ({
    marginTop: '10px',
    padding: '10px 20px',
    borderRadius: '10px',
    backgroundColor: theme.palette?.primary?.main || '#5D3FD3',
    color: '#fff',
    border: 'none',
    cursor: 'pointer',
    '&:hover': {
        backgroundColor: theme.palette?.primary?.dark || '#4a2fb0',
    }
}));

const averageRatingMark = (rating) => [
    {
        value: Number(rating),
        label: (
            <div style={{ position: 'relative', bottom: '10px' }}>
                <BsStar style={{ color: 'red' }} />
            </div>
        )
    }
];

const StyledSlider = styled(Slider)(({ theme }) => ({
    width: '80%',  // Adjust this value to your preference
    margin: '0 auto',  // This will center the slider
}));

// Add styles for the review section and placeholder
const ReviewSection = styled('div')(({ theme }) => ({
    width: '100%',  // Take up the full width of its parent
    marginTop: '10px',
    padding: '10px',
    borderRadius: '10px',
    backgroundColor: 'rgba(240, 245, 250, 0.95)', // Match the modal's background
    boxShadow: '0px 2px 5px rgba(0, 0, 0, 0.1)',
    textAlign: 'center',
    boxSizing: 'border-box',  // Ensure padding and border are included in the total width and height
}));

const ReviewPlaceholder = styled('p')(({ theme }) => ({
    fontFamily: 'Roboto, sans-serif',
    fontSize: '1rem',
    color: '#aaa', // Placeholder text color
    textAlign: 'center',
  
}));


const CopyIcon = styled(FiCopy)(({ theme }) => ({
    cursor: 'pointer',
    transition: 'transform 0.3s ease-in-out, color 0.3s ease-in-out',
    '&:hover': {
        transform: 'scale(1.1)', // This will slightly enlarge the icon when hovered
        color: theme.palette?.primary?.main || '#5D3FD3', // Change color on hover, defaulting to a purple shade if the theme doesn't provide a primary color
    },
    '&:active': {
        transform: 'scale(0.9)', // This will slightly reduce the icon size when clicked
    }
}));


const Description = styled('p')(({ theme }) => ({
    fontFamily: 'Roboto, sans-serif',
    fontSize: '1rem',
    color: '#333',
    textAlign: 'justify',
    maxWidth: '90%',
    margin: '10px 0',
}));

const InfoSection = styled('div')({
    width: '100%',  // Take up the full width of its parent
    textAlign: 'left',  // Align content to the left
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'flex-start',  // Align children to the start (left side)
    // overflowX: 'hidden',
});

const InfoHeader = styled('h3')(({ theme }) => ({
    fontFamily: 'Roboto, sans-serif',  // Assuming this is the font used for the spot name
    fontSize: '1.2rem',  // Adjust this value to make the font smaller or larger
    fontWeight: 'bold',
    margin: '10px 0',  // Add some margin for spacing
    color: '#333',  // Adjust the color if needed
    textAlign: 'left',  // Align the text to the left
}));


const AddressContainer = styled('div')(({ theme }) => ({
    display: 'flex',
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    width: '100%',
    backgroundColor: 'rgba(240, 245, 250, 0.95)',
    padding: '10px',
    borderRadius: '10px',
    margin: '10px 0',
    boxShadow: '0px 2px 5px rgba(0, 0, 0, 0.1)',
    boxSizing: 'border-box',
}));



const getAffiliateIcon = (appName, url) => {
    const iconProps = {
        size: 24,
        style: { verticalAlign: 'middle' } // To align the icon with the text
    };

    let icon;
    switch (appName.toLowerCase()) {
        case 'uber':
            icon = <SiUber {...iconProps} />;
            break;
        case 'lyft':
            icon = <FaLyft {...iconProps} />;
            break;
        case 'yelp':
            icon = <ImYelp {...iconProps} />;
            break;
        case 'instagram':
            icon = <BsInstagram {...iconProps} />;
            break;
        default:
            icon = null;
    }

    return (
        <a href={url} target="_blank" rel="noopener noreferrer">
            {icon}
        </a>
    );
};



const IconWithLabel = styled('div')(({ theme }) => ({
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    gap: '5px'
}));

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
    alignItems: 'flex-end',
    justifyContent: 'center',
    overflowY: 'auto',
    zIndex: 9999, // Ensure the modal is on top of other elements
}));

const Content = styled('div')(({ theme }) => ({
    width: '100%',
    zIndex: 10000,
    height: useMediaQuery(theme.breakpoints.down('sm')) ? '80vh' : '80vh',
    backgroundColor: 'rgba(240, 245, 250, 0.95)',
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    boxShadow: '0px -2px 10px rgba(0, 0, 0, 0.1)',
    fontFamily: 'Roboto, sans-serif',
    animation: 'fadeIn 0.5s',
    '& button:hover': {
        backgroundColor: '#ddd',
    },
    '& button:active': {
        backgroundColor: '#bbb',
    },
    '& input:focus': {
        borderColor: '#555',
    },
    '&::-webkit-scrollbar': {
        display: 'none',
    },
    
    // Hide scrollbar for Firefox
    scrollbarWidth: 'none',
    
    // Ensure content is still scrollable
    '-ms-overflow-style': 'none',
    flex: 1, // This ensures that the Content component takes up all available space
    overflowY: 'auto',
    border: '1px solid #ccc',  // This adds a light gray border
    borderRadius: '30px', 
    scrollbarWidth: 'thin',
    scrollbarColor: '#888 #f5f5f5',
}));

const Image = styled('img')(({ theme }) => ({
    maxWidth: '150%', // Allow the image to take up to 90% of the modal's width
    maxHeight: '40vh', // Limit the image height to 40% of the viewport height
    objectFit: 'contain', // Ensure the entire image is displayed
    margin: '5px 0', // Add some margin around the image for spacing
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

const MenuIcon = styled('div')(({ theme, isActive }) => ({
    color: 'yellow',
    fontSize: isActive ? '32px' : '20px', // Make the active icon bigger
    cursor: 'pointer',
    position: 'relative',
}));


const ActiveLine = styled('div')(({ theme, position }) => ({
    position: 'absolute',
    bottom: '5px',
    left: position + '%',
    width: '24px',
    height: '2px',
    backgroundColor: 'yellow',
    transform: 'translateX(-50%)', // Center the line
    transition: 'left 0.3s ease-in-out',
}));


const getActiveLinePosition = (page) => {
    switch (page) {
        case 'favorites':
            return 10.5; // Adjust these values based on the exact positions of your icons
        case 'price':
            return 30;
        case 'map':
            return 50;
        case 'comments':
            return 70;
        case 'user':
            return 89.5;
        default:
            return 50; // Default to the map icon
    }
};




const Map = memo(({ spots }) => {
    const [isOpen, setIsOpen] = useState(false);
    const [selectedSpot, setSelectedSpot] = useState(null);

    const handleOpen = (spot) => {
        setSelectedSpot(spot);
        setIsOpen(true);
    };

    const handleClose = (event) => {
        // Check if the click event's target is the modal content itself
        if (event.target === event.currentTarget) {
            setIsOpen(false);
        }
    };
    

    const theme = useTheme(); // Get the default theme
    const slideDuration = theme.transitions.duration.enteringScreen; // Define a constant for the transition duration

    const [ratingValue, setRatingValue] = useState(5); // Default value is set to 5
    const [reviewContent, setReviewContent] = useState("");

    const handleSliderChange = (event, newValue) => {
        setRatingValue(newValue);
    };
    const [activePage, setActivePage] = useState('map');

    
    return (
        <LoadScript googleMapsApiKey="API KEY HERE">
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
                    <MenuIcon isActive={activePage === 'favorites'} onClick={() => setActivePage('favorites')}><FaStar /></MenuIcon>
                    <MenuIcon isActive={activePage === 'price'} onClick={() => setActivePage('price')}><FaDollarSign /></MenuIcon>
                    <MenuIcon isActive={activePage === 'map'} onClick={() => setActivePage('map')}><FaMapMarkedAlt /></MenuIcon>
                    <MenuIcon isActive={activePage === 'comments'} onClick={() => setActivePage('comments')}><FaCommentDots /></MenuIcon>
                    <MenuIcon isActive={activePage === 'user'} onClick={() => setActivePage('user')}><FaUser /></MenuIcon>
                    <ActiveLine position={getActiveLinePosition(activePage)} />
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
                    <Content className="modal-content"> {/* Add a class name to the modal content */}
                        {/* <CloseButton onClick={handleClose}>
                            <CloseIcon />
                        </CloseButton> */}
                        {selectedSpot && (
                            <React.Fragment>
                                <TitleSection>
                                    <TitleText>{selectedSpot.name}</TitleText>
                                </TitleSection>
                                {selectedSpot.main_image && 
                                    <Image src={`http://127.0.0.1:8000${selectedSpot.main_image}`} alt={selectedSpot.name} />}
                                
                                <Grid container spacing={3}>
                                    <Grid item xs={4}>
                                        <IconWithLabel>
                                            <FiPhoneCall size={24} />
                                            <span>{selectedSpot.phone_number}</span>
                                        </IconWithLabel>
                                    </Grid>
                                    <Grid item xs={4}>
                                        <IconWithLabel>
                                            <BsStar size={24} />
                                            <span>{selectedSpot.rating}</span>
                                        </IconWithLabel>
                                    </Grid>
                                    <Grid item xs={4}>
                                        <IconWithLabel>
                                            <MdOutlineDirections size={24}  />
                                            <span>Directions</span>
                                        </IconWithLabel>
                                    </Grid>
                                    <Grid item xs={4}>
                                        <IconWithLabel>
                                            <TbWorldWww size={24} />
                                            {selectedSpot.website ? 
                                                <a href={selectedSpot.website} target="_blank" rel="noopener noreferrer">Website</a> : 
                                                <span>No Website</span>}
                                        </IconWithLabel>
                                    </Grid>
                              
                                  
                                    {selectedSpot.affiliate_apps.map(app => (
                                    <Grid item xs={4} key={app.affiliate_app.id}>
                                        <IconWithLabel>
                                            {getAffiliateIcon(app.affiliate_app.name, app.url || app.affiliate_app.website)}
                                            <a href={app.url || app.affiliate_app.website} target="_blank" rel="noopener noreferrer">
                                                {app.affiliate_app.name}
                                            </a>
                                        </IconWithLabel>
                                    </Grid>
                                ))}
                                </Grid>
                                <InfoSection>
                                    <InfoHeader>Address</InfoHeader>
                                    <AddressContainer>
                                        <span>{selectedSpot.address}</span>
                                        <CopyToClipboard text={selectedSpot.address}>
                                            <CopyIcon size={24} />
                                        </CopyToClipboard>
                                    </AddressContainer>
                                </InfoSection>

                                <InfoSection>
                                    <InfoHeader>Description</InfoHeader>
                                    <Description>
                                        {selectedSpot.description}
                                    </Description>
                                    
                                    <InfoHeader>Reviews</InfoHeader>
                                    <ReviewSection>
                                        <ReviewPlaceholder>
                                            No reviews yet, be the first to review!
                                        </ReviewPlaceholder>
                                    </ReviewSection>

                                    <h4>Rate & Review {selectedSpot.name}</h4>
                                    <StyledSlider
                                        value={ratingValue}
                                        onChange={handleSliderChange}
                                        step={0.1}
                                        min={0.1}
                                        max={10}
                                        valueLabelDisplay="auto"
                                        marks={selectedSpot ? averageRatingMark(selectedSpot.rating) : []}

                                    />
                                </InfoSection>
                                <ReviewInputContainer>
                                    <ReviewTextArea 
                                        placeholder="Write your review here..." 
                                        value={reviewContent} 
                                        onChange={(e) => setReviewContent(e.target.value)}
                                    />
                                    <SubmitReviewButton onClick={() => {
                                        // For now, just log the review content
                                        console.log("Review submitted:", reviewContent);
                                        setReviewContent(""); // Clear the review content
                                    }}>
                                        Submit Review
                                    </SubmitReviewButton>
                                </ReviewInputContainer>

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