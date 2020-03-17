# flask & kdb 

A repo designed to show the multiple ways you can integrate flask and kdb together using websockets. I have used two ways a KDB connection can be ultized within the flask framework.

## 1. Passing q/KDB DB connections across flask requests

The first method is uses a persistant DB connection object that can be imported when required. I implemented this from this answer from [toppatopvt on StackOverflow](https://stackoverflow.com/a/55537278)

### chart_flask - Details

* kdb connection is opened by using Websockets ( functions found in kdb.py )
* DB object created within extensions.py file
* Connection object is imported when flask is started (found in  app/__init__.py )
* kdb.get_db() can be called to obtain the object's current ws connection ( see main/routes.py chart_flask )
    * It will attempt to reconnect if the WS connection drops
    * I have just send a simple string message that is simply returned via kdb

### End Result

![method1](https://user-images.githubusercontent.com/32989131/76908370-69f5e480-68a0-11ea-8e42-ec459308bdd8.PNG)

## 2. Passing KDB Connection details via jinja2 / js

The second method is done by passing connection details to the webpage via jinja2 and using js websockets to connect.

### chart_kdb - Details

* The connection details are passed via a jinja2 data object to the html page. ( see main/routes.py chart_kdb )
* This is then passed into the JS function named connect (( taken from KX WebSocket Whitepaper)[https://code.kx.com/q/wp/websockets/]) 
    * Also defines the onmessage function.
* In my example, I've used a button (Click me) that sends a message to the KDB server and returns a JSON message back
* The data is then used to generate a chart using chart.js
* data is compared with data sent via jinja2 in same flask request

### End Result

![method2](https://user-images.githubusercontent.com/32989131/76908431-901b8480-68a0-11ea-89b3-19a26231fccb.PNG)

## Improvements and Ideas?

1. You could implement both methods concurrently, 
    * The first request can be sent to a index server using method one to retrieve dedicated gateway host & port information
    * Pass this info to webpage via method 2 to allow the user to have dedicated gateway to query the underlying kdb db

