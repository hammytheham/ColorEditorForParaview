#!/usr/bin/env python

###################################
# Created by Hamish Robertson #####
# For use with Python2.7 ##########
###################################

import numpy as np

############################################################
# 1. Add your data refinement in VarA-D in format of VarX ##
# This example goes from 30 to 183 in 4 increments with ####
# highest resolution around 108 to 120. ####################
# If adding extra ranges (or using less) then modify line ##
# begining valrange. #######################################
############################################################

VarA=np.arange(30,75,3)
VarB=np.arange(75,108,0.29)
VarC=np.arange(108,120,0.1)
VarD=np.arange(122,184,10)
#VarX=np.arrange(start,stop,step)

valrange=(np.concatenate([VarA,VarB,VarC,VarD])).flatten()

print 'Change data refinements if %d is not 256' % (np.size(valrange))

#######################################################
# 2. Edit the two Paths to those of the supplied B&W ##
# Colormap and to the location of your new colormap ###
#######################################################

with open('PATH_TO_BW_ColorMap.json','r') as infile: #Edit here
    lista=[]
    for i in infile:
        lista.append(i)
    firstline=np.array(lista[6:1034:4])
    secondline=np.array(lista[7:1034:4])
    thirdline=np.array(lista[8:1034:4])
    prologuelines= np.array(lista[0:5:1])
    postloglines=np.array(lista[-4:-1])
    with open('PATH_TO_NEW_Modified_BW_ColorMap.json','w') as outfile: #Edit here
        for i in prologuelines:
            outfile.write(i)
        for i in range(0,256):
            outfile.write('         '+ str(valrange[i]) + ',' + '\n' )
            outfile.write(str(firstline[i]))
            outfile.write(str(secondline[i]))
            outfile.write(str(thirdline[i]))
        for i in postloglines:
            outfile.write(i)
    outfile.close()
infile.close()

