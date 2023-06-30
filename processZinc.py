import requests
import json
import os
from tqdm import tqdm
from rdkit import Chem
from rdkit.Chem import Draw, Descriptors




def download_zinc():
    with open('./data/ZINC-downloader-2D-txt.uri','r') as f:
        sources = f.readlines()
        
    for _,source in enumerate(tqdm(sources)):
        section = source.split('/')[-1].split('.')[0]
        if os.path.exists(f'./data/{section}.csv'):
            continue
        response = requests.get(source.strip())
        data = response.text.split('\n')
        with open(f'./data/{section}.csv','w') as f:
            for item in data:
                row = item.replace('\r','').split('\t')
                features = '' if len(row) < 8 else row[8].replace(',',';')
                if len(row) < 8:
                    continue
                f.write(f'{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]},{row[5]},{row[6]},{row[7]},{features}\n')

def summarize_zinc():
    summary_str = 'file, count\n'
    for idx,f in enumerate(tqdm(os.listdir('./data'))):
        if not f.endswith('csv'):
            continue
        with open(f'./data/{f}','r') as t:
            data = t.readlines()
        summary_str += f'{f},{len(data)}\n' 

    with open('./data/summary.csv','w') as summary:
        summary.write(summary_str)

def process_molecule(smile,zinc_id):
    

    mol = Chem.MolFromSmiles(smile)

    descriptors = Descriptors.CalcMolDescriptors(mol)

    # Draw.MolToFile(mol,f'./Images/mols/{zinc_id}.png')

    return descriptors

def get_descriptors():
    with open('./data/summary.csv','r') as f:
        data = f.readlines()
    
    molecules = {}
    for idx,item in enumerate(tqdm(data)):
        if idx == 0:
            continue
        try:
            with open(f'./data/{item.split(",")[0]}','r') as f:
                molecule_data = f.readlines()
        except:
            continue
        molecule = molecule_data[1].split(',')
        descriptors = process_molecule(molecule[0],molecule[1])
        #smiles, zinc_id, inchikey, mwt, logp,reactive,purchasable,tranche_name,features
        molecules[molecule[1]] =  {
            'smile':molecule[0],
            'inchikey':molecule[2],
            'mwt':molecule[3],
            'logp':molecule[4],
            'reactive':molecule[5],
            'purchasable':molecule[6],
            'tranche_name':molecule[7],
            'features':molecule[8],
            'descriptors':descriptors
        }
        
    json.dump(molecules,open('./molecules.json','w'))

if __name__ == '__main__':
    
    get_descriptors()