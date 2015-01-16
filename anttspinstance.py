import urllib2,json



class anttspinstance : 
	
	def __init__(self, stops):
		if len(stops) < 3 :
			#print "TSP doesn't make sens with " + str(len(stops)) + " stop(s)."
			print "TSP doesn't make sens with %d stop(s)." % len(stops)
		else : 
			self.origins = self.get_stops_string(stops)
			#url="https://maps.googleapis.com/maps/api/distancematrix/json?origins=" + origins + "&destinations=" + origins
			url="https://maps.googleapis.com/maps/api/distancematrix/json?origins=%s&destinations=%s" % (self.origins,self.origins)
			response = urllib2.urlopen(url)
			jsongeocode = response.read()
			self.data = json.loads(jsongeocode)
			self.cities = self.data['destination_addresses']
			self.num_cities = self.parse_num_cities()
			self.dist_matrix = self.parse_dist_matrix()
			self.dur_matrix = self.parse_dur_matrix()
		
	def parse_num_cities(self):
		return len(self.data['destination_addresses'])
		
		
	def parse_dur_matrix(self):
		matrix = [ [self.data['rows'][i]['elements'][j]['duration']['value']  
						for i in range(len(self.data['destination_addresses'])) 
				   ]	for j in range(len(self.data['destination_addresses']))
				 ]
		return matrix


	def parse_dist_matrix(self):
		matrix = [ [self.data['rows'][j]['elements'][i]['distance']['value'] 
						for i in range(len(self.data['destination_addresses'])) 
				   ]	for j in range(len(self.data['destination_addresses']))
				 ]
		return matrix
		
	def get_stops_string(self,arrets):
		ar = ""
		for arg in arrets : 
			print str(arg),"is of type",type(arg) 
			ar+= arg + '|'
		return ar[:-1]
		
		
		
"""		Sample exemple 									"""		
#sample = ("Noisy-le-Grand", "Villeparisis", "Paris")

#tsp = anttspinstance(sample)	
