import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np 
#from IPython.display import display

df = pd.read_csv('chandra_sources_v2.csv')
#df = pd.read_csv('chandra_var_sources.csv' )
df.index.name='index'
df.insert(0 , 'class' , ['']*len(df))
df.insert(1,'catalog' , ['']*len(df))
df.insert(2,'cat_name' , ['']*len(df))
df.insert(3,'cat_ra' , [0.0]*len(df))
df.insert(4,'cat_dec' , [0.0]*len(df))
df.insert(5,'offset' , [0.0]*len(df))
df.insert(0 , 'csc_index' , ['CSC_'+ str(n) for n in range(len(df))])
df 


from astropy.coordinates import SkyCoord
import astropy.units as u

plt.figure(figsize=(12,10))
#plt.subplot(111, projection='aitoff' ,)
plt.subplot(111)
plt.grid(True)

eq = SkyCoord(df['ra'] , df['dec'] , unit = u.deg)
gal = eq.galactic
plt.scatter(gal.l.wrap_at('180d').radian, gal.b.radian , s=1 , marker='x' , color='b')



gc  = pd.read_csv('gc_cat.csv' , delimiter=',')
eq = SkyCoord(gc['RA(2000)'] , gc['DEC'] , unit = (u.hourangle, u.deg))

gal = eq.galactic
plt.scatter(gal.l.wrap_at('180d').radian, gal.b.radian , s=40 , alpha=0.2 , color='r')

plt.title('CSC 2.0 variable Point sources')
plt.show()

#plt.hexbin(gal.l.wrap_at('180d').radian, gal.b.radian ,)
#plt.colorbar()
