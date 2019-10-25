#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 15:02:03 2019

@author: gus
"""
import urllib.request
import os
import sys
import json
from termcolor import colored
import time
from selenium import webdriver
import unittest
from selenium.webdriver.chrome.options import Options
import datetime
from datetime import datetime
#from selenium.webdriver.Firefox.options import Options

def api_request_and_vars():
    ## Trace the ISS - earth.orbital space station
    eoss = 'http://api.open-notify.org/iss-now.json'
    #Call the webserver
    trackiss = urllib.request.urlopen(eoss)
    #put into file object
    ztrack = trackiss.read()
    #json 2 python data structure
    result = json.loads(ztrack.decode('utf-8'))
    #display our pythonic data
    location = result['iss_position']#from 'result variable, obtain the tag 'iss_possition' into a list
    timesStamp = result['timestamp']
    message = result['message']
    global lat, lon, comma, space, lines #these functions can be called from another function
    lat = location['latitude']
    lon = location['longitude']
    lat = str(lat)
    lon = str(lon)
    now = datetime.now()
    yymmday = '%s-%s-%s' % (now.year, now.month, now.day)
    hhmmss = '%s:%s:%s' % (now.hour, now.minute, now.second) 
    todayis = (str(yymmday)+"-"+str(hhmmss))
    minutes = round(timesStamp/60)
    hours = round(minutes/60)
    day = round(hours/24)
    weeks = round(day/7)
    months = round(day/30)
    years = round(months/12)
    comma = ","
    space = " "
    hashtags = ("#################################################")
    lines = ("-------------------------------------------------")
    log = open('iss_tracker.log', 'a')
    print(result)
    log.write('\n'+hashtags)
    log.write('\n'+"Actual date and time: "+todayis)
    print(colored(lines, 'cyan'))
    log.write('\n'+hashtags)
    print(colored('Hours: '+str(hours)+' Minutes: '+str(minutes), 'white'))
    log.write('\n'+'Hours: '+str(hours)+' Minutes: '+str(minutes))
    print(colored('Actual Timestamp: '+str(timesStamp)+" in seconds", 'white'))
    log.write('\n'+(lines))
    log.write('\n'+"Actual Timestamp: "+str(timesStamp)+" in seconds")
    log.write('\n'+(lines))
    print(colored(lines, 'cyan'))
    log.write('\n'+'Latitude: '+str(lat))
    print(colored('Latitude: '+str(lat) ,'green'))
    log.write('\n'+(lines))
    print(colored(lines, 'cyan'))
    print(colored('Longitude: '+str(lon), 'magenta',))
    log.write('\n'+'Longitude: '+str(lon))
    print(colored(lines, 'cyan'))
    log.write('\n'+(lines))
    print(colored('Message: '+ message, 'yellow',))
    log.write('\n'+'Message: '+ message)
    pass
    
def timenow():
    global todayis, todaysdate, yymmday #these functions can be called from another function
    now = datetime.now()
    yymmday = '%s-%s-%s' % (now.year, now.month, now.day)
    hhmmss = '%s:%s:%s' % (now.hour, now.minute, now.second) 
    todayis = (str(yymmday)+"-"+str(hhmmss))
    print("Today is: "+str(yymmday)+" "+str(hhmmss))
    pass

def selenium_code_screenshots():
    loop = 11
    while(loop==11):
        print("Enter amount of seconds to refresh the coordinates from the API.")
        sleep_time = input("Minimum recommended is 5...")
        if not sleep_time.isdigit():
                lines = ("-------------------------------------------------")
                print(colored(lines, 'cyan'))
                print("Please only enter numbers here!")

        else:
            for number in range(amount_of_repetitions,0,-1):
                lines = ("-------------------------------------------------")
                print(colored(lines, 'cyan'))
                print("Amount of remaining iterations: "+str(number))
                lines = ("-------------------------------------------------")
                print(colored(lines, 'cyan'))
                print("Refresh interval in seconds set to: "+str(sleep_time))
                print(colored(lines, 'cyan'))
                print("\n\nShowing ISS coordinates")
                timenow()
                print(colored(lines, 'cyan'))
                api_request_and_vars()
                driver.find_element_by_xpath('//*[@id="searchboxinput"]').send_keys(lat+comma+space+lon)
                driver.find_element_by_xpath('//*[@id="searchbox-searchbutton"]').click()
                lines = ("-------------------------------------------------")
                print(colored(lines, 'cyan'))
                cwd = os.getcwd()
                path = cwd
                for remaining_seconds in range(int(sleep_time),0,-1):
                    print(colored("Refreshing in: " +str(remaining_seconds), 'red'))
                    time.sleep(1)
                    if remaining_seconds == 1:
                        lines = ("-------------------------------------------------")
                        print(colored(lines, 'cyan'))
                        name_and_path_to_screenshots = (datepath+"/"+str(number)+"-ISS"+"-"+str(todayis)+".png")
                        driver.save_screenshot(name_and_path_to_screenshots)
                        print("The screenshot was saved to: " + name_and_path_to_screenshots)
                        print(colored(lines, 'cyan'))
                        if number == 1:
                            print(colored(lines, 'cyan'))
                            print("Program finished, returning to main menu...")
                            main_program_function()
                        else:
                            print("Waiting other 5 seconds to process picture in path...")
                            for remaining_seconds in range(5,0,-1):
                                print(colored(lines, 'cyan'))
                                print(colored("Refreshing in: " +str(remaining_seconds), 'red'))
                                time.sleep(1)
                                if remaining_seconds == 1:
                                    driver.find_element_by_xpath('//*[@id="searchboxinput"]').clear()

                                elif number == 1:
                                    print(colored(lines, 'cyan'))
                                    print("Program finished, returning to main menu...")
                                    main_program_function()

                                elif remaining_seconds < 1:
                                    print(colored(lines, 'cyan'))
                                    print("Program finished, returning to main menu...")
                                    main_program_function()
                                    pass
            
        
    
def google_maps_coordinates():
    loop = 4
    while(loop==4):
        lines = ("-------------------------------------------------")
        print(colored(lines, 'cyan'))
        print("b - Get back to main menu.")
        print("c - Proceed with above selection and launch ISS tracker program.")
        print(colored(lines, 'cyan'))
        back_to_main = input("Please select a letter from the menu and press enter...")
        b = "b"
        c = "c"
        if back_to_main == b:
            main_program_function()
        elif back_to_main == c:
            print("\n")
            print("Google Maps Module accessed.")
            print("Triggering selenium webdriver to open browser...")
            global driver
            driver = webdriver.Firefox()
            #driver = webdriver.Chrome()
            driver.get("https://maps.google.com")
            print(colored(lines, 'cyan'))
            print("Working directory is:")
            pwd = os.system("pwd")
            print(colored(lines, 'cyan'))
            loop = 5
            while(loop==5):
                global amount_of_repetitions
                amount_of_repetitions = input("Enter the amount of iterations to calculate coordinates...")
                if not amount_of_repetitions.isdigit():
                    print(colored(lines, 'cyan'))
                    print("Please only enter numbers here!")
                    loop = 5

                else:
                    amount_of_repetitions = int(amount_of_repetitions)
                    print(colored(lines, 'cyan'))
                    global number
                    for number in range(amount_of_repetitions,0,-1):
                        if number == 1:
                            print(colored(lines, 'cyan'))
                            print("Program terminated, returning to main menu again.")
                            print(colored(lines, 'cyan'))
                            main_program_function()
                            
                        elif number >1 :
                            selenium_code_screenshots()

        else:
            print(colored(lines, 'cyan'))
            print("Please only enter either 'b' or 'c'!")
            print(colored(lines, 'cyan'))
            time.sleep(1)
            loop = 4
            pass

def main_program_function():
    loop = 1
    while(loop==1):
        hashtags = ("#################################################")
        global lines
        lines = ("-------------------------------------------------")
        print(colored(hashtags, 'cyan'))
        print(colored("WELCOME TO THE ISS TRACKER PROGRAM.", 'green'))
        print(colored(hashtags, 'cyan'))
        print("This program will track and show the actual coordinates")
        print("of the International space station on google maps, and take screenshots")
        print("to a specified path in your system.")
        print(colored(hashtags, 'cyan'))
        print(colored(lines, 'cyan'))
        loop = 2
        while(loop==2):
            
            menu_selection = input("Press enter to start program...")
                

            if len(menu_selection) > 0:
                print(colored(lines, 'cyan'))
                print(colored("Only press enter please!", 'red'))
                print(colored(lines, 'cyan'))
                time.sleep(1)
                
            elif len(menu_selection) == 0:
                try:
                    global cwd, path, create_folder, datepath
                    cwd = os.getcwd()
                    path = cwd
                    now = datetime.now()
                    yymmday = '%s-%s-%s' % (now.year, now.month, now.day)
                    create_folder = str(yymmday)
                    datepath = (path+"/"+create_folder)
                    print("Current working directory is: "+cwd)
                    os.mkdir(datepath)
                    print(colored(hashtags, 'cyan'))
                    print ("Successfully created the directory "+datepath)
                    print("The screenshots of the ISS location will be")
                    print("stored in the path created above")
                    google_maps_coordinates()
                                
                except:
                    cwd = os.getcwd()
                    path = cwd
                    create_folder = str(yymmday)
                    datepath = (path+"/"+create_folder)
                    if datepath == (cwd+"/"+create_folder):
                        print(colored(hashtags, 'cyan'))
                        print("Cannot create the directory as it already exists")
                        print("The screenshots of the ISS location will be")
                        print("in the existing path: "+path+"/"+create_folder)
                        google_maps_coordinates()

        
main_program_function()
            
    

               
                                                    


