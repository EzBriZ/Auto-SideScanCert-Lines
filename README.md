# Auto-SideScanCert-Lines
2024-08-25
# My first project - primarily for the purpose of learning python - that automates Side Scan Certification lines for any number of given potential targets. 
# Developed for use aboard the NOAA ship Thomas Jefferson in aid of hydrographic surveying 

# Using Sypder - and Pydro's subsequent environment - this project:
  reads a kml file\
  strips coordinates\
  loops through coordinates\
    depending on the prompting of the function "spacing()" - with the options of 50,75, and 100 - calculates the 24 points from which to draw 12 SSC lines\
    converts coordinates to UTM\
  outputs to UTM to text file in a format readable by HYPACK (.lnw) --- in progress\
  finds output file and changes extension from .txt to .lnw --- in progress
