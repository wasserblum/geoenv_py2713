__author__ = 'lnx'
import numpy as np
import matplotlib.pyplot as plt
import gdal
import sys
gdal.UseExceptions() # this allows GDAL to throw Python Exceptions
import scipy
#import random

##read georeferenced rasters of relevant information
#LCZ = ...
#LCZ_new = .... #LCZ with densificated properties (height + 3m)
MASK1 = gdal.Open("D:/_URBANIA/GEODATA/PGO/stadtregionp45_Baulandreserve_georef2.tif") #PGO_FreeScenario
MASK2a = gdal.Open("D:/_URBANIA/GEODATA/PGO/stadtregionp46_StrukturierteStadtregion_georef.tif") #PGO_Structured
#MASK2b = D:/_URBANIA/GEODATA/STEP05/GRUENFREILOGD_GRUENGEWOGD# STEP05_Gruen
#MASK2c = # STEP25_built
#MASK2d = # STEP25_green?
#MASK1 = none #close dataset

MASK1_array = MASK1.ReadAsArray()
print MASK1_array

#plt.hist2d(lc[0],lc[1])
plt.imshow(MASK1_array)#,interpolation='nearest', vmin=0 )#, cmap=plt.cm.gist_earth)
#plt.colorbar()
plt.show()


print MASK1.GetMetadata()

#test = random.sample([[1,2],[3,4],[5,6]], 1)
#print test


##parameters:
pixelsize = 111
LCZ_builtratio = 0.5
BWGF_add = 1000000 #Bruttowohngeschossflaeche
SplitFactor = 0.7

#actual Bruttowohngeschossflaeche
BWGF = pixelsize**2 * LCZ_builtratio

#new BWGF is  split in densification and urban expansion
BWGF_densification = BWGF_add*SplitFactor
BWGF_extension = BWGF_add*(1-SplitFactor)

######

#3) Assumption: random distribution on all built categories
SP = np.random.randint(0, 10, (3,3))

#weighting = ... #raster with development priorities for growth
SP_ran = np.random.randint(0, 2, (3,3))

#import random
#i = random.choice(SP)
#print random.choice(i)

#random.sample(population, k)
#SP_adddensif = np.random.sample(SP,BWFG_Nr)

print SP
print SP_ran
SP_new = SP
for i in range(len(SP)):
    for j in range(len(SP[i])):
        SP_new[i][j] = SP[i][j]+SP_ran[i][j]
print SP_new

plt.matshow(SP_new)
plt.show()





