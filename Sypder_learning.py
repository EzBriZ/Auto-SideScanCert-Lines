# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 18:45:26 2024

@author: carter.d.smith
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Overarching project to allow for an input of kml target file,
#given parameters of  SSS certification spacing, what length of
#lines you want, and if you want them rotated - exports a Hypack .lnw 
#CarterSmith#
#July2024

#currently only works for NAD83(2011) / UTM zone 17N

#import pyKML

#parser tool from pykml library
from pykml import parser

#import suite of libraries to convert between reference systems and do math on the points
import geopy
import geopy.distance
import math
from math import sqrt
import utm

#import os to control file writing and reading
import os

#import for button making
import tkinter as tk
from tkinter import filedialog, Label, simpledialog, messagebox

#initialize variable to test for button1 (browse) being executed before button2 (convert)
button1_executed = False

#function to allow user to find kml file they want to convert
def browse_kml():
    #intialize global variables for later use
    global all_coordinates
    global file_path
    global button1_executed

    #ask user to select kml file
    file_path = filedialog.askopenfilename(title="Select KML File", filetypes=[("KML Files", "*.kml")])
    
    #if they select a kml, open file and...
    if file_path:
        try:
            #open and read KML file (binary)
            with open(file_path, 'rb') as file:
                    kml_content = file.read()
                    
            #parse through file
            root = parser.fromstring(kml_content)
            
            #create list to store all coordinates
            all_coordinates = []
            
            #search through folders for ones with coordinates
            for folder in root.Document.Folder:
                if hasattr(folder, 'Placemark'):
                    for placemark in folder.Placemark:
                        if hasattr(placemark, 'Point') and hasattr(placemark.Point, 'coordinates'):
                            
                            #strip text (coordinates)
                            coordinates = placemark.Point.coordinates.text.strip()
                            
                            #seperate Long and Lat into seperate columns
                            coordinates = coordinates.split(',')
                            
                            #compile coordinates into list as function iterates through all 
                            all_coordinates.append(coordinates)
                            
                            #label to show file has been changed
                            label.config(text=f"File chosen: {file_path}")
                            
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            
    #store whether this button has been executed to test for right order of operations when calling button2
    button1_executed = True

