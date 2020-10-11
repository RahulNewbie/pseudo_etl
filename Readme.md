Welcome to Pseudo ETL Project

***Used Python Version***

python 3.8

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








