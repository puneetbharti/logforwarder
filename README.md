# logforwarder

####Technologies used
* Python: for log forwarding 
* Nodejs: Apis for input and output 
* Elasticsearch: as a data store

## Assumptions
****
* Python script is used to pick logs and send it to an api 
* Data loss in the program is not considered
* Limited conditional check on the api as well as on the forwarder script.
* Python script will run as a daemon through upstart.
 
****

#### local setup nodejs 
* go to the directory /api
* execute ```npm install ```
* execute ```node app.js```

#### Python setup 
* go to directory /forwarder
* execute ```python forwarder.py``` 

#### Upstart script 
* copy file forwarder.conf to /etc/init/
* make sure the path of the python script is specified correctly.
* execute ```sudo start forwarder```


