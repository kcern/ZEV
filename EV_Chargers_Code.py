"""
EV_Chargers_Code.py by Kennan Cronen
Power a map of charging stations around the country

TODO: Create a quality database of regulations: 
http://developer.nrel.gov/docs/transportation/transportation-incentives-laws-v1/#!/v1.json/transportation_incentives_laws_get_3
"""

def main():
	#import stuff
	import requests
	import gmplot
	import json
	import gmaps
	"""
	#install requests
	pip install requests	
	#clone the requests code
	git clone git://github.com/kennethreitz/requests.git
	"""
	
	#############################################################
	#Request parameters
	#############################################################
	state="CA"
	limit="500"
	api_key="oxTjUFJhThYrCpnpxivQGAJDRf48nUOfVveZh0ya"
	format_type="JSON"
	fuel_type = "ELEC"
	
	# Make a get request to get the latest position of the international space station 
	# from the opennotify api.	
	response = requests.get("https://developer.nrel.gov/api/alt-fuel-stations/v1.json?"+
		"state="+state+
		"&limit="+limit+
		"&api_key="+api_key+
		"&format="+format_type+
		"&fuel_type="+fuel_type
		)
	data = response.json()
	fuel_stations = data.get("fuel_stations")
		
	#print(type(fuel_stations))
	print(str(data["total_results"]) + " Total Fuel Stations")

	#############################################################
	#Get Location Data and Create Map
	#############################################################

	Locations = [( float(i.get("latitude")),float(i.get("longitude"))) for i in fuel_stations]
	
	lats = [float(i.get("latitude")) for i in fuel_stations]
	lngs = [float(i.get("longitude")) for i in fuel_stations]
	
	#Center Map in CA
	gmap = gmplot.GoogleMapPlotter(38.58431244, -121.4956055, 6)

	#gmap.plot(lats, lngs, 'cornflowerblue', edge_width=10)
	gmap.scatter(lats, lngs, '#3B0B39', size=40, marker=False)
	gmap.scatter(lats, lngs, 'k', marker=True)
	gmap.heatmap(lats, lngs)
	gmap.draw("Kennan_EV.html")
	
	"""
	nearest station URL Query
	"""
	#nearest_station = requests.get("/api/alt-fuel-stations/v1/nearest.json?api_key=oxTjUFJhThYrCpnpxivQGAJDRf48nUOfVveZh0ya&location=1617+Cole+Blvd+Golden+CO&fuel_type=ELEC&limit=1")
	#nearest_station_data = nearest_station.json()	
	#print(type(nearest_station_data))
	#print(nearest_station_data)
	#Print the status code of the response.

if __name__ == '__main__':
	main()
