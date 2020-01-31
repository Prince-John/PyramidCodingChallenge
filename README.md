# PyramidCodingChallenge
A python flask based webservice that tells if a string is pyramid word.

This program requires python 3 with flask, flask-RESTful packeges to run. 


To run the program through the console you need to have python as a path variable. 
Once the program runs, it starts the webservice on the localhost at port 5000. 

This API can be queried by passing the word as a string get request in the following url format:
         `https://localhost:5000/pyramid/api/<InputText>`
This API returns the a boolean json object as a result.  

**Error Handeling:**
Current version of the program does not check for input type and expects a string without any special characters or numbers. 
