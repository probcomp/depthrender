import numpy as np
import matplotlib.pyplot as plt
import time
from depthrender.render import Renderer

width = 64
height = 48
fx = width/3.0
fy = width/3.0
cx = width/2.0
cy = height/2.0
renderer = Renderer()
renderer.set_camera_params(width, height, fx, fy, cx, cy)

def R(angle):
    return np.transpose(np.array([
        [np.cos(angle), np.sin(angle), 0.0],
        [-np.sin(angle), np.cos(angle), 0.0],
        [0.0, 0.0, 1.0]]))

original_vertices = np.array([
        [-0.25, -0.25, 1],
        [0.25, -0.25, 1],
        [0.0, 0.25, 1],
        [-1, -1, 2],
        [1, -1, 2],
        [0, 1, 2]])

triangles = np.array([
        [0, 1, 2],
        [3, 4, 5]])

# capture depth images
depth_images = []
period = 20.0
start = time.time()
n = 100
for i in range(n):
    angle = i*2*3.1415926/period
    vertices = np.matmul(original_vertices, np.transpose(R(angle)))
    depth_image = renderer.render(vertices, triangles)
    depth_images.append(depth_image)
fps = n / (time.time() - start)
print("%d fps" % (fps,))

for (i, img) in enumerate(depth_images):
    print(i)
    plt.figure()
    plt.imshow(img)
    plt.savefig("output/depth-%03d.png" % (i,))
    plt.clf()
