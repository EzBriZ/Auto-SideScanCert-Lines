# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Overarching project to allow "copy/paste" of line plans for Hypack when conducting SideScan Certification 
#This particular file grabs coordinates from kml file to manipulate and create lines
#CarterSmith#
#July2024



#Current Status - Looping through spacing nad creating all 216(i think. 9x24) new points for lines and loops through to convert to utm. Current problem is getting the loop to work for the writing to file. Needs to tell how many points there are and seperate every 24 points


#import pyKML

#parser tool from pykml library
from pykml import parser

#open and read KML file (binary)
with open('SSSCertObj.kml', 'rb') as file:
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
                
    

#bring in geopy and maths to do math of lat and long to linear distance
import geopy
import geopy.distance
import math
from math import sqrt
import utm


def spacing(number):
    
    #set length and height
    length = 12.5
    
    #determine number of lines being written to use in creating .txt file -- Might need to go after append coordinates in order to convert number to string for writing output
    endlength= len(all_coordinates)*12
    #turn that number into string for writing to file
    endlength_str = f"{endlength}"
    #print(endlength)

    
    for x in all_coordinates:
        long = x[0]
        lat = x[1]
    
        start_point = geopy.Point(lat,long)
    
        if number == 100:
            
        #Calculate positions of new point for 15m line North 
            distance_m15 = sqrt(length**2 + 15**2)
            bearing1N15 = math.degrees(math.atan(length/15))
            bearing2N15 = 360 - (math.degrees(math.atan(length/15)))
            
            #Create Northern East and West points for 15m line
            WNpoint15 = geopy.distance.geodesic(meters=distance_m15).destination(start_point, bearing1N15)
            ENpoint15 = geopy.distance.geodesic(meters=distance_m15).destination(start_point, bearing2N15)
            
            #Create Southern East and West points for 15m line
            bearing1S15 = 180 + (math.degrees(math.atan(length/15)))
            bearing2S15 = 180 - (math.degrees(math.atan(length/15)))
            
            WSpoint15 = geopy.distance.geodesic(meters=distance_m15).destination(start_point, bearing1S15)
            ESpoint15 = geopy.distance.geodesic(meters=distance_m15).destination(start_point, bearing2S15)
            
            #print(WNpoint15.latitude, WNpoint15.longitude)
            #print(ENpoint15.latitude, ENpoint15.longitude)
            #print(WSpoint15.latitude, WSpoint15.longitude)
            #print(ESpoint15.latitude, ESpoint15.longitude)
    
            #Create Western North and South points for 15m line
            bearing1W15 = 270 + (math.degrees(math.atan(length/15)))
            bearing2W15 = 270 - (math.degrees(math.atan(length/15)))
            
            NWpoint15 = geopy.distance.geodesic(meters=distance_m15).destination(start_point, bearing1W15)
            SWpoint15 = geopy.distance.geodesic(meters=distance_m15).destination(start_point, bearing2W15)
            
            #Create Eastern North and South points for 15m line
            bearing1E15 = 90 + (math.degrees(math.atan(length/15)))
            bearing2E15 = 90 - (math.degrees(math.atan(length/15)))
            
            NEpoint15 = geopy.distance.geodesic(meters=distance_m15).destination(start_point, bearing1E15)
            SEpoint15 = geopy.distance.geodesic(meters=distance_m15).destination(start_point, bearing2E15)
            
            #print(NWpoint15.latitude, NWpoint15.longitude)
            #print(SWpoint15.latitude, SWpoint15.longitude)
            #print(NEpoint15.latitude, NEpoint15.longitude)
            #print(SEpoint15.latitude, SEpoint15.longitude)
            
        #Calc for points 50m North
            distance_m50 = sqrt(length**2 + 50**2)
            bearing1N50 = math.degrees(math.atan(length/50))
            bearing2N50 = 360 - (math.degrees(math.atan(length/50)))
            
            #Create East and West points for 50m spacing North 
            WNpoint50 = geopy.distance.geodesic(meters=distance_m50).destination(start_point, bearing1N50)
            ENpoint50 = geopy.distance.geodesic(meters=distance_m50).destination(start_point, bearing2N50)
            
            #Create Southern East and West points for 50m line
            bearing1S50 = 180 + (math.degrees(math.atan(length/50)))
            bearing2S50 = 180 - (math.degrees(math.atan(length/50)))
            
            WSpoint50 = geopy.distance.geodesic(meters=distance_m50).destination(start_point, bearing1S50)
            ESpoint50 = geopy.distance.geodesic(meters=distance_m50).destination(start_point, bearing2S50)
            
            #print(WNpoint50.latitude, WNpoint50.longitude)
            #print(ENpoint50.latitude, ENpoint50.longitude)
            #print(WSpoint50.latitude, WSpoint50.longitude)
            #print(ESpoint50.latitude, ESpoint50.longitude)
            
            #Create Western North and South points for 50m line
            bearing1W50 = 270 + (math.degrees(math.atan(length/50)))
            bearing2W50 = 270 - (math.degrees(math.atan(length/50)))
            
            NWpoint50 = geopy.distance.geodesic(meters=distance_m50).destination(start_point, bearing1W50)
            SWpoint50 = geopy.distance.geodesic(meters=distance_m50).destination(start_point, bearing2W50)
            
            #Create Eastern North and South points for 50m line
            bearing1E50 = 90 + (math.degrees(math.atan(length/50)))
            bearing2E50 = 90 - (math.degrees(math.atan(length/50)))
            
            NEpoint50 = geopy.distance.geodesic(meters=distance_m50).destination(start_point, bearing1E50)
            SEpoint50 = geopy.distance.geodesic(meters=distance_m50).destination(start_point, bearing2E50)
            
            #print(NWpoint50.latitude, NWpoint50.longitude)
            #print(SWpoint50.latitude, SWpoint50.longitude)
            #print(NEpoint50.latitude, NEpoint50.longitude)
            #print(SEpoint50.latitude, SEpoint50.longitude)
    
    
        #Calc for points 85m North
            distance_m85 = sqrt(length**2 + 85**2)
            bearing1N85 = math.degrees(math.atan(length/85))
            bearing2N85 = 360 - (math.degrees(math.atan(length/85)))
            
            #Create East and West points for 85m spacing North 
            WNpoint85 = geopy.distance.geodesic(meters=distance_m85).destination(start_point, bearing1N85)
            ENpoint85 = geopy.distance.geodesic(meters=distance_m85).destination(start_point, bearing2N85)
    
            #Create Southern East and West points for 85m line
            bearing1S85 = 180 + (math.degrees(math.atan(length/85)))
            bearing2S85 = 180 - (math.degrees(math.atan(length/85)))
    
            WSpoint85 = geopy.distance.geodesic(meters=distance_m85).destination(start_point, bearing1S85)
            ESpoint85 = geopy.distance.geodesic(meters=distance_m85).destination(start_point, bearing2S85)
    
            #print(WNpoint85.latitude, WNpoint85.longitude)
            #print(ENpoint85.latitude, ENpoint85.longitude)
            #print(WSpoint85.latitude, WSpoint85.longitude)
            #print(ESpoint85.latitude, ESpoint85.longitude)
            
            #Create Western North and South points for 85m line
            bearing1W85 = 270 + (math.degrees(math.atan(length/85)))
            bearing2W85 = 270 - (math.degrees(math.atan(length/85)))
            
            NWpoint85 = geopy.distance.geodesic(meters=distance_m85).destination(start_point, bearing1W85)
            SWpoint85 = geopy.distance.geodesic(meters=distance_m85).destination(start_point, bearing2W85)
            
            #Create Eastern North and South points for 85m line
            bearing1E85 = 90 + (math.degrees(math.atan(length/85)))
            bearing2E85 = 90 - (math.degrees(math.atan(length/85)))
            
            NEpoint85 = geopy.distance.geodesic(meters=distance_m85).destination(start_point, bearing1E85)
            SEpoint85 = geopy.distance.geodesic(meters=distance_m85).destination(start_point, bearing2E85)
            
            #print(NWpoint85.latitude, NWpoint85.longitude)
            #print(SWpoint85.latitude, SWpoint85.longitude)
            #print(NEpoint85.latitude, NEpoint85.longitude)
            #print(SEpoint85.latitude, SEpoint85.longitude)
    
    
    #-----------------------------------------------------------------------------------------------------------
    
        elif number == 75:
            
        #Calculate positions of new point for 11.25m line North 
            distance_m1125 = sqrt(length**2 + 11.25**2)
            bearing1N1125 = math.degrees(math.atan(length/11.25))
            bearing2N1125 = 360 - (math.degrees(math.atan(length/11.25)))
            
            #Create Northern East and West points for 11.25m line
            WNpoint1125 = geopy.distance.geodesic(meters=distance_m1125).destination(start_point, bearing1N1125)
            ENpoint1125 = geopy.distance.geodesic(meters=distance_m1125).destination(start_point, bearing2N1125)
            
            #Create Southern East and West points for 11.25m line
            bearing1S1125 = 180 + (math.degrees(math.atan(length/11.25)))
            bearing2S1125 = 180 - (math.degrees(math.atan(length/11.25)))
            
            WSpoint1125 = geopy.distance.geodesic(meters=distance_m1125).destination(start_point, bearing1S1125)
            ESpoint1125 = geopy.distance.geodesic(meters=distance_m1125).destination(start_point, bearing2S1125)
            
            #print(WNpoint1125.latitude, WNpoint1125.longitude)
            #print(ENpoint1125.latitude, ENpoint1125.longitude)
            #print(WSpoint1125.latitude, WSpoint1125.longitude)
            #print(ESpoint1125.latitude, ESpoint1125.longitude)
              
            #Create Western North and South points for 11.25 line
            bearing1W1125 = 270 + (math.degrees(math.atan(length/11.25)))
            bearing2W1125 = 270 - (math.degrees(math.atan(length/11.25)))
            
            NWpoint1125 = geopy.distance.geodesic(meters=distance_m1125).destination(start_point, bearing1W1125)
            SWpoint1125 = geopy.distance.geodesic(meters=distance_m1125).destination(start_point, bearing2W1125)
            
            #Create Eastern North and South points for 11.25 line
            bearing1E1125 = 90 + (math.degrees(math.atan(length/11.25)))
            bearing2E1125 = 90 - (math.degrees(math.atan(length/11.25)))
            
            NEpoint1125 = geopy.distance.geodesic(meters=distance_m1125).destination(start_point, bearing1E1125)
            SEpoint1125 = geopy.distance.geodesic(meters=distance_m1125).destination(start_point, bearing2E1125)
            
            #print(NWpoint1125.latitude, NWpoint1125.longitude)
            #print(SWpoint1125.latitude, SWpoint1125.longitude)
            #print(NEpoint1125.latitude, NEpoint1125.longitude)
            #print(SEpoint1125.latitude, SEpoint1125.longitude)
            
        #Calculate positions for 37.5m line North 
            distance_m375 = sqrt(length**2 + 37.5**2)
            bearing1N375 = math.degrees(math.atan(length/37.5))
            bearing2N375 = 360 - (math.degrees(math.atan(length/37.5)))
            
            #Create Northern East and West points for 37.5m line
            WNpoint375 = geopy.distance.geodesic(meters=distance_m375).destination(start_point, bearing1N375)
            ENpoint375 = geopy.distance.geodesic(meters=distance_m375).destination(start_point, bearing2N375)
            
            #Create Southern East and West points for 37.5m line
            bearing1S375 = 180 + (math.degrees(math.atan(length/37.5)))
            bearing2S375 = 180 - (math.degrees(math.atan(length/37.5)))
            
            WSpoint375 = geopy.distance.geodesic(meters=distance_m375).destination(start_point, bearing1S375)
            ESpoint375 = geopy.distance.geodesic(meters=distance_m375).destination(start_point, bearing2S375)
            
            #print(WNpoint375.latitude, WNpoint375.longitude)
            #print(ENpoint375.latitude, ENpoint375.longitude)
            #print(WSpoint375.latitude, WSpoint375.longitude)
            #print(ESpoint375.latitude, ESpoint375.longitude)
            
            #Create Western North and South points for 37.5m line
            bearing1W375 = 270 + (math.degrees(math.atan(length/37.5)))
            bearing2W375 = 270 - (math.degrees(math.atan(length/37.5)))
            
            NWpoint375 = geopy.distance.geodesic(meters=distance_m375).destination(start_point, bearing1W375)
            SWpoint375 = geopy.distance.geodesic(meters=distance_m375).destination(start_point, bearing2W375)
            
            #Create Eastern North and South points for 37.5m line
            bearing1E375 = 90 + (math.degrees(math.atan(length/37.5)))
            bearing2E375 = 90 - (math.degrees(math.atan(length/37.5)))
            
            NEpoint375 = geopy.distance.geodesic(meters=distance_m375).destination(start_point, bearing1E375)
            SEpoint375 = geopy.distance.geodesic(meters=distance_m375).destination(start_point, bearing2E375)
            
            #print(NWpoint375.latitude, NWpoint375.longitude)
            #print(SWpoint375.latitude, SWpoint375.longitude)
            #print(NEpoint375.latitude, NEpoint375.longitude)
            #print(SEpoint375.latitude, SEpoint375.longitude)
            
        #Calculate positions for 63.75m line North 
            distance_m6375 = sqrt(length**2 + 63.75**2)
            bearing1N6375 = math.degrees(math.atan(length/63.75))
            bearing2N6375 = 360 - (math.degrees(math.atan(length/63.75)))
            
            #Create Northern East and West points for 63.75m line
            WNpoint6375 = geopy.distance.geodesic(meters=distance_m6375).destination(start_point, bearing1N6375)
            ENpoint6375 = geopy.distance.geodesic(meters=distance_m6375).destination(start_point, bearing2N6375)
            
            #Create Southern East and West points for 63.75m line
            bearing1S6375 = 180 + (math.degrees(math.atan(length/63.75)))
            bearing2S6375 = 180 - (math.degrees(math.atan(length/63.75)))
            
            WSpoint6375 = geopy.distance.geodesic(meters=distance_m6375).destination(start_point, bearing1S6375)
            ESpoint6375 = geopy.distance.geodesic(meters=distance_m6375).destination(start_point, bearing2S6375)
            
            #print(WNpoint6375.latitude, WNpoint6375.longitude)
            #print(ENpoint6375.latitude, ENpoint6375.longitude)
            #print(WSpoint6375.latitude, WSpoint6375.longitude)
            #print(ESpoint6375.latitude, ESpoint6375.longitude)    
            
            #Create Western North and South points for 63.75m line
            bearing1W6375 = 270 + (math.degrees(math.atan(length/63.75)))
            bearing2W6375 = 270 - (math.degrees(math.atan(length/63.75)))
            
            NWpoint6375 = geopy.distance.geodesic(meters=distance_m6375).destination(start_point, bearing1W6375)
            SWpoint6375 = geopy.distance.geodesic(meters=distance_m6375).destination(start_point, bearing2W6375)
            
            #Create Eastern North and South points for 63.75m line
            bearing1E6375 = 90 + (math.degrees(math.atan(length/63.75)))
            bearing2E6375 = 90 - (math.degrees(math.atan(length/63.75)))
            
            NEpoint6375 = geopy.distance.geodesic(meters=distance_m6375).destination(start_point, bearing1E6375)
            SEpoint6375 = geopy.distance.geodesic(meters=distance_m6375).destination(start_point, bearing2E6375)
            
            #print(NWpoint6375.latitude, NWpoint6375.longitude)
            #print(SWpoint6375.latitude, SWpoint6375.longitude)
            #print(NEpoint6375.latitude, NEpoint6375.longitude)
            #print(SEpoint6375.latitude, SEpoint6375.longitude)
    
    #-----------------------------------------------------------------------------------------------------------
    
        elif number == 50:
    
        #Calculate positions of new point for 7.5m line North 
            distance_m75 = sqrt(length**2 + 7.5**2)
            bearing1N75 = math.degrees(math.atan(length/7.5))
            bearing2N75 = 360 - (math.degrees(math.atan(length/7.5)))
            
            #Create Northern East and West points for 7.5m line
            WNpoint75 = geopy.distance.geodesic(meters=distance_m75).destination(start_point, bearing1N75)
            ENpoint75 = geopy.distance.geodesic(meters=distance_m75).destination(start_point, bearing2N75)
            
            #Create Southern East and West points for 7.5m line
            bearing1S75 = 180 + (math.degrees(math.atan(length/7.5)))
            bearing2S75 = 180 - (math.degrees(math.atan(length/7.5)))
            
            WSpoint75 = geopy.distance.geodesic(meters=distance_m75).destination(start_point, bearing1S75)
            ESpoint75 = geopy.distance.geodesic(meters=distance_m75).destination(start_point, bearing2S75)
            
            #print(WNpoint75.latitude, WNpoint75.longitude)
            #print(ENpoint75.latitude, ENpoint75.longitude)
            #print(WSpoint75.latitude, WSpoint75.longitude)
            #print(ESpoint75.latitude, ESpoint75.longitude)
            
            #Create Western North and South points for 7.5m line
            bearing1W75 = 270 + (math.degrees(math.atan(length/7.5)))
            bearing2W75 = 270 - (math.degrees(math.atan(length/7.5)))
            
            NWpoint75 = geopy.distance.geodesic(meters=distance_m75).destination(start_point, bearing1W75)
            SWpoint75 = geopy.distance.geodesic(meters=distance_m75).destination(start_point, bearing2W75)
            
            #Create Eastern North and South points for 7.5m line
            bearing1E75 = 90 + (math.degrees(math.atan(length/7.5)))
            bearing2E75 = 90 - (math.degrees(math.atan(length/7.5)))
            
            NEpoint75 = geopy.distance.geodesic(meters=distance_m75).destination(start_point, bearing1E75)
            SEpoint75 = geopy.distance.geodesic(meters=distance_m75).destination(start_point, bearing2E75)
            
            #print(NWpoint75.latitude, NWpoint75.longitude)
            #print(SWpoint75.latitude, SWpoint75.longitude)
            #print(NEpoint75.latitude, NEpoint75.longitude)
            #print(SEpoint75.latitude, SEpoint75.longitude)
    
        #Calc for points 25m North
            distance_m25 = sqrt(length**2 + 25**2)
            bearing1N25 = math.degrees(math.atan(length/25))
            bearing2N25 = 360 - (math.degrees(math.atan(length/25)))
            
            #Create East and West points for 25m spacing North 
            WNpoint25 = geopy.distance.geodesic(meters=distance_m25).destination(start_point, bearing1N25)
            ENpoint25 = geopy.distance.geodesic(meters=distance_m25).destination(start_point, bearing2N25)
            
            #Create Southern East and West points for 25m line
            bearing1S25 = 180 + (math.degrees(math.atan(length/25)))
            bearing2S25 = 180 - (math.degrees(math.atan(length/25)))
            
            WSpoint25 = geopy.distance.geodesic(meters=distance_m25).destination(start_point, bearing1S25)
            ESpoint25 = geopy.distance.geodesic(meters=distance_m25).destination(start_point, bearing2S25)
            
            #print(WNpoint25.latitude, WNpoint25.longitude)
            #print(ENpoint25.latitude, ENpoint25.longitude)
            #print(WSpoint25.latitude, WSpoint25.longitude)
            #print(ESpoint25.latitude, ESpoint25.longitude)
    
            #Create Western North and South points for 25m line
            bearing1W25 = 270 + (math.degrees(math.atan(length/25)))
            bearing2W25 = 270 - (math.degrees(math.atan(length/25)))
            
            NWpoint25 = geopy.distance.geodesic(meters=distance_m25).destination(start_point, bearing1W25)
            SWpoint25 = geopy.distance.geodesic(meters=distance_m25).destination(start_point, bearing2W25)
            
            #Create Eastern North and South points for 25m line
            bearing1E25 = 90 + (math.degrees(math.atan(length/25)))
            bearing2E25 = 90 - (math.degrees(math.atan(length/25)))
            
            NEpoint25 = geopy.distance.geodesic(meters=distance_m25).destination(start_point, bearing1E25)
            SEpoint25 = geopy.distance.geodesic(meters=distance_m25).destination(start_point, bearing2E25)
            
            #print(NWpoint25.latitude, NWpoint25.longitude)
            #print(SWpoint25.latitude, SWpoint25.longitude)
            #print(NEpoint25.latitude, NEpoint25.longitude)
            #print(SEpoint25.latitude, SEpoint25.longitude)
    
        #Calc for points 42.5m North
            distance_m425 = sqrt(length**2 + 42.5**2)
            bearing1N425 = math.degrees(math.atan(length/42.5))
            bearing2N425 = 360 - (math.degrees(math.atan(length/42.5)))
            
            #Create East and West points for 42.5m spacing North 
            WNpoint425 = geopy.distance.geodesic(meters=distance_m425).destination(start_point, bearing1N425)
            ENpoint425 = geopy.distance.geodesic(meters=distance_m425).destination(start_point, bearing2N425)
    
            #Create Southern East and West points for 42.5m line
            bearing1S425 = 180 + (math.degrees(math.atan(length/42.5)))
            bearing2S425 = 180 - (math.degrees(math.atan(length/42.5)))
    
            WSpoint425 = geopy.distance.geodesic(meters=distance_m425).destination(start_point, bearing1S425)
            ESpoint425 = geopy.distance.geodesic(meters=distance_m425).destination(start_point, bearing2S425)
    
            #print(WNpoint425.latitude, WNpoint425.longitude)
            #print(ENpoint425.latitude, ENpoint425.longitude)
            #print(WSpoint425.latitude, WSpoint425.longitude)
            #print(ESpoint425.latitude, ESpoint425.longitude)
            
            #Create Western North and South points for 42.5m line
            bearing1W425 = 270 + (math.degrees(math.atan(length/42.5)))
            bearing2W425 = 270 - (math.degrees(math.atan(length/42.5)))
            
            NWpoint425 = geopy.distance.geodesic(meters=distance_m425).destination(start_point, bearing1W425)
            SWpoint425 = geopy.distance.geodesic(meters=distance_m425).destination(start_point, bearing2W425)
            
            #Create Eastern North and South points for 42.5m line
            bearing1E425 = 90 + (math.degrees(math.atan(length/42.5)))
            bearing2E425 = 90 - (math.degrees(math.atan(length/42.5)))
            
            NEpoint425 = geopy.distance.geodesic(meters=distance_m425).destination(start_point, bearing1E425)
            SEpoint425 = geopy.distance.geodesic(meters=distance_m425).destination(start_point, bearing2E425)
            
            #print(NWpoint425.latitude, NWpoint425.longitude)
            #print(SWpoint425.latitude, SWpoint425.longitude)
            #print(NEpoint425.latitude, NEpoint425.longitude)
            #print(SEpoint425.latitude, SEpoint425.longitude)


        
            #make list of points to loop through for eastings and northings
            ToUTMList = [WNpoint75, ENpoint75, WSpoint75, ESpoint75, NWpoint75, SWpoint75, NEpoint75, SEpoint75, WNpoint25, ENpoint25, WSpoint25, ESpoint25, NWpoint25, SWpoint25, NEpoint25, SEpoint25, WNpoint425, ENpoint425, WSpoint425, ESpoint425, NWpoint425, SWpoint425, NEpoint425, SEpoint425]
            
            #create empty variable to append UTM coords to in order to create list outside of each if statement loop
            all_UTMCoords = []
            total_UTM = []

    
            #Loop through created line-points and store as UTM list
            for x in ToUTMList:
                LatTest = utm.from_latlon(x.latitude,x.longitude)
     
            #Grab just the easting/northing from the UTM
                #Note - current output for LatTest1 gives UTM zone 17S... I am currently ignoring the "S" as it seems to work
                UTMCoords = f"{LatTest[0]:.2f}, {LatTest[1]:.2f}"
                #append values as this loop...loops
                all_UTMCoords.append(UTMCoords)
                #print(UTMCoords)

                
                
        print("break here")
        total_UTM.extend(all_UTMCoords)
            #print(total_UTM)
        singlelist = '\n'.join(total_UTM)
        print(singlelist)
        print(len(singlelist))
            
        #testing from here on on how to create line file
        
        #Variable to write number of lines at beginning of file
        #lineslength = ["LNS " + endlength_str]
        #Variable to write which line youre writing to in file
        #numberoflines = list(range(1,endlength+1))
        #Variable for how many points make up line(for this purpose, always 2)
        #LIN2 = "LIN2"
        
        
        #all_UTMCoords = f"{all_UTMCoords}"
        #print(all_UTMCoords)
        #pairs = all_UTMCoords[:2]
        #print(pairs)
        
        
        

            
           
         #Compile Test variables in txt file format that Hypack could read once converted to .lnw
         #lines = ["LNS 1\n", "LIN 2\n", f"PTS {easting_str} {northing_str}\n", f"PTS {easting2_str} {northing2_str}\n", "LNN 1\n", "EOL"]
    



            
    


    
    #Compile Test variables in txt file format that Hypack could read once converted to .lnw
    #lines = ["LNS 1\n", "LIN 2\n", f"PTS {easting_str} {northing_str}\n", f"PTS {easting2_str} {northing2_str}\n", "LNN 1\n", "EOL"]
        
        #Write file
        #with open("lineplanpractice", "w") as file:
            #file.writelines(lines)
            #file.close()
        
        




