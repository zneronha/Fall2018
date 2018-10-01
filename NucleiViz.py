# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 15:42:03 2018

@author: ZNERONHA
"""

import numpy as np
from mayavi import mlab

numparticles = 10

theta = np.linspace(0,2*np.pi,100)
z = np.linspace(1,numparticles,numparticles)
x = 5*np.cos(theta)
y = 5*np.sin(theta)
b = np.ones((numparticles,100))
xx = b*x
yy = b*y

s3 = 0.5*np.ones((numparticles,1))+0.05*np.random.randn(numparticles,1)


z = np.array(z)
z = np.reshape(z,(numparticles,1))
zz = z*b

@mlab.animate(delay = 100)
def updateAnimation(xx,yy,zz):
    t = 1
    while True:
        ball.mlab_source.set(x = xx[:,t], y =  yy[:,t], z = zz[:,t])
        t += 1
        if t == 99:
            t = 0
        yield

ball = mlab.points3d(xx[:,0], yy[:,0], zz[:,0],scale_factor = 0.6,color=(0.2, 0.4, 0.5))


updateAnimation(xx,yy,zz)
mlab.show()