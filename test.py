import os
print(os.getcwd())
currdir = './webproject/static/Images/mols'
for f in os.listdir(currdir):
    os.rename(os.path.join(currdir,f),os.path.join(currdir,f.strip()))
