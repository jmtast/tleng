import numpy as NP
from numpy import array

result = {'color': array([0, 1, 1]), 'translation': array([[ 0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.]]), 'type': 'box', 'depth': 100, 'space': array([[ 2.44948974,  0.5       ,  0.61237244,  0.        ],
       [-1.56030387,  0.86483855, -0.31606175,  0.        ],
       [-2.75053664, -0.04532427,  0.72464127,  0.        ],
       [ 0.        ,  0.        ,  0.        ,  1.        ]])}

position = NP.dot(NP.array([0,0,0,1]), result['space'])[:3]
dirx = NP.dot(NP.array([1,0,0,0]), result['space'])[:3]
diry = NP.dot(NP.array([0,1,0,0]), result['space'])[:3]
dirz = NP.dot(NP.array([0,0,1,0]), result['space'])[:3]
color= result['color']
print "position:",position
print "dirx:",dirx
print "diry:",diry
print "dirz:",dirz
print "color:",color

print NP.array([1,2,4,8])

size = NP.array([NP.linalg.norm(dirx),NP.linalg.norm(diry),NP.linalg.norm(dirz)])
print size

import visual as visual
visual.box(pos=position, size=size, axis=dirx, up=diry, color=color)
color[0]=1
color[2]=0
#position[0] = 1
#position[1] = 1
position[2] += 1
print color
visual.ellipsoid(pos=position, size=size, axis=dirx, up=diry, color=color)