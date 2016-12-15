##HomeIn

----

<img src="doc/HomeIn.png">

HomeIn provides an analysis tool for  housing data, prices, and crime rates on a multiple-layered map interface.  This visualization technology allows users to pinpoint areas and analyze their specifications and statistics before making a decision on a home purchase.

With HomeIn, users will have  access to past sales and crime data.  This repository is intended to exist as both a place where home-buyers can compare their house price to others in the area, and also as a tool that GitHub users can edit and create similar maps for themselves.

----

### Necessary Packages and License Information

All of the necessary implementations in this repository can be carried out using the following software.  All software is open source.

####Python packages:

- NumPy 1.11.1  
- pandas 0.19.1  
- matplotlib 1.5.3  
- geopy 1.11.0  
- folium 0.2.1  
- Pillow 3.0.0  

####Installing Packages:

**1. Install numpy, pandas, and matplotlib:**  
$ conda install numpy pandas matplotlib

**2. Install geopy:**  
$ pip install geopy

**3. Install folium:**  
$ pip install folium

**4. Install Pillow:**  
$ pip install Pillow

####Licensing info:

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

###Directory Structure

The package is organized as follows:

    HomeIn (master)  
    |---Data  
        |---King_County_Sheriff_s_Office.csv  
        |---cleaned_crime_data.csv  
        |---crime_info.csv  
        |---crime_info_sample_of_10.csv  
        |---house_crime_data.csv  
        |---kc_house_data.csv  
        |---merged_data_sample.csv  
        |---zipcode_king_county.geojson  
    |---Examples  
        |---Correlations.ipynb  
        |---FoliumExpl.ipynb  
        |---Geopy.ipynb  
        |---House_photos.ipynb  
        |---Map.html  
        |---Zipcodes.ipynb  
        |---crime_info_usage.ipynb  
        |---data_preprocessing.ipynb  
        |---layer_map.ipynb  
    |---HomeIn  
        |---__init__.py  
        |---crime_info.py  
        |---house_cluster.py  
        |---map_demo.py  
        |---test_zipcodes.py  
        |---unittest_crime_info.py  
        |---zipcodes_search.py  
    |---doc
        |---CSE599_project_summary.pptx  
        |---HomeIn.png  
        |---Makefile  
    |--.gitignore  
    |--DATA_DESCRIPTION.md  
    |--LICENSE.txt  
    |--README.md  
    |--UsercaseExplication.md  
    |--setup.py  

----

###Tutorial For Generating An Interactive Map With Custom Parameters

####Step 1: Download the Data

The raw datasets are all open data from [Kaggle](https://www.kaggle.com/harlfoxem/housesalesprediction) or [King County Open Data](https://moto.data.socrata.com/dataset/King-County-Sheriff-s-Office/4h35-4mtu). The main columns of the data are the GPS coordinates of the house and crime incidents, crime type as well as house information including price, _etc._ The data used to generate the demo Map are described in detail in **DATA_DESCRIPTION.md**

####Step 2: Geocode Crime Data and Merge with House Data

With the questions mostly concerning the users, the crime information around houses in the past a few years within the cutoff distance are generated and added to house data by three steps. The example in our case is in '/Examples/data_preprocessing.ipynb'.  

- **1. Set a year range.** In our case, we set the year range as the past 5 years before those houses are sold and drop all the crime data which are not in that time range.  

- **2. Set a **cutoff distance.** The cutoff distance in our case is default as 1.0 mile. Plug in the gps corrdinates, house ids and crime type by the function _crime_info_output_ in module _crime_info_. This process might take a long time, in our case, it took 6.5h to generate all the crime data.  

- **3. Merge** the crime data with house data based on their ids.  

####Step 3: Obtain Google Maps API Key and Define URL Parameters

####Step 4: Create Marker Popups

####Step 5: Create Map Layers and View Toggler
