from flask import Flask, render_template, request

from Dataset import *  
from Operations import *
from Active_registry import *

def get_df():
	d = DatasetGFF3('Homo_sapiens.GRCh38.85.gff3')
	return d.dataframe


def operations():
	dic = {'info': info,
		'seqID': seqID,
		'type_operation':type_operation,
		'count_features': count_features,
		'count_entries':count_entries,
		'entire_chromosome': entire_chromosome,
		'count_supercontigs': count_supercontigs,
		'entries_ens_hav_enshav': entries_ens_hav_enshav,
		'count_entries_ens_hav_enshav':count_entries_ens_hav_enshav,
		'gene_names': gene_names}  
	return dic


webapp = Flask(__name__)

@webapp.route('/')
def homepage():
	return render_template('html_homepage.html')
	
@webapp.route('/html_activeoperations.html')
def active_operations():
	d = Active().get_dic()
	return render_template('html_activeoperations.html', dic = d)

@webapp.route('/html_operation.html')
def operation():
	selected = request.args.get("select_operation")
	s = operations()[selected]
	df = get_df()
	output = s(df)
	return render_template('html_operation.html', selection = selected, out = output)
	
@webapp.route('/html_projectdocumentation.html')
def project_documentation():
	return render_template('html_projectdocumentation.html')

@webapp.route('/html_database.html')
def database():
	df = get_df()
	return render_template('html_database.html', dataframe = df)
	
@webapp.route('/html_alloperations.html')
def alloperations():
	return render_template('/html_alloperations.html')

if __name__ == '__main__':
	webapp.run(debug=True)
