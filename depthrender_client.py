from __future__ import print_function
import logging

import numpy as np
import matplotlib.pyplot as plt
import time

import grpc
import depthrender_pb2
import depthrender_pb2_grpc

num_vertices = 300
num_triangles = 100
vertices = np.random.rand(num_vertices, 3)
triangles = np.random.randint(0, num_vertices, (num_triangles, 3))

def R(angle):
    return np.transpose(np.array([
        [np.cos(angle), np.sin(angle), 0.0],
        [-np.sin(angle), np.cos(angle), 0.0],
        [0.0, 0.0, 1.0]]))

def run():
    depth_images = []
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = depthrender_pb2_grpc.DepthRenderStub(channel)
        start = time.time()
        n = 1000
        period = 100.0

        # set params
        width = 640
        height = 480
        fx = width/3.0
        fy = width/3.0
        cx = width/2.0
        cy = height/2.0
        response = stub.SetCameraParams(depthrender_pb2.SetCameraParamsRequest(
            width=width, height=height,
            fx=fx, fy=fy,
            cx=cx, cy=cy))
        
        for i in range(n):
            print(i)
            t = time.time() - start
            angle = i * 2 * 3.1415926 / period

            num_vertices = np.random.randint(300, 900)
            num_triangles = np.random.randint(100, 200)
            vertices = np.random.rand(num_vertices, 3)
            vertices[:,0:2] = 0.5 * (vertices[:,0:2] - 0.5)
            vertices[:,2] = (vertices[:,2] * 0.5) + 1.0 # in front of camera
            triangles = np.random.randint(0, num_vertices, (num_triangles, 3))
            response = stub.RenderDepthImage(depthrender_pb2.RenderDepthImageRequest(
                num_vertices=num_vertices,
                num_triangles=num_triangles,
                vertices=vertices.tobytes(),
                triangles=triangles.tobytes()))
            depth_image = np.reshape(np.frombuffer(response.depth_image, dtype=np.float32), (height, width))
            depth_images.append(depth_image)
        fps = n / (time.time() - start)
        print("%d fps" % (fps,))
        
    # now save some of them to disk
    for (i, img) in enumerate(depth_images[0:20]):
        print(i)
        plt.figure()
        plt.imshow(img)
        plt.savefig("output/depth-%03d.png" % (i,))
        plt.clf()

if __name__ == '__main__':
    logging.basicConfig()
    run()
