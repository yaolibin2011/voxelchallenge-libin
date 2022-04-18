from scene import Scene
import taichi as ti
from taichi.math import *

scene = Scene(exposure=5)
scene.set_floor(-0.03, (0.0, 0.6, 0.2))
scene.set_background_color((0.0, 0.6, 0.2))


@ti.kernel
def initialize_voxels():
    scene.set_voxel(vec3(0, 0, 0), 2, vec3(0.0, 0.6, 0.2))

  
    for i in range(1, 50):
         scene.set_voxel(vec3(0, i, 0), 2, vec3(0.0, 0.6, 0.2))
        
    for j in range(1, 50):
         scene.set_voxel(vec3(0, 0, j), 2, vec3(1.0, 0.6, 0.0))   
         
    for k in range(1, 50):
         scene.set_voxel(vec3(k, 0, 0), 2, vec3(0.4, 0.4, 1.0))       

initialize_voxels()

scene.finish()
