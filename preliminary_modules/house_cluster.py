import os
import webbrowser

import numpy as np
import pandas as pd
import folium
import branca
from folium import plugins
import vincent
from vincent import AxisProperties, PropertySet, ValueRef
import matplotlib.pyplot as plt


"""
	## Create one map showing each listing of in house dataset and saved in a html.
"""
MAX_SHOW = 10
TYPE_OF_CRIME = 6

def popup_text(iters, row):
	TmpFig = str(iters) + ".png"

	fig,ax = plt.subplots()
	ax.bar(range(6), [row['Assault'],row['Breaking & Entering'],row['Drugs'],row['Property Crime'],row['Robbery'],row['Theft']])
	fig.savefig(TmpFig)
	
	html = """
		<h4> Crime Info within Neighborhood </h4><br>
		<img src='file://' + os.path.realpath(TmpFig) alt="Crime Histogram" style="width:304px;height:228px;"> <br>
		"""

	html = html + "Total Crimes: " + str(row['number of crimes']) + "<br>"
	html = html + "Assault: " + str(row['Assault']) + "<br>"
	html = html + "Breaking & Entering: " + str(row['Breaking & Entering']) + "<br>"
	html = html + "Drugs: " + str(row['Drugs']) + "<br>"
	html = html + "Property Crime: " + str(row['Property Crime']) + "<br>"
	html = html + "Robbery: " + str(row['Robbery']) + "<br>"
	html = html + "Theft: " + str(row['Theft']+row['Theft from Vehicle']+row['Theft of Vehicle']) + "<br>"
	#html = html + <img src="./tmp.png" alt="Crime Histogram" style="width:304px;height:228px;"> + <br>;
	html = html + "<h4> House Info </h4><br>"
	html = html + "Sqft of Living Area: " + str(row['sqft_living']) + "<br>"
	html = html + "Sqft of Lot:imesiik " + str(row['sqft_lot']) + "<br>"
	html = html + "Price: " + str(row['price']) + "<br>"
	html = html + "Bedroom/Bathroom: " + str(row['bedrooms']) + "Bed/" + str(row['bathrooms']) + "Bath" + "<br>"
	html = html + "Year Built: " + str(row['yr_built']) + "<br>"
	html = html + "Year Renovated: " + str(row['yr_renovated']) + "<br>"

	# bar plot'file://' + os.path.realpath(TmpFig)
	#BarPlot = vincent.Bar([10, 20, 30, 20, 15, 30, 45], width = 150, height = 50)
	#BarPlot.axis_titles(x='Crime Type', y='Number of Incidents')
	#rotate x axis labels
	#ax = AxisProperties(
    #    labels = PropertySet(angle=ValueRef(value=270)))
	#BarPlot.axes[0].properties = ax
	#folium.Vega(BarPlot, width = 300, height = 100).add_to(popup)

	iframe = branca.element.IFrame(html = html, width = 500, height = 300)
	#BarFigure = folium.element.Figure()
	#BarPlot.add_to(BarFigure)
	#BarFigure.add_to(iframe)

	popup = folium.Popup(iframe, max_width = 2650)

	return popup

def house_cluster(HouseData, HouseUrl):
	house_map = folium.Map(location=[HouseData['lat'].mean(), HouseData['long'].mean()], zoom_start=10)
	marker_cluster = folium.MarkerCluster().add_to(house_map)

	for iters, row in data[0:MAX_SHOW].iterrows():
		folium.Marker([row["lat"], row["long"]], 
			popup=popup_text(iters, row)).add_to(marker_cluster)
	# Save the house cluster map to a html and open it in broswer.
	house_map.save(HouseUrl)


#Example
#HOUSE_URL = 'House Cluster Map.html'
#pd.set_option('display.max_columns', None)
#
#data = pd.read_csv("./Data/house_crime_data.csv", parse_dates=['date'])
#house_cluster(data, HOUSE_URL);
#webbrowser.open('file://' + os.path.realpath(HOUSE_URL), new=2)
