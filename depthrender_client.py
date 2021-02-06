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
        for i in range(n):
            t = time.time() - start
            angle = i * 2 * 3.1415926 / period
            # NOTE: here, we just rotate the vertices, but, we can actually set
            # arbitrary new vertex and triangle data here
            # vertices are float32 n x 3
            # trangles are int32 n x 3
            new_vertices = np.matmul(vertices, np.transpose(R(angle)))
            new_triangles = triangles
            response = stub.RenderDepthImage(depthrender_pb2.RenderDepthImageRequest(
                num_vertices=num_vertices,
                num_triangles=num_triangles,
                vertices=new_vertices.astype(np.float32).tobytes(),
                triangles=new_triangles.astype(np.int32).tobytes()))
            width = response.width
            height = response.height
            depth_image = np.reshape(np.frombuffer(response.depth_image, dtype=np.float32), (width, height))
            depth_images.append(depth_image)
        fps = n / (time.time() - start)
        print("%d fps" % (fps,))
        
    # now save some of them to disk
    for (i, img) in enumerate(depth_images[1:5]):
        print(i)
        plt.figure()
        plt.imshow(img)
        plt.savefig("output/depth-%03d.png" % (i,))
        plt.clf()

if __name__ == '__main__':
    logging.basicConfig()
    run()
