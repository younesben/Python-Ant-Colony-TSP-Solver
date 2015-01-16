from exemple import solve_tour

cost = "dur"
#best_path_vec, ordered_cities, best_path_cost = solve_tour(cost,"Paris", "||||Pan|tin", "Bruxelles", "Lille","Londres","Amsterdam")
best_path_vec, ordered_cities, best_path_cost = solve_tour(cost,
"Noisy-Le-Grand", 
"Chelles", 
"Montreuil", 
"Rosny",
"Villemomble",
"Saint-Denis", 
"Courbevoie",
"L'ile_saint-denis",
"Champigny",
"Trappes")

if cost in ("dist","distance") : 
	print "Minimun distance is ", best_path_cost/1000, "km(s)"
elif cost in ("dur","duration") : 
	print "Minimun time is ", best_path_cost/60, "min(s)"
	
# dur 	[5, 7, 6, 9, 8, 0, 1, 4, 3, 2]
#dist 	[8, 0, 1, 4, 3, 2, 5, 7, 6, 9]