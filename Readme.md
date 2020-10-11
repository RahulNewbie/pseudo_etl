Welcome to Pseudo ETL Project

***Used Python and pip Version***

python 3.8

pip version 19.3.1

***Install Dependency***

pip install -r requirements.txt

***Database Install***

I have tested it in windows 10 environment and installed PostgreSQL 13.

I have made database.ini file to put all PostgreSQL params and used it to connect
the database

ini file contains:

host=localhost<br/>
database=postgres<br/>
user=postgres<br/>
password=123<br/>
port=5433<br/>

Please change the host, port, user and password according to your installation

***Simulator***

Simulator will generate a new record everytime, when source parameter is simulator.
It will generate a single record and either show up in the console or get inserted into the database
according to sink parameter

Structure of the generated data is :

{"key": "A123", "value":"15.6", "ts":'2020-10-07 13:28:43.399620+02:00'} 


***File of Json Array***

I have made a json file file.json, which contains array of json objects.

For the testing purpose I am using this file read scenario. This scenario will be reading the
file content and transmit the data one by one to sink.

As proper format of the file was not given, so i have used my creativity 
to design the file as a json file.


***Run the Application***

Run the application using the following statement

python application.py \<source_param\> \<sink_param\>

source_param can be simulator and file

sink_param can be console and database

***Example command to run the application***

1. If the source is simulator and sink is console
    ```
    python application.py simulator console
    ```
    
2. If the source is simulator and sink is database
    ```
    python application.py simulator database
    ```
3. If the source is file and sink is console
    ```
    python application.py file console
    ```
4. If the source is file and sink is database
    ```
    python application.py file database
    ```








