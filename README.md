# ReactDjangoMapApplication
# Map Application with Django and Google Maps API
This repository contains a web application that integrates React for the frontend and Django for the backend. The main functionality revolves around displaying and managing map-related data.

# Update
- Continuously updating this repository. 

## Front-end
The front-end of the application is built using React.js. The key components of the front-end React.js can be found in the **frontend** folder. 

## Backend
- **drycana:** This is the primary Django app. It contains the following key components:

  - **models.py:** Defines the data models used in the application.
  - **views.py:** Contains the logic for handling HTTP requests.
  - **serializers.py:** Used for converting complex data types, such as Django models, into a format that can be easily rendered into JSON, XML, or other content types.
  - **urls.py:** Defines the URL patterns for the app.
  - **admin.py:** Configurations for the Django admin interface.
  - **migrations:** Contains database migration scripts.
  - **page:** Another Django app in the repository. It has similar components as the drycana app, such as models, views, serializers, and URLs.

**drycana/models.py**
- **MyModel:** A basic model with a name and description field.
- **AffiliateApp:** Represents affiliate applications with a name and website URL.
- **LocationType:** Represents different types of locations with a name and website URL.
- **Tag:** Represents tags with a name and website URL.
- **Spot:** Represents a specific location or spot. It has fields for name, address, latitude, longitude, website, rating, cover charge, description, phone number, and many-to-many relationships with LocationType and Tag.
- **SpotAffiliate:** Represents the relationship between a spot and an affiliate app. It contains a foreign key to both Spot and AffiliateApp.
- **SpotImage:** Represents images associated with a spot. It has a foreign key to Spot and an image field.

**drycana/views.py**
- **MyModelViewSet, AffiliateAppViewSet, LocationTypeViewSet, TagViewSet, SpotViewSet, SpotImageViewSet:** These are Django Rest Framework viewsets for the respective models. They handle CRUD operations for each model.
- **HomePageView:** A simple Django view that renders the 'index.html' template.

**drycana/serializers.py**
- Serializers for each model are defined here. They are used to convert Django models to JSON format for API responses. Notably, the SpotSerializer has custom logic for handling the creation and updating of spots, especially concerning its relationship with affiliate apps.
