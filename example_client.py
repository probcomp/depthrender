from __future__ import print_function
import logging

import numpy as np
import matplotlib.pyplot as plt
import time

import grpc
from depthrender.depthrender_pb2 import SetCameraParamsRequest
from depthrender.depthrender_pb2 import RenderDepthImageRequest
from depthrender.depthrender_pb2_grpc import DepthRenderStub

def R(angle):
    return np.transpose(np.array([
        [np.cos(angle), np.sin(angle), 0.0],
        [-np.sin(angle), np.cos(angle), 0.0],
        [0.0, 0.0, 1.0]]))

vertices = np.array([
        [-0.25, -0.25, 1],
        [0.25, -0.25, 1],
        [0.0, 0.25, 1],
        [-1, -1, 2],
        [1, -1, 2],
        [0, 1, 2]])

triangles = np.array([
        [0, 1, 2],
        [3, 4, 5]])

def run():
    depth_images = []
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = DepthRenderStub(channel)
        start = time.time()
        n = 100
        period = 20.0

        # set params
        width = 64
        height = 48
        fx = width/3.0
        fy = width/3.0
        cx = width/2.0
        cy = height/2.0
        response = stub.SetCameraParams(SetCameraParamsRequest(
            width=width, height=height,
            fx=fx, fy=fy,
            cx=cx, cy=cy))
        
        for i in range(n):
            t = time.time() - start
            angle = i * 2 * 3.1415926 / period
            rotated_vertices = np.matmul(vertices, np.transpose(R(angle)))
            num_vertices = vertices.shape[0]
            num_triangles = triangles.shape[0]
            response = stub.RenderDepthImage(RenderDepthImageRequest(
                num_vertices=num_vertices,
                num_triangles=num_triangles,
                vertices=rotated_vertices.tobytes(),
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
