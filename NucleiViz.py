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

numparticles = 10
interpstep = 100
DragonFrame = 5
rad = 5

theta = np.linspace(0,2*np.pi,interpstep)
z = np.linspace(1,numparticles,numparticles)
x = rad*np.cos(theta)
y = rad*np.sin(theta)
b = np.ones((numparticles,interpstep))
xx = b*x
yy = b*y
z = np.array(z)
z = np.reshape(z,(numparticles,1))
zz = z*b

@mlab.animate(delay = 100)
def updateAnimation(xx,yy,zz):
    t = 6
    while t<100:
        mlab.draw(figure=None)
        ball.mlab_source.set(x = xx[:,t], y =  yy[:,t], z = zz[:,t])
        
        #run calculations for dragontail data 
        if t>6:
            #dragonX = xx[:,range(t-DragonFrame,t+1)]
            #dragonY = yy[:,range(t-DragonFrame,t+1)]
            #dragonZ = zz[:,range(t-DragonFrame,t+1)]
            
            dtLB = t-DragonFrame
            dtUB = t+1
            
            
            for jj in range(0,numparticles):
                xpts = xx[jj,dtLB:dtUB]
                ypts = yy[jj,dtLB:dtUB]
                zpts = zz[jj,dtLB:dtUB]  
                dragontail[jj].mlab_source.reset(x=xpts,y=ypts,z=zpts)
            #dragontail.mlab_source.reset(x=xpts,y=ypts,z=zpts)
            #for ii in range(0,numparticles):
            #    dtLB = t-DragonFrame
            #    dtUB = t+1
            #    xpts = xx[0,dtLB:dtUB]
            #    ypts = yy[0,dtLB:dtUB]
            #    zpts = zz[0,dtLB:dtUB]
             #   mlab.plot3d(xpts,ypts,zpts)
             #   print(ii)
                        
        t += 1
        if t == interpstep-1:
            t = 0
        yield
        

#set background color to black and plot
mlab.figure(figure=None,bgcolor = (0,0,0))
ball = mlab.points3d(xx[:,0], yy[:,0], zz[:,0],scale_factor = 0.8,color=(0.2, 0.4, 0.5))
t = 6
dtLB = t-DragonFrame
dtUB = t+1

dragontail = []

for j in range(0,numparticles):
    
    xpts = xx[j,dtLB:dtUB]
    ypts = yy[j,dtLB:dtUB]
    zpts = zz[j,dtLB:dtUB]
    dragontail.append(mlab.plot3d(xpts,ypts,zpts, color=(1,0,0), tube_radius=0.05))
    
#dragontail = mlab.plot3d(np.zeros((1,DragonFrame+1)),np.zeros((1,DragonFrame+1)),np.zeros((1,DragonFrame+1)))
t = np.linspace(0, 100,100)
#mlab.plot3d(np.sin(t), np.cos(t), 0.1*t, t,tube_radius =0.05)
mlab.outline(extent = [-rad,rad,-rad,rad,0,numparticles])
updateAnimation(xx,yy,zz)

#mlab.savefig(filename = 'HelloAnimation!.png')
mlab.show()
