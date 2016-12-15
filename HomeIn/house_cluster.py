import folium


"""
	## Create one map showing each listing of in house dataset and saved in a html.
"""
MAX_SHOW = 10
TYPE_OF_CRIME = 6

def popup_text(iters, row):
    url = "https://maps.googleapis.com/maps/api/streetview?size=300x300&location=" + str(row['lat']) + "," + str(row['long']) + "&pitch=10&key=AIzaSyALN4DKjGjGkg_KA7XFvLSCBlBOMATQdxE"
	
    html = """
		<h4> House Street View </h4><br>
		"""

    html = html + "<img src =" + url + ">" + "<br>"
    html = html + "<h4> House Info </h4><br>"
    html = html + "Sqft of Living Area: " + str(row['sqft_living']) + "<br>"
    html = html + "Sqft of Lot:imesiik " + str(row['sqft_lot']) + "<br>"
    html = html + "Price: " + str(row['price']) + "<br>"
    html = html + "Bedroom/Bathroom: " + str(row['bedrooms']) + "Bed/" + str(row['bathrooms']) + "Bath" + "<br>"
    html = html + "Year Built: " + str(row['yr_built']) + "<br>"
    html = html + "Year Renovated: " + str(row['yr_renovated']) + "<br>"
    html = html + "<h4> Crime Info within Neighborhood <br> (5-year total within 1-mile radius) </h4><br>"
    html = html + "Total Crimes: " + str(row['number of crimes']) + "<br>"
    html = html + "Assault: " + str(row['Assault']) + "<br>"
    html = html + "Breaking & Entering: " + str(row['Breaking & Entering']) + "<br>"
    html = html + "Drugs: " + str(row['Drugs']) + "<br>"
    html = html + "Property Crime: " + str(row['Property Crime']) + "<br>"
    html = html + "Robbery: " + str(row['Robbery']) + "<br>"
    html = html + "Theft: " + str(row['Theft']+row['Theft from Vehicle']+row['Theft of Vehicle']) + "<br>"

    iframe = folium.element.IFrame(html=html, width=500, height=300)
    popup = folium.Popup(iframe, max_width=2650)

    return popup

def house_cluster(HouseData, HouseUrl):
    house_map = folium.Map(location=[HouseData['lat'].mean(), HouseData['long'].mean()], zoom_start=10)
    marker_cluster = folium.MarkerCluster().add_to(house_map)
    for iters, row in data.iterrows():
        folium.Marker([row["lat"], row["long"]], 
        popup=popup_text(iters, row)).add_to(marker_cluster)
    # Save the house cluster map to a html and open it in broswer.
    house_map.save(HouseUrl)
