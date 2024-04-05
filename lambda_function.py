import json
import requests
import mysql.connector

def lambda_handler(event, context):
    response = requests.get('http://api.open-notify.org/iss-now.json')
    response_data = response.json()
    latitude = response_data['iss_position']['latitude']
    longitude = response_data['iss_position']['longitude']
    timestamp = response_data['timestamp']
    message = response_data['message']

    connection = mysql.connector.connect(
    host="databasefinalproject.cdm2yygckc11.us-east-1.rds.amazonaws.com",
    user="admin",
    password=" ",
    database="finalcapstone"
    )
    cursor = connection.cursor()
    try:
        query="""CREATE TABLE if not exists space_station (latitudes float, longitudes float, Timestamp integer, message text)"""
        cursor.execute(query)
        print("Table created")
    except:
         print("Table already exists")
        
    connection.commit()
    try:
        insert_query="""INSERT INTO space_station (latitudes, longitudes, Timestamp, message) VALUES (%s, %s, %s, %s)"""
        cursor.execute(insert_query, (latitude, longitude, timestamp, message))
        print("Data Inserted..")
    except:
        print("Data insertion is unsuccessful..")
    cursor.close()
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
        }