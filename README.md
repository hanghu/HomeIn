## HomeIn

----
  
<img src="doc/HomeIn.png">
  
HomeIn provides an analysis tool for  housing data, prices, and crime rates on a multiple-layered map interface.  This visualization technology allows users to pinpoint areas and analyze their specifications and statistics before making a decision on a home purchase.
     
With HomeIn, users will have  access to past sales and crime data.  This repository is intended to exist as both a place where home-buyers can compare their house price to others in the area, and also as a tool that GitHub users can edit and create similar maps for themselves.

----

### Necessary Packages and License Information
  
All of the necessary implementations in this repository can be carried out using the following software.  All software is open source.
  
**Python packages:**
  
- NumPy 1.11.1  
- pandas 0.19.1  
- matplotlib 1.5.3  
- geopy 1.11.0  
- folium 0.2.1  
- Pillow 3.0.0  

**Licensing info:**
  
HomeIn uses the MIT license.  The data and packages used are completely open source.  We want to make  our code readily available  to be improved and utilized with suggestions and implemenations by our user base.  It is important the house photos are able to be edited, as they will not always provide a 100% accurate photo.  The MIT license for this project is descrived in full in **LICENSE.txt**.

----

###Directory Summary

**Data:** All data used in analyses is accesible from the data folder.  The data is described in full in the DATA_DESCRIPTION.md document.
  
**Examples:** This folder contains iPython Notebook walkthroughs of how we cleaned up our data as well as basic examples of how to use each python package.  A demo of a final map is also included.
  
**HomeIn:** All python modules used in the project directory are found in this folder.  Unit tests are also included for testable modules.
  
**doc:** Documentation for the project is found in this folder.  This includes the project summary, HomeIn logo, and walkthroughs on how to make a map.
  
**UsercaseExplication.md:** Use cases and scientific questions answered by the project.
  
**License.txt:** The  MIT license used for this project.  We thought that having open access to the data was important for multiple user bases. (i.e. real estate professionals, potential homeowners, etc.)
  
----

###Designing a Map
  
**Step 1: Download the Data**
  
**Step 2: Geocode Crime Data and Merge with House Data**
  
**Step 3: Obtain Google Maps API Key and Define URL Parameters**
  
**Step 4: Create Marker Popups**
  
**Step 5: Create Map Layers and View Toggler**
  
