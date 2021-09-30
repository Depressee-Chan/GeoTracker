# Tracker
A simple little webpage that locates a client's coords. Coords are send back to the server and stored in a database where they can be retrieved if a client shares their QR code so that others can have realtime access to their geolocation.

## How to use
In order to set up the server, simply delete any databases within the same directory as the server files that have the name ```userLocation.db```. Then run the file ```app.py``` and a new database for user location data will be generated. The default port for hosting pages is ```port 80``` but it can be changes at the bottom of the app.py file. In order to fully prepare the server to recieve data from the webpages, you need to change the IP/Domain for the ```data``` variable on ```line 92``` (index.html) and ```line 45``` (viewing.html) to the IP/Domain of the server running the application. Do not forget to add the ```/v/``` at the end of the IP/Domain or the data will send to the wrong web path.
