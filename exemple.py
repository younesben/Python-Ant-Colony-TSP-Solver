from anttspinstance import anttspinstance # , sample, tsp
from antcolony import AntColony
from antgraph import AntGraph
import traceback,sys




"""
a=tsp.dur_matrix
b=tsp.dist_matrix
qot=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(3) :
	for j in range(3) :
		if b[i][j]!=0 :
			qot[i][j] = float(a[i][j])/float(b[i][j])
			print "(%d,%d) : %f, a : %d, b : %d " % (i,j,qot[i][j],a[i][j],b[i][j])
			
"""

def solve_tour(cost,*arg) :
	
	if cost not in ("dist","distance","duration","dur") :
		print cost,'is an invalid cost argument'
		return
	
	tsp = anttspinstance(arg)
	num_nodes = tsp.num_cities
	cities = tsp.cities
	
	
	if num_nodes <= 10:
		num_ants = 20
		num_iterations = 12
		num_repetitions = 1
	else:
		num_ants = 28
		num_iterations = 20
		num_repetitions = 1
	
	
	if cost == "dist" or cost == "distance": 
		cost_mat = tsp.dist_matrix
	elif cost == "duration" or cost == "dur":
		cost_mat = tsp.dur_matrix
	else : #this should never happen
		print cost, 'is an invalid cost argument and first verification unsuccesful'
		return

	
	if num_nodes < len(cost_mat):
		cost_mat = cost_mat[0:num_nodes]
		for i in range(0, num_nodes):
			cost_mat[i] = cost_mat[i][0:num_nodes]
	
	print cost_mat
	
	try:
		graph = AntGraph(num_nodes, cost_mat)
		best_path_vec = None
		best_path_cost = sys.maxint
		for i in range(0, num_repetitions):
			graph.reset_tau()
			ant_colony = AntColony(graph, num_ants, num_iterations)
			ant_colony.start()
			if ant_colony.best_path_cost < best_path_cost:
				best_path_vec = ant_colony.best_path_vec
				best_path_cost = ant_colony.best_path_cost
	
		print "\n------------------------------------------------------------"
		print "                     Results                                "
		print "------------------------------------------------------------"
		print "\nBest path = %s" % (best_path_vec,)
		ordered_cities = [cities[node] for node in best_path_vec]
		for city in ordered_cities :
			print city + " \n",
		print "\nBest path cost = %s\n" % (best_path_cost,)
	
	except Exception, e:
		print "exception: " + str(e)
		traceback.print_exc()
	return best_path_vec, ordered_cities, best_path_cost
	