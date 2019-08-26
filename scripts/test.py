
import numpy as np

def find_vx_vy(v,x1,y1,x2,y2):
    theta = np.arctan((y2-y1)/(x2-x1))
    vx = v* np.cos(theta)
    vy = v* np.sin(theta)
    return vx,vy,x2-x1,y2-y1

print(find_vx_vy(2,23.79,19.09,38.58,8.732))
print(find_vx_vy(3,20.06,16.6066,-11.70,-17.8292))
print(find_vx_vy(2,4.137,0.063,15.227,11.564))