#function taking an input (will do math if 50,75, or 100) that then calculates and converts necessary endpoints for SSS lines being created
def spacing():

    #variable to prompt user and record input
    number = simpledialog.askinteger("Input", "Enter (50, 75, or 100):")
    
    #test if number is entered correctly
    if number is None:
        label.config(text="Operation Cancelled")
        return
    
    elif number not in (50, 75, 100):
        messagebox.showerror("Error", "Now you know that number weren't right")
        return
    
    #throw error if trying to execute button 2 without first executing button 1
    if not button1_executed:
        #label to show file has been changed
        label.config(text="Error, ensure you have browsed to file")
    
    #set desired lenght of lines
    length = simpledialog.askstring("Line Length", "Enter desired line length")
    
    #test if length entered correctly
    if length is None:
        label.config(text="Operation Cancelled")
        return
    
    #If something is entered, try converting to float. Else, throw flag
    try:
        length = float(length)
    except ValueError:
        label.config(text="Error, length needs to be a number")
        return
        
    #set desired rotation (as string so even no value returns 0)
    rotation = simpledialog.askstring("Degrees", "Enter desired rotation")
    
    #if no answer or cancel is used, rotation set to 0
    if rotation is None:
        label.config(text="Operation Cancelled")
        return
    
    #if no value is given, set rotation to 0
    if rotation.strip() =="":
        rotation = 0
    else:
        messagebox.showerror("Error","Input given not an integer")
        return
    
    

    #determine number of lines being written to use in creating .txt file -- Might need to go after append coordinates in order to convert number to string for writing output
    endlength= len(all_coordinates)*12
    #turn that number into string for writing to file
    endlength_str = f"{endlength}"
    #print(endlength)
    combined_list = []

    #loop through target coordinates to grab and store "start points" from which to math
    for x in all_coordinates:
        long = x[0]
        lat = x[1]
    
        start_point = geopy.Point(lat,long)
        #print(start_point)
    
    #-----------------------------------------------------------------------------------------------------------
        if number == 100:
            
        #Calculate positions of new point for 15m line North 
            distance_m15 = sqrt(length**2 + 15**2) 
            bearing1N15 = math.degrees(math.atan(length/15)) + rotation
            bearing2N15 = 360 - (math.degrees(math.atan(length/15))) + rotation
            
            #Create Northern East and West points for 15m line
            WNpoint15 = geopy.distance.geodesic(meters=distance_m15).destination(start_point, bearing1N15)
            ENpoint15 = geopy.distance.geodesic(meters=distance_m15).destination(start_point, bearing2N15)
            
            #Create Southern East and West points for 15m line
            bearing1S15 = 180 + (math.degrees(math.atan(length/15))) + rotation
            bearing2S15 = 180 - (math.degrees(math.atan(length/15))) + rotation
            
            WSpoint15 = geopy.distance.geodesic(meters=distance_m15).destination(start_point, bearing1S15)
            ESpoint15 = geopy.distance.geodesic(meters=distance_m15).destination(start_point, bearing2S15)
            
            #print(WNpoint15.latitude, WNpoint15.longitude)
            #print(ENpoint15.latitude, ENpoint15.longitude)
            #print(WSpoint15.latitude, WSpoint15.longitude)
            #print(ESpoint15.latitude, ESpoint15.longitude)
    
            #Create Western North and South points for 15m line
            bearing1W15 = 270 + (math.degrees(math.atan(length/15))) + rotation
            bearing2W15 = 270 - (math.degrees(math.atan(length/15))) + rotation
            
            NWpoint15 = geopy.distance.geodesic(meters=distance_m15).destination(start_point, bearing1W15)
            SWpoint15 = geopy.distance.geodesic(meters=distance_m15).destination(start_point, bearing2W15)
            
            #Create Eastern North and South points for 15m line
            bearing1E15 = 90 + (math.degrees(math.atan(length/15))) + rotation
            bearing2E15 = 90 - (math.degrees(math.atan(length/15))) + rotation
            
            NEpoint15 = geopy.distance.geodesic(meters=distance_m15).destination(start_point, bearing1E15)
            SEpoint15 = geopy.distance.geodesic(meters=distance_m15).destination(start_point, bearing2E15)
            
            #print(NWpoint15.latitude, NWpoint15.longitude)
            #print(SWpoint15.latitude, SWpoint15.longitude)
            #print(NEpoint15.latitude, NEpoint15.longitude)
            #print(SEpoint15.latitude, SEpoint15.longitude)
            
        #Calc for points 50m North
            distance_m50 = sqrt(length**2 + 50**2)
            bearing1N50 = math.degrees(math.atan(length/50)) + rotation
            bearing2N50 = 360 - (math.degrees(math.atan(length/50))) + rotation
            
            #Create East and West points for 50m spacing North 
            WNpoint50 = geopy.distance.geodesic(meters=distance_m50).destination(start_point, bearing1N50)
            ENpoint50 = geopy.distance.geodesic(meters=distance_m50).destination(start_point, bearing2N50)
            
            #Create Southern East and West points for 50m line
            bearing1S50 = 180 + (math.degrees(math.atan(length/50))) + rotation
            bearing2S50 = 180 - (math.degrees(math.atan(length/50))) + rotation
            
            WSpoint50 = geopy.distance.geodesic(meters=distance_m50).destination(start_point, bearing1S50)
            ESpoint50 = geopy.distance.geodesic(meters=distance_m50).destination(start_point, bearing2S50)
            
            #print(WNpoint50.latitude, WNpoint50.longitude)
            #print(ENpoint50.latitude, ENpoint50.longitude)
            #print(WSpoint50.latitude, WSpoint50.longitude)
            #print(ESpoint50.latitude, ESpoint50.longitude)
            
            #Create Western North and South points for 50m line
            bearing1W50 = 270 + (math.degrees(math.atan(length/50))) + rotation
            bearing2W50 = 270 - (math.degrees(math.atan(length/50))) + rotation
            
            NWpoint50 = geopy.distance.geodesic(meters=distance_m50).destination(start_point, bearing1W50)
            SWpoint50 = geopy.distance.geodesic(meters=distance_m50).destination(start_point, bearing2W50)
            
            #Create Eastern North and South points for 50m line
            bearing1E50 = 90 + (math.degrees(math.atan(length/50))) + rotation
            bearing2E50 = 90 - (math.degrees(math.atan(length/50))) + rotation
            
            NEpoint50 = geopy.distance.geodesic(meters=distance_m50).destination(start_point, bearing1E50)
            SEpoint50 = geopy.distance.geodesic(meters=distance_m50).destination(start_point, bearing2E50)
            
            #print(NWpoint50.latitude, NWpoint50.longitude)
            #print(SWpoint50.latitude, SWpoint50.longitude)
            #print(NEpoint50.latitude, NEpoint50.longitude)
            #print(SEpoint50.latitude, SEpoint50.longitude)
    
    
        #Calc for points 85m North
            distance_m85 = sqrt(length**2 + 85**2)
            bearing1N85 = math.degrees(math.atan(length/85)) + rotation
            bearing2N85 = 360 - (math.degrees(math.atan(length/85))) + rotation
            
            #Create East and West points for 85m spacing North 
            WNpoint85 = geopy.distance.geodesic(meters=distance_m85).destination(start_point, bearing1N85)
            ENpoint85 = geopy.distance.geodesic(meters=distance_m85).destination(start_point, bearing2N85)
    
            #Create Southern East and West points for 85m line
            bearing1S85 = 180 + (math.degrees(math.atan(length/85))) + rotation
            bearing2S85 = 180 - (math.degrees(math.atan(length/85))) + rotation
    
            WSpoint85 = geopy.distance.geodesic(meters=distance_m85).destination(start_point, bearing1S85)
            ESpoint85 = geopy.distance.geodesic(meters=distance_m85).destination(start_point, bearing2S85)
    
            #print(WNpoint85.latitude, WNpoint85.longitude)
            #print(ENpoint85.latitude, ENpoint85.longitude)
            #print(WSpoint85.latitude, WSpoint85.longitude)
            #print(ESpoint85.latitude, ESpoint85.longitude)
            
            #Create Western North and South points for 85m line
            bearing1W85 = 270 + (math.degrees(math.atan(length/85))) + rotation
            bearing2W85 = 270 - (math.degrees(math.atan(length/85))) + rotation
            
            NWpoint85 = geopy.distance.geodesic(meters=distance_m85).destination(start_point, bearing1W85)
            SWpoint85 = geopy.distance.geodesic(meters=distance_m85).destination(start_point, bearing2W85)
            
            #Create Eastern North and South points for 85m line
            bearing1E85 = 90 + (math.degrees(math.atan(length/85))) + rotation
            bearing2E85 = 90 - (math.degrees(math.atan(length/85))) + rotation
            
            NEpoint85 = geopy.distance.geodesic(meters=distance_m85).destination(start_point, bearing1E85)
            SEpoint85 = geopy.distance.geodesic(meters=distance_m85).destination(start_point, bearing2E85)
            
            #print(NWpoint85.latitude, NWpoint85.longitude)
            #print(SWpoint85.latitude, SWpoint85.longitude)
            #print(NEpoint85.latitude, NEpoint85.longitude)
            #print(SEpoint85.latitude, SEpoint85.longitude)
            
            #store endpoints for SSS lines 
            ToUTMList = [WNpoint15, ENpoint15, WSpoint15, ESpoint15, NWpoint15, SWpoint15, NEpoint15, SEpoint15, WNpoint50, ENpoint50, WSpoint50, ESpoint50, NWpoint50, SWpoint50, NEpoint50, SEpoint50, WNpoint85, ENpoint85, WSpoint85, ESpoint85, NWpoint85, SWpoint85, NEpoint85, SEpoint85]

    
    #-----------------------------------------------------------------------------------------------------------
    
        elif number == 75:
            
        #Calculate positions of new point for 11.25m line North 
            distance_m1125 = sqrt(length**2 + 11.25**2)
            bearing1N1125 = math.degrees(math.atan(length/11.25)) + rotation
            bearing2N1125 = 360 - (math.degrees(math.atan(length/11.25))) + rotation
            
            #Create Northern East and West points for 11.25m line
            WNpoint1125 = geopy.distance.geodesic(meters=distance_m1125).destination(start_point, bearing1N1125)
            ENpoint1125 = geopy.distance.geodesic(meters=distance_m1125).destination(start_point, bearing2N1125)
            
            #Create Southern East and West points for 11.25m line
            bearing1S1125 = 180 + (math.degrees(math.atan(length/11.25))) + rotation
            bearing2S1125 = 180 - (math.degrees(math.atan(length/11.25))) + rotation
            
            WSpoint1125 = geopy.distance.geodesic(meters=distance_m1125).destination(start_point, bearing1S1125)
            ESpoint1125 = geopy.distance.geodesic(meters=distance_m1125).destination(start_point, bearing2S1125)
            
            #print(WNpoint1125.latitude, WNpoint1125.longitude)
            #print(ENpoint1125.latitude, ENpoint1125.longitude)
            #print(WSpoint1125.latitude, WSpoint1125.longitude)
            #print(ESpoint1125.latitude, ESpoint1125.longitude)
              
            #Create Western North and South points for 11.25 line
            bearing1W1125 = 270 + (math.degrees(math.atan(length/11.25))) + rotation
            bearing2W1125 = 270 - (math.degrees(math.atan(length/11.25))) + rotation
            
            NWpoint1125 = geopy.distance.geodesic(meters=distance_m1125).destination(start_point, bearing1W1125)
            SWpoint1125 = geopy.distance.geodesic(meters=distance_m1125).destination(start_point, bearing2W1125)
            
            #Create Eastern North and South points for 11.25 line
            bearing1E1125 = 90 + (math.degrees(math.atan(length/11.25))) + rotation
            bearing2E1125 = 90 - (math.degrees(math.atan(length/11.25))) + rotation
            
            NEpoint1125 = geopy.distance.geodesic(meters=distance_m1125).destination(start_point, bearing1E1125)
            SEpoint1125 = geopy.distance.geodesic(meters=distance_m1125).destination(start_point, bearing2E1125)
            
            #print(NWpoint1125.latitude, NWpoint1125.longitude)
            #print(SWpoint1125.latitude, SWpoint1125.longitude)
            #print(NEpoint1125.latitude, NEpoint1125.longitude)
            #print(SEpoint1125.latitude, SEpoint1125.longitude)
            
        #Calculate positions for 37.5m line North 
            distance_m375 = sqrt(length**2 + 37.5**2)
            bearing1N375 = math.degrees(math.atan(length/37.5)) + rotation
            bearing2N375 = 360 - (math.degrees(math.atan(length/37.5))) + rotation
            
            #Create Northern East and West points for 37.5m line
            WNpoint375 = geopy.distance.geodesic(meters=distance_m375).destination(start_point, bearing1N375)
            ENpoint375 = geopy.distance.geodesic(meters=distance_m375).destination(start_point, bearing2N375)
            
            #Create Southern East and West points for 37.5m line
            bearing1S375 = 180 + (math.degrees(math.atan(length/37.5))) + rotation
            bearing2S375 = 180 - (math.degrees(math.atan(length/37.5))) + rotation
            
            WSpoint375 = geopy.distance.geodesic(meters=distance_m375).destination(start_point, bearing1S375)
            ESpoint375 = geopy.distance.geodesic(meters=distance_m375).destination(start_point, bearing2S375)
            
            #print(WNpoint375.latitude, WNpoint375.longitude)
            #print(ENpoint375.latitude, ENpoint375.longitude)
            #print(WSpoint375.latitude, WSpoint375.longitude)
            #print(ESpoint375.latitude, ESpoint375.longitude)
            
            #Create Western North and South points for 37.5m line
            bearing1W375 = 270 + (math.degrees(math.atan(length/37.5))) + rotation
            bearing2W375 = 270 - (math.degrees(math.atan(length/37.5))) + rotation
            
            NWpoint375 = geopy.distance.geodesic(meters=distance_m375).destination(start_point, bearing1W375)
            SWpoint375 = geopy.distance.geodesic(meters=distance_m375).destination(start_point, bearing2W375)
            
            #Create Eastern North and South points for 37.5m line
            bearing1E375 = 90 + (math.degrees(math.atan(length/37.5))) + rotation
            bearing2E375 = 90 - (math.degrees(math.atan(length/37.5))) + rotation
            
            NEpoint375 = geopy.distance.geodesic(meters=distance_m375).destination(start_point, bearing1E375)
            SEpoint375 = geopy.distance.geodesic(meters=distance_m375).destination(start_point, bearing2E375)
            
            #print(NWpoint375.latitude, NWpoint375.longitude)
            #print(SWpoint375.latitude, SWpoint375.longitude)
            #print(NEpoint375.latitude, NEpoint375.longitude)
            #print(SEpoint375.latitude, SEpoint375.longitude)
            
        #Calculate positions for 63.75m line North 
            distance_m6375 = sqrt(length**2 + 63.75**2)
            bearing1N6375 = math.degrees(math.atan(length/63.75)) + rotation
            bearing2N6375 = 360 - (math.degrees(math.atan(length/63.75))) + rotation
            
            #Create Northern East and West points for 63.75m line
            WNpoint6375 = geopy.distance.geodesic(meters=distance_m6375).destination(start_point, bearing1N6375)
            ENpoint6375 = geopy.distance.geodesic(meters=distance_m6375).destination(start_point, bearing2N6375)
            
            #Create Southern East and West points for 63.75m line
            bearing1S6375 = 180 + (math.degrees(math.atan(length/63.75))) + rotation
            bearing2S6375 = 180 - (math.degrees(math.atan(length/63.75))) + rotation
            
            WSpoint6375 = geopy.distance.geodesic(meters=distance_m6375).destination(start_point, bearing1S6375)
            ESpoint6375 = geopy.distance.geodesic(meters=distance_m6375).destination(start_point, bearing2S6375)
            
            #print(WNpoint6375.latitude, WNpoint6375.longitude)
            #print(ENpoint6375.latitude, ENpoint6375.longitude)
            #print(WSpoint6375.latitude, WSpoint6375.longitude)
            #print(ESpoint6375.latitude, ESpoint6375.longitude)    
            
            #Create Western North and South points for 63.75m line
            bearing1W6375 = 270 + (math.degrees(math.atan(length/63.75))) + rotation
            bearing2W6375 = 270 - (math.degrees(math.atan(length/63.75))) + rotation
            
            NWpoint6375 = geopy.distance.geodesic(meters=distance_m6375).destination(start_point, bearing1W6375)
            SWpoint6375 = geopy.distance.geodesic(meters=distance_m6375).destination(start_point, bearing2W6375)
            
            #Create Eastern North and South points for 63.75m line
            bearing1E6375 = 90 + (math.degrees(math.atan(length/63.75))) + rotation
            bearing2E6375 = 90 - (math.degrees(math.atan(length/63.75))) + rotation
            
            NEpoint6375 = geopy.distance.geodesic(meters=distance_m6375).destination(start_point, bearing1E6375)
            SEpoint6375 = geopy.distance.geodesic(meters=distance_m6375).destination(start_point, bearing2E6375)
            
            #print(NWpoint6375.latitude, NWpoint6375.longitude)
            #print(SWpoint6375.latitude, SWpoint6375.longitude)
            #print(NEpoint6375.latitude, NEpoint6375.longitude)
            #print(SEpoint6375.latitude, SEpoint6375.longitude)
            
            #store endpoints for SSS lines 
            ToUTMList = [WNpoint1125, ENpoint1125, WSpoint1125, ESpoint1125, NWpoint1125, SWpoint1125, NEpoint1125, SEpoint1125, WNpoint375, ENpoint375, WSpoint375, ESpoint375, NWpoint375, SWpoint375, NEpoint375, SEpoint375, WNpoint6375, ENpoint6375, WSpoint6375, ESpoint6375, NWpoint6375, SWpoint6375, NEpoint6375, SEpoint6375]

    
    #-----------------------------------------------------------------------------------------------------------

        elif number == 50:
    
        #Calculate positions of new point for 7.5m line North 
            distance_m75 = sqrt(length**2 + 7.5**2)
            bearing1N75 = math.degrees(math.atan(length/7.5)) + rotation
            bearing2N75 = 360 - (math.degrees(math.atan(length/7.5))) + rotation
            
            #Create Northern East and West points for 7.5m line
            WNpoint75 = geopy.distance.geodesic(meters=distance_m75).destination(start_point, bearing1N75)
            ENpoint75 = geopy.distance.geodesic(meters=distance_m75).destination(start_point, bearing2N75)
            
            #Create Southern East and West points for 7.5m line
            bearing1S75 = 180 + (math.degrees(math.atan(length/7.5))) + rotation
            bearing2S75 = 180 - (math.degrees(math.atan(length/7.5))) + rotation
            
            WSpoint75 = geopy.distance.geodesic(meters=distance_m75).destination(start_point, bearing1S75)
            ESpoint75 = geopy.distance.geodesic(meters=distance_m75).destination(start_point, bearing2S75)
            
            #print(WNpoint75.latitude, WNpoint75.longitude)
            #print(ENpoint75.latitude, ENpoint75.longitude)
            #print(WSpoint75.latitude, WSpoint75.longitude)
            #print(ESpoint75.latitude, ESpoint75.longitude)
            
            #Create Western North and South points for 7.5m line
            bearing1W75 = 270 + (math.degrees(math.atan(length/7.5))) + rotation
            bearing2W75 = 270 - (math.degrees(math.atan(length/7.5))) + rotation
            
            NWpoint75 = geopy.distance.geodesic(meters=distance_m75).destination(start_point, bearing1W75)
            SWpoint75 = geopy.distance.geodesic(meters=distance_m75).destination(start_point, bearing2W75)
            
            #Create Eastern North and South points for 7.5m line
            bearing1E75 = 90 + (math.degrees(math.atan(length/7.5))) + rotation
            bearing2E75 = 90 - (math.degrees(math.atan(length/7.5))) + rotation
            
            NEpoint75 = geopy.distance.geodesic(meters=distance_m75).destination(start_point, bearing1E75)
            SEpoint75 = geopy.distance.geodesic(meters=distance_m75).destination(start_point, bearing2E75)
            
            #print(NWpoint75.latitude, NWpoint75.longitude)
            #print(SWpoint75.latitude, SWpoint75.longitude)
            #print(NEpoint75.latitude, NEpoint75.longitude)
            #print(SEpoint75.latitude, SEpoint75.longitude)
    
        #Calc for points 25m North
            distance_m25 = sqrt(length**2 + 25**2)
            bearing1N25 = math.degrees(math.atan(length/25)) + rotation
            bearing2N25 = 360 - (math.degrees(math.atan(length/25))) + rotation
            
            #Create East and West points for 25m spacing North 
            WNpoint25 = geopy.distance.geodesic(meters=distance_m25).destination(start_point, bearing1N25)
            ENpoint25 = geopy.distance.geodesic(meters=distance_m25).destination(start_point, bearing2N25)
            
            #Create Southern East and West points for 25m line
            bearing1S25 = 180 + (math.degrees(math.atan(length/25))) + rotation
            bearing2S25 = 180 - (math.degrees(math.atan(length/25))) + rotation
            
            WSpoint25 = geopy.distance.geodesic(meters=distance_m25).destination(start_point, bearing1S25)
            ESpoint25 = geopy.distance.geodesic(meters=distance_m25).destination(start_point, bearing2S25)
            
            #print(WNpoint25.latitude, WNpoint25.longitude)
            #print(ENpoint25.latitude, ENpoint25.longitude)
            #print(WSpoint25.latitude, WSpoint25.longitude)
            #print(ESpoint25.latitude, ESpoint25.longitude)
    
            #Create Western North and South points for 25m line
            bearing1W25 = 270 + (math.degrees(math.atan(length/25))) + rotation
            bearing2W25 = 270 - (math.degrees(math.atan(length/25))) + rotation
            
            NWpoint25 = geopy.distance.geodesic(meters=distance_m25).destination(start_point, bearing1W25)
            SWpoint25 = geopy.distance.geodesic(meters=distance_m25).destination(start_point, bearing2W25)
            
            #Create Eastern North and South points for 25m line
            bearing1E25 = 90 + (math.degrees(math.atan(length/25))) + rotation
            bearing2E25 = 90 - (math.degrees(math.atan(length/25))) + rotation
            
            NEpoint25 = geopy.distance.geodesic(meters=distance_m25).destination(start_point, bearing1E25)
            SEpoint25 = geopy.distance.geodesic(meters=distance_m25).destination(start_point, bearing2E25)
            
            #print(NWpoint25.latitude, NWpoint25.longitude)
            #print(SWpoint25.latitude, SWpoint25.longitude)
            #print(NEpoint25.latitude, NEpoint25.longitude)
            #print(SEpoint25.latitude, SEpoint25.longitude)
    
        #Calc for points 42.5m North
            distance_m425 = sqrt(length**2 + 42.5**2)
            bearing1N425 = math.degrees(math.atan(length/42.5)) + rotation
            bearing2N425 = 360 - (math.degrees(math.atan(length/42.5))) + rotation
            
            #Create East and West points for 42.5m spacing North 
            WNpoint425 = geopy.distance.geodesic(meters=distance_m425).destination(start_point, bearing1N425)
            ENpoint425 = geopy.distance.geodesic(meters=distance_m425).destination(start_point, bearing2N425)
    
            #Create Southern East and West points for 42.5m line
            bearing1S425 = 180 + (math.degrees(math.atan(length/42.5))) + rotation
            bearing2S425 = 180 - (math.degrees(math.atan(length/42.5))) + rotation
    
            WSpoint425 = geopy.distance.geodesic(meters=distance_m425).destination(start_point, bearing1S425)
            ESpoint425 = geopy.distance.geodesic(meters=distance_m425).destination(start_point, bearing2S425)
    
            #print(WNpoint425.latitude, WNpoint425.longitude)
            #print(ENpoint425.latitude, ENpoint425.longitude)
            #print(WSpoint425.latitude, WSpoint425.longitude)
            #print(ESpoint425.latitude, ESpoint425.longitude)
            
            #Create Western North and South points for 42.5m line
            bearing1W425 = 270 + (math.degrees(math.atan(length/42.5))) + rotation
            bearing2W425 = 270 - (math.degrees(math.atan(length/42.5))) + rotation
            
            NWpoint425 = geopy.distance.geodesic(meters=distance_m425).destination(start_point, bearing1W425)
            SWpoint425 = geopy.distance.geodesic(meters=distance_m425).destination(start_point, bearing2W425)
            
            #Create Eastern North and South points for 42.5m line
            bearing1E425 = 90 + (math.degrees(math.atan(length/42.5))) + rotation
            bearing2E425 = 90 - (math.degrees(math.atan(length/42.5))) + rotation
            
            NEpoint425 = geopy.distance.geodesic(meters=distance_m425).destination(start_point, bearing1E425)
            SEpoint425 = geopy.distance.geodesic(meters=distance_m425).destination(start_point, bearing2E425)
            
            #print(NWpoint425.latitude, NWpoint425.longitude)
            #print(SWpoint425.latitude, SWpoint425.longitude)
            #print(NEpoint425.latitude, NEpoint425.longitude)
            #print(SEpoint425.latitude, SEpoint425.longitude)

            #store endpoints for SSS lines 
            #make list of points to loop through for eastings and northings
            ToUTMList = [WNpoint75, ENpoint75, WSpoint75, ESpoint75, NWpoint75, SWpoint75, NEpoint75, SEpoint75, WNpoint25, ENpoint25, WSpoint25, ESpoint25, NWpoint25, SWpoint25, NEpoint25, SEpoint25, WNpoint425, ENpoint425, WSpoint425, ESpoint425, NWpoint425, SWpoint425, NEpoint425, SEpoint425]
            #print(ToUTMList)
 
            
        #create empty variable to append UTM coords to in order to create list outside of each if statement loop
        all_UTMCoords = []
        #total_UTM = []
            

    
        #Loop through created line-points and store as UTM list
        for x in ToUTMList:
            LatTest = utm.from_latlon(x.latitude,x.longitude)
                #print(LatTest)
        
            #Grab just the easting/northing from the UTM
                #Note - current output for LatTest1 gives UTM zone 17S... I am currently ignoring the "S" as it seems to work
                #append values as this loop...loops
            all_UTMCoords.append(f"{LatTest[0]:.2f} {LatTest[1]:.2f}")
            #print(all_UTMCoords)

 
                #print("break here")
        # loop through UTM coords, split the long and lat, but then re-smush on same line
        for coords in all_UTMCoords:
            lat_long = coords.split()
            combined_list.append(f"{lat_long[0]} {lat_long[1]}")

        #join everything into one big list with lat and longs on each line
        singlelist = '\n'.join(combined_list)
        #print(combined_list)
        #print(singlelist)
    
    
    #Variable to write number of lines at beginning of file
    lineslength = "LNS " + endlength_str
    #print(lineslength)

    
    #print(singlelist[:21])
    
    #crack open the filename given earlier, seperate base from suffix
    base, _ = os.path.splitext(file_path)
    txt_filename = base 
    
    #open a tect file to write to
    with open (txt_filename, 'w') as file:
        #create first line that describe amount of lines in file
        file.write(f"{lineslength}\nLIN 2\n")
        
        #index to use in deliminating total data set so they can be seperated into chunks (individual lines/pairs of points) so it can be written in correct format
        set_index = 1 
        #create a total set number so jamming together of last PTS line and last LNN line can be resolved
        total_sets = len(singlelist) // 21
        #loop through sets of data (each pair of end points)
        for i in range(0, len(singlelist), 21):
            if (i // 21) % 2 ==0 and i>0:
                #write LIN 2 before each set
                file.write("LIN 2\n")
            # create iterative subsets to write with
            subset = singlelist[i:i+21]
            # join coordinate for each endpoint
            line = ''.join(map(str, subset))
            #Write out in PTS {coordinates} format
            file.write(f"PTS {line}")
            
            #set up writing LNN # after each set of endpoints with logic to resolve last PTS/LNN smushing described above
            if (i // 21 + 1) %2 ==0:
                #resolve last smush
                if (i // 21 + 1) == total_sets + 1:
                    #write last PTS/LNN set with new line inbetween
                    file.write(f"\nLNN {set_index}\n")
                #write all other LNN lines directly (really already a line down) after PTS line
                else:
                    file.write(f"LNN {set_index}\n")
                #write EOL after each iterative LNN line
                file.write("EOL\n")
                #what to index for next iteration of this loop
                set_index += 1


            
    new_filename = filedialog.asksaveasfilename(defaultextension=".lnw", title="Save File as", filetypes=[("Line files", "*.lnw",),("All files", "*.*")])

    if not new_filename:
        messagebox.showinfo("Cancelled","Operation Cancelled")
                        #if file name exists already in directory, delete it so we can "write over it"
    if os.path.exists(new_filename):
        os.remove(new_filename)
                        
            #rename old name with new filename
    os.rename(txt_filename, new_filename)

    
    if not txt_filename:
     
        messagebox.showwarning("Warning", "No File name provided")
        return
    
    #write out to button where the new file was written to
    label.config(text=f"File renamed to: {new_filename}")



def explanation():
    messagebox.showinfo("Explanation", "When Certifying SideScan, feed this program a .kml of the target(s) you want to investigate and it will spit out Hypack .lnw based on given parameters set in 1.5.7.2 of the 2020 FPM")

# create tkinter GUI
root = tk.Tk()
root.geometry("500x200")
root.title("SSS Certification .lnw automation")

explanation_button = tk.Button(root, text="How to use", command=explanation)
explanation_button.pack(pady=10)


#set purpose of button1 (browse for kml)
browse_button = tk.Button(root, text="Browse for .kml", command=browse_kml)
browse_button.pack(pady=10)

#set purpose of button2 (do math and conversion on coordinates, rename file)
execute_button = tk.Button(root, text="Convert to .lnw", command=spacing)
execute_button.pack(pady=10)

#set style of label
label = Label(root, text="")
label.pack(pady=20)

root.mainloop()
        
        
        
            
            
       