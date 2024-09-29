# Auto-SideScanCert-Lines
2024-08-25\
My first project - primarily for the purpose of learning python - that automates Side Scan Certification lines for any number of given potential targets.\
Developed for use aboard the NOAA ship Thomas Jefferson in aid of hydrographic surveying 

# Using Sypder - and Pydro's subsequent environment - this project:
  prompts users with a button which will: 
  read a kml file\
  strip coordinates\
  loop through coordinates\
    depending on the prompting of the function "spacing()" - with the options of 50,75, and 100 - calculates the 24 points from which to draw 12 SSC lines\
    converts coordinates to UTM\
  outputs UTM to file in a format readable by HYPACK (.lnw) 
 


  
