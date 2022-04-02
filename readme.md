Programming Assignment 3
1. run 'mongod' in terminal and 'mongo' in a different terminal after 
establishing a connection in mongodb compass
2. change app.config according to the mongoDB localhost of your system
and do add the database name after '/' (as mentioned below) where all 
the parsed data is dumped (or you can leave it as is, since the URI is
same for all mongodb by default)
app.config["MONGO_URI"] = "mongodb://localhost:27017/webAPIs"
3. run main.py file which runs parse.py to parse the text files 
into mongoDB compass
4. keep template folder which has home.html, index.html on the same 
level as main.py, parse.py, api.txt and mashup.txt
5. open the URL http://127.0.0.1:5000 as prompted
6. enter the filters (fields are case sensitive except for keywords in 
queries 3 and 4)
7. please refrain from using ',' when entering multiple keywords.
Seperate the words using white space