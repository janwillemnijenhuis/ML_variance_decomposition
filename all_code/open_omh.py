import pickle
import os
from IPython.display import display
import pandas as pd
import numpy as np

path = os.getcwd()
os.chdir(os.path.join(path,'5_application/results_OMH'))
facet=[2,3]
exp = 1
types = ['depth','trees']
nums = ['1000','all']

for i in range(6):
    exp = i+1
    m=0
    gcoefs = []
    varcomps = []
    for j in facet:
        facets=j
        for k in types:
            type2=k
            for n in nums:
                numobs = n
                if (facets==2):
                    pathname = 'exp'+str(exp)+'_results_'+str(facets)+'_seed_'+numobs
                else:
                    pathname = 'exp'+str(exp)+'_results_'+str(facets)+'_seed_'+type2+'_'+numobs

                
                path = os.getcwd()
                newpath = os.path.join(path,pathname)
                os.chdir(newpath)
                files = os.listdir(newpath)
                for p in files:
                    if('omh_var_components' in p):
                        with open(p,'rb') as file:
                            varcomps.append(pickle.load(file))
                    elif('omh_g_cofficients' in p):
                        with open(p,'rb') as file:
                            gcoefs.append(pickle.load(file))
                m+=1
                os.chdir(path)
        data1 = pd.Series(gcoefs)
        data2 = pd.Series(varcomps)
        data = pd.concat([data1,data2],keys=['g','v'])
        df=pd.DataFrame(data)
        df.to_excel('results_exp'+str(exp)+'_'+str(facets)+'_facets.xlsx')  
          
                    

