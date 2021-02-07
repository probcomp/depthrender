from concurrent import futures
import logging

import time
import numpy as np
from depthrender.render import Renderer

import grpc
from depthrender import depthrender_pb2
from depthrender import depthrender_pb2_grpc

class Server(depthrender_pb2_grpc.DepthRenderServicer):

    def __init__(self):
        super().__init__()
        self.renderer = Renderer()

    def SetCameraParams(self, request, context):
        width = request.width
        height = request.height
        fx = request.fx
        fy = request.fy
        cx = request.cx
        cy = request.cy
        self.renderer.set_camera_params(width, height, fx, fy, cx, cy)
        return depthrender_pb2.SetCameraParamsReply()

    def RenderDepthImage(self, request, context):
        num_vertices = request.num_vertices
        num_triangles = request.num_triangles
        vertices = np.reshape(
            np.frombuffer(request.vertices, dtype=np.float64),
            (num_vertices, 3)).copy()
        triangles = np.reshape(
            np.frombuffer(request.triangles, dtype=np.int64),
            (num_triangles, 3)).copy()
        depth_image = self.renderer.render(vertices, triangles)
        return depthrender_pb2.RenderDepthImageReply(
            depth_image=depth_image.tobytes())

    def destroy_renderer(self):
        self.renderer.destroy()

def serve():
    render_server = Server()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    depthrender_pb2_grpc.add_DepthRenderServicer_to_server(render_server, server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
    render.server.destroy_renderer()
        

def main():
    logging.basicConfig()
    serve()
