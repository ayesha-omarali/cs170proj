# rough pseudo code because it's late and I don't 
# really quite know python well enough to write this correctly

import sys

class solutions:

	def __init__(self, instances, sol_file_object):
		#given zip file of instances
		self.instances = instances



		#no clue if this is right
		for instance in self.instances:
			self.instance = instance
			#or maybe self.instance = analyze_instance(instance) idk?

			self.instance_name = self.instance.readline() #so i can write to corresponding line.
			#https://docs.python.org/2/library/stdtypes.html#str.format 
			# -- string format crap that i pulled crap from

	shit_to_write = []

	def read_instances(instances):

		#validate instances
		scc_lst = []
		for instance in instances:
			instance_validator()

			analyze_instance(instance)

	
	def analyze_instance(instance):		
		scc_lst = SCCMaker(instance)

		for scc in scc_lst:
			#organize crap within SCCs
			scc = bellman_ford(topological_sort(scc))

			scc = all_orderings(scc)

			###this is definitely wrong because I don't follow Apollo's code that great
			### but essentially implement eff cycle anal such that 
			### as we iterate through each SCC in the instance, we end up with the best path of each SCC
			### then after compare the best of each SCC in it's own list with probs brute force that Apollo wrote
			## THEN we save that shit to the shit_to_write list, so we can make an easy writing shit function output.
			loose_approx = efficient_cycle_analysis_49(scc, instance)

			tight_approx = efficient_cycle_analysis(loose_approx, instance) #i have no idea if this is done properly... 

			shit_to_write.append([instance.instance_name, tight_approx])

	def write_sol(shit_to_write):
		sol = open(sol_file_object)

		for shit in shit_to_write:
			int(sol.writeline(shit[1]'\n').split()[0]) #need to figure out how to ensure solution i is on the ith line






