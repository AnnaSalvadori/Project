class Active:
	def __init__ (self):
		self.__d = {
            'info': True,
            'seqID' : True,
            'type_operation' : True,
            'count_features' : True,
            'count_entries' : True,
            'entire_chromosome' : True,
            'count_supercontigs' : True,
            'entries_ens_hav_enshav' : False,
            'count_entries_ens_hav_enshav' : True,
            'gene_names' : True
        }
        
	def get_dic(self):
		return self.__d  
        
def active_decorator(function):
	act = Active()
	def activation(*arg):
		name = str(function).split()[1]
		if act.get_dic()[name]:
			return function(*arg)
		else: 
			return f'The operation {name} is not active'

	return activation