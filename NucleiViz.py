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

xx = pd.read_csv('C:\Users\zjner\Desktop\w18_Xdata.csv')
yy = pd.read_csv('C:\Users\zjner\Desktop\w18_Ydata.csv')
zz = pd.read_csv('C:\Users\zjner\Desktop\w18_Zdata.csv')
xx = np.array(xx)
yy = np.array(yy)
zz = np.array(zz)

timesize = np.size(xx,axis=1)
print(timesize)

@mlab.animate(delay = 100)
def updateAnimation(xx,yy,zz):
    t = 0
    while t<timesize:
        mlab.draw(figure=None)
        ball.mlab_source.set(x = xx[:,t], y =  yy[:,t], z = zz[:,t])
        
        
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
            t = 0
        yield
        

#set background color to black and plot
mlab.figure(figure=None,bgcolor = (0,0,0))
ball = mlab.points3d(xx[:,0], yy[:,0], zz[:,0],scale_factor = 8, color=(0.85,0,0))
t = 6
dtLB = t-DragonFrame
dtUB = t+1

dragontail = []
DTx = []
DTy = []
DTz = []

#for j in range(0,numparticles):
#    DTx.append(np.ones((5,1))*xx[j,0])
#    DTy.append(np.ones((5,1))*yy[j,0])
#    DTz.append(np.ones((5,1))*zz[j,0])

#    dragontail.append(mlab.plot3d(DTx[j],DTy[j],DTz[j], color=(1,0,0), tube_radius=0.05))
    
#dragontail = mlab.plot3d(np.zeros((1,DragonFrame+1)),np.zeros((1,DragonFrame+1)),np.zeros((1,DragonFrame+1)))
t = np.linspace(0, 100,100)
#mlab.plot3d(np.sin(t), np.cos(t), 0.1*t, t,tube_radius =0.05)
mlab.outline(extent = [np.nanmin(xx),np.nanmax(xx),np.nanmin(yy),np.nanmax(yy),np.nanmin(zz),np.nanmax(zz)])
#mlab.outline(extent = [0,500,0,500,0,50])

updateAnimation(xx,yy,zz)

#mlab.savefig(filename = 'HelloAnimation!.png')
mlab.show()
