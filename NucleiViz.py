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
def updateAnimation(xx,yy,zz,xT,yT,zT):
    t = 0
    while t<100:
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
    dragontail.append(mlab.plot3d(xn,yn,zn,color=(1,0,0), tube_radius=0.05))
    
#dragontail = mlab.plot3d(np.zeros((1,DragonFrame+1)),np.zeros((1,DragonFrame+1)),np.zeros((1,DragonFrame+1)))
t = np.linspace(0, 100,100)
#mlab.plot3d(np.sin(t), np.cos(t), 0.1*t, t,tube_radius =0.05)
mlab.outline(extent = [-rad,rad,-rad,rad,0,numparticles])
updateAnimation(xx,yy,zz,xT,yT,zT)

#mlab.savefig(filename = 'HelloAnimation!.png')
mlab.show()
