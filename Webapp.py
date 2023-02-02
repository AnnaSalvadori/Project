from flask import Flask, render_template, request

from Dataset import *  
from Operations import *
from Active_registry import *

def get_df():
	d = DatasetGFF3('Homo_sapiens.GRCh38.85.gff3')
	return d.dataframe

webapp = Flask(__name__)

@webapp.route('/')
def homepage():
	#df = get_df()
	#return render_template('html_homepage.html', dataframe=df)
	return render_template('html_homepage.html')
	
@webapp.route('/html_activeoperations.html')
def active_operations():
	d = Active().get_dic()
	#dic = d.get_dic()
	return render_template('html_activeoperations.html', dic = d)
	
'''possiamo usare la funzione redirect('/') o redirect('/html_activeoperations.html' se viene selezionata un'operazione non attiva')'''

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

if __name__ == '__main__':
	webapp.run(debug=True)
