# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 11:26:03 2018

@author: ZNERONHA
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 15:42:03 2018

@author: ZNERONHA
"""

import numpy as np
from mayavi import mlab
import pandas as pd
from tvtk.api import tvtk
from tvtk.common import configure_input_data

numparticles = 10

interpstep = 100
DragonFrame = 5
rad = 5



#theta = np.linspace(0,2*np.pi,interpstep)
#z = np.linspace(1,numparticles,numparticles)
#x = rad*np.cos(theta)
#y = rad*np.sin(theta)
#b = np.ones((numparticles,interpstep))
#xx = b*x
#yy = b*y
#z = np.array(z)
#z = np.reshape(z,(numparticles,1))
#zz = z*b

#p = np.empty((9,20))
#p[:] = np.nan
#xx[1:10,0:20] = p
#yy[1:10,0:20] = p
#zz[1:10,0:20] = p

xlsZ = pd.ExcelFile('C:\Users\zjner\Desktop\ConvertedData\w18_combineddata.xls')
dxx = pd.read_excel(xlsZ,'xStore')
dyy = pd.read_excel(xlsZ,'yStore')
dzz = pd.read_excel(xlsZ,'zStore')
xx = np.array(dxx)
yy = np.array(dyy)
zz = np.array(dzz)

#xx = pd.read_csv('C:\Users\zjner\Desktop\w18_Xdata.csv')
#yy = pd.read_csv('C:\Users\zjner\Desktop\w18_Ydata.csv')
#zz = pd.read_csv('C:\Users\zjner\Desktop\w18_Zdata.csv')
#xx = np.array(xx)
#yy = np.array(yy)
#zz = np.array(zz)

numparticles = np.int64(np.size(xx,axis=0))
timesize = np.int64(np.size(xx,axis=1))
print(timesize)

@mlab.animate(delay = 100)
def updateAnimation(xx,yy,zz,xT,yT,zT):
    t = 0
    while t<timesize:
        mlab.draw(figure=None)
        ball.mlab_source.set(x = xx[:,t], y =  yy[:,t], z = zz[:,t])
        
        
       #redefine the dragontail matrix
        for j in range(0,numparticles):
            oxR = range(0,5)
            for updateN in oxR[4:None:-1]:
                if updateN>0:
                    xT[j][updateN] = xT[j][updateN-1]
                    yT[j][updateN] = yT[j][updateN-1]
                    zT[j][updateN] = zT[j][updateN-1]
                else:
                    xT[j][updateN] = xx[j,t]
                    yT[j][updateN] = yy[j,t]
                    zT[j][updateN] = zz[j,t]
                    
            dragontail[j].mlab_source.reset(x = xT[j],y = yT[j], z = zT[j])  
        
 #       for k in range(0,np.size(xx,axis=0)):
 #           text[k].mlab_source.reset(x = xx[k,t], y = yy[k,t], z = zz[k,t])

        
        #for j in range(0,numparticles):
        #    for update in reversed(range(0,DragonFrame)):
        #        if update>0:
        #            DTx[update] = DTx[update-1]
        #            DTy[update] = DTy[update-1]
        #            DTz[update] = DTz[update-1]
        #        else: 
        #                DTx[update] = xx[]
            
        
        #run calculations for dragontail data 
        #if t>6:            
        #    dtLB = t-DragonFrame
        #    dtUB = t+1
        #    
        #   for jj in range(0,numparticles):
        #        xpts = xx[jj,dtLB:dtUB]
        #        ypts = yy[jj,dtLB:dtUB]
        #        zpts = zz[jj,dtLB:dtUB]  
        #        dragontail[jj].mlab_source.reset(x=xpts,y=ypts,z=zpts)
                        
        t += 1
        if t == interpstep-1:
            xT = xds
            yT = yds
            zT = zds
            t = 0
        yield
        

#set background color to black and plot
v = mlab.figure(figure=None,bgcolor = (0,0,0))
ball = mlab.points3d(xx[:,0], yy[:,0], zz[:,0],scale_factor = 6, color=(0,1,1))
#text = list()
#for k in range(0,np.size(xx,axis=0)):
#    text.append(mlab.text3d(xx[k,0], yy[k,0], zz[k,0],'cell ' + repr(k),scale=(5,5,5)))

# The Property will give the parameters of the material.
#p = tvtk.Property(opacity=0.2, color=(0, 1, 1))
# The actor is the actually object in the scene.
#sphere_actor = tvtk.Actor(mapper=sphere_mapper, property=p)
#v.scene.add_actor(sphere_actor)

#b = mlab.text3d(0,0,0,'hello world',scale=(2,2,2))

dragontail = []
xT = []
yT = []
zT = []

for j in range(0,numparticles):
    xn = np.zeros((DragonFrame,1))
    yn = np.zeros((DragonFrame,1))
    zn = np.zeros((DragonFrame,1))
    xn = xn*np.nan
    yn = yn*np.nan
    zn = zn*np.nan
    xn[0] = xx[j,0]
    yn[0] = yy[j,0]
    zn[0] = zz[j,0]

    xT.append(xn)
    yT.append(yn)
    zT.append(zn)    
    dragontail.append(mlab.plot3d(list(xn),list(yn),list(zn),color=(1,0,0), tube_radius=0.05))

xds = xT
yds = yT
zds = zT

t = np.linspace(0, 100,100)
#mlab.plot3d(np.sin(t), np.cos(t), 0.1*t, t,tube_radius =0.05)
mlab.outline(extent = [np.nanmin(xx),np.nanmax(xx),np.nanmin(yy),np.nanmax(yy),np.nanmin(zz),np.nanmax(zz)])
#mlab.outline(extent = [0,500,0,500,0,50])

updateAnimation(xx,yy,zz,xT,yT,zT)

#mlab.savefig(filename = 'HelloAnimation!.png')
mlab.show()
