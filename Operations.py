import pandas as pd
from Active_registry import *




'Getting the some basic information about the dataset. The basic information are the name and data type of each column'
@active_decorator
def info(df):
    res = pd.DataFrame([], columns=["Name", "Type"])
    for i in df: 
        next = pd.DataFrame([[i, [x for x in df[i].apply(type).unique()]]], columns=["Name", "Type"])
        res = pd.concat(objs=[res, next], ignore_index = True)
    return res
    

'Obtaining the list of unique sequence IDs available in the dataset'
@active_decorator
def seqID(df):
    return pd.DataFrame(data = df['seq_id'].unique(), columns=['seqID'])

    
'obtaining the list of unique type of operations available in the dataset'
@active_decorator
def type_operation(df):
    return pd.DataFrame(data = df['type'].unique(), columns=['type'])


'counting the number of features provided by the same source'
@active_decorator
def count_features(df): 
    counts = df['source'].value_counts()
    sources = counts.index.tolist()
    res = pd.DataFrame(data = [], columns=['Source', 'Count'])
    for i in range(counts.size):
        next = pd.DataFrame(data = [[sources[i], counts[i]]], columns=['Source', 'Count'])
        res = pd.concat([res, next], ignore_index=True)
    return res


'counting the number of entries for each type of operation'
@active_decorator
def count_entries(df):
    counts = df['type'].value_counts()
    types = counts.index.tolist()
    res = pd.DataFrame(data = [], columns=['Type', 'Count'])
    for i in range(counts.size):
        next = pd.DataFrame(data = [[types[i], counts[i]]], columns=['Type', 'Count'])
        res = pd.concat([res, next], ignore_index=True)
    return res


'Deriving a new dataset containing only the information about entire chromosomes. Entries with entire chromosomes comes from source GRCh38'
@active_decorator
def entire_chromosome(df): 
    new_df = df.loc[df['source'] == 'GRCh38']
    return new_df.loc[df['type'] == 'chromosome']


'Calculating the fraction of unassembled sequences from source GRCh38. Hint: unassembled sequences are of type supercontig while the others are of chromosome'
@active_decorator
def count_supercontigs(df):
    new_df = df.loc[df['source'] == 'GRCh38']
    return pd.DataFrame(data = [new_df['type'].value_counts(normalize = True).supercontig], columns = ['Fraction'])


# ? specific_entries
'obtaining a new dataset containing only entries from source ensembl , havana and ensembl_havana'
@active_decorator
def entries_ens_hav_enshav(df): 
    a = [True if i in ['ensembl', 'havana', 'ensembl_havana' ] else False for i in df['source']]
    return df.loc[a]


# ? count_specific_entries
'counting the number of entries for each type of operation for the dataset containing containing only entries from source ensembl , havana and ensembl_havana'
@active_decorator
def count_entries_ens_hav_enshav(df): 
    a = [True if i in ['ensembl', 'havana', 'ensembl_havana' ] else False for i in df['source']]
    new_df = df.loc[a]
    counts = new_df['type'].value_counts()
    sources = counts.index.tolist()
    res = pd.DataFrame(data = [], columns=['Operation', 'Count'])
    for i in range(counts.size):
        next = pd.DataFrame(data = [[sources[i], counts[i]]], columns=['Operation', 'Count'])
        res = pd.concat([res, next], ignore_index=True)
    return res


'returning the gene names from the dataset containing containing only entries from source ensembl , havana and ensembl_havana'
@active_decorator
def gene_names(df):
    new_df = df.loc[df['type'] == 'gene']
    res = pd.DataFrame(data = [], columns = ['Names'])
    for i in new_df['attributes']:
        name = i[i.index('Name=')+ 5:]
        name =  pd.DataFrame(data = [name[:name.index(';')]], columns = ['Names'])
        res = pd.concat([res, name], ignore_index=True )
    return res




# operations() does not belong to the requested operations. do we keep it here anyway?
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

