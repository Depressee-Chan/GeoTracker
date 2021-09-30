# Tracker
A simple little webpage that locates a client's coords. Coords are send back to the server and stored in a database where they can be retrieved if a client shares their QR code so that others can have realtime access to their geolocation.

## How to use
In order to set up the server, simply delete any databases within the same directory as the server files that have the name "userLocation.db". Then run the file "app.py" and a new database for user location data will be generated. The default port for hosting pages is port 80 but it can be changes at the bottom of the app.py file. 
