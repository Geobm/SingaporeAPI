# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 16:30:44 2020

@author: Geovani BM
"""
import requests
import csv
import datetime
import pandas as pd

def getURLS(date_format):
    #Filtrate by specific camera
    req_camera_id = '1701'
    global times
    image=[]
    time =[]
    for i in range(len(date_format)):
        url_date = date_format[i].replace('/','-') #Adjust timestamps to correct url format
        endpoint = "https://api.data.gov.sg/v1/transport/traffic-images?date_time="+url_date
        data = requests.get(endpoint)
        if (data):
            data = requests.get(endpoint).json()    
            for item in data['items']:
                for cam in item['cameras']:
                    camera_id = cam['camera_id']
                    if camera_id == req_camera_id:	
                        image = cam['image']
                        wanted_cam.append(camera_id)
                        wanted_url.append(image)
                        time.append(cam['timestamp'])
                        print(times[i])
                        with open('/home/sutd/Downloads/cam1701/Wed11-13-19.csv','w',newline='') as f: #Choose your own path
                            writer = csv.writer(f)
                            writer.writerows(zip(wanted_cam, wanted_url, times))
    df = pd.read_csv('/home/sutd/Downloads/cam1701/Wed11-13-19.csv', header=None)
    df.rename(columns={0: 'Cam_id', 1: 'Image', 2: 'Timestamp_sg_time'}, inplace=True)
    df.to_csv('/home/sutd/Downloads/cam1701/Wed11-13-19.csv', index=False) # save csv file
            
if __name__ == "__main__":    
    string_date_list = []   
    #Generate timestamps every N minutes. Parameters can be modified  
    initial_time = datetime.datetime(2019, 11, 13, 0, 0)
    final_time = datetime.datetime(2019, 11, 14, 0, 0)
    delta = datetime.timedelta(minutes=10) 
    times = []
    wanted_url=[]
    wanted_cam=[]
    endpoints =[]
    data_lists =[]
    
    while initial_time < final_time:
        times.append(initial_time)
        initial_time += delta
     
    for i in range(len(times)): #Convert datetime objects to string list    
        string_date_list.append((times[i].strftime('%Y/%m/%dT%H:%M:%S')))
    getURLS(string_date_list)
