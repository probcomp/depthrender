from concurrent import futures
import logging

import time
import numpy as np
from depthrender.render import Renderer

import grpc
from depthrender import depthrender_pb2
from depthrender import depthrender_pb2_grpc

class Server(depthrender_pb2_grpc.DepthRenderServicer):

    def __init__(self, renderer):
        super().__init__()
        self.renderer = renderer

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

def serve():
    renderer = Renderer()
    render_server = Server(renderer)
    # NOTE: needs to be only 1 worker thread; otherwise regular Open3D build
    # (not OSMesa) crashes when there are multiple channels opened
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1)) 
    depthrender_pb2_grpc.add_DepthRenderServicer_to_server(render_server, server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
    renderer.destroy()
        

def main():
    logging.basicConfig()
    serve()
