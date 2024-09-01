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
    
    #determine number of lines being written to use in creating .txt file
    endlength = len(all_coordinates)*12
    print(endlength)

    #Create list variable to loop through in order to name lines in output file
    listlength = 0
    
    for x in all_coordinates:
        long = x[0]
        lat = x[1]
    
        start_point = geopy.Point(lat,long)


    
    #-----------------------------------------------------------------------------------------------------------
    
        if number == 50:
    
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


    
            #Loop through created line-points and store as UTM list
            for x in ToUTMList:
                LatTest = utm.from_latlon(x.latitude,x.longitude)
     
            #Grab just the easting/northing from the UTM
                #Note - current output for LatTest1 gives UTM zone 17S... I am currently ignoring the "S" as it seems to work
                easting_str = f"{LatTest[0]:.2f}"
                northing_str = f"{LatTest[1]:.2f}"
                
                print(easting_str,northing_str)
                
        
                listlength = listlength + 1
                print(listlength)
                
            print("break here")
            
        #testing from here on on how to create line file
        
        lines = []
            
            
        print(lines)
            
            appendinglines = ["LIN 2\n", ]
            #Compile Test variables in txt file format that Hypack could read once converted to .lnw
            #lines = ["LNS 1\n", "LIN 2\n", f"PTS {easting_str} {northing_str}\n", f"PTS {easting2_str} {northing2_str}\n", "LNN 1\n", "EOL"]
    



            
    


    
    #Compile Test variables in txt file format that Hypack could read once converted to .lnw
    #lines = ["LNS 1\n", "LIN 2\n", f"PTS {easting_str} {northing_str}\n", f"PTS {easting2_str} {northing2_str}\n", "LNN 1\n", "EOL"]
        
        #Write file
        #with open("lineplanpractice", "w") as file:
            #file.writelines(lines)
            #file.close()
        
        


        


