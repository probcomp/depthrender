from concurrent import futures
import logging

import open3d as o3d
import time
import numpy as np

import grpc
import depthrender_pb2
import depthrender_pb2_grpc

# NOTE: use a version of Open3D built using these instructions:
# http://www.open3d.org/docs/latest/tutorial/Advanced/headless_rendering.html

def create_open3d_vis(width, height, fx, fy, cx, cy):
    vis = o3d.visualization.Visualizer()
    vis.create_window(width=width, height=height)
    view = vis.get_view_control()
    camera = o3d.camera.PinholeCameraParameters()
    camera.extrinsic = np.eye(4)
    camera.intrinsic = o3d.camera.PinholeCameraIntrinsic(
        width, height, fx, fy, cx, cy)
    view.convert_from_pinhole_camera_parameters(camera)
    view.set_constant_z_near(0.001)
    view.set_constant_z_far(5.0)
    mesh = o3d.geometry.TriangleMesh(
        o3d.utility.Vector3dVector(np.zeros((0, 3), dtype=np.float64)),
        o3d.utility.Vector3iVector(np.zeros((0, 3), dtype=np.int32)))
    vis.add_geometry(mesh)
    return vis, mesh

class DepthRenderer(depthrender_pb2_grpc.DepthRenderServicer):

    def __init__(self, width, height, fx, fy, cx, cy):
        self.vis, self.mesh = create_open3d_vis(width, height, fx, fy, cx, cy)
        self.width = width
        self.height = height

    def RenderDepthImage(self, request, context):
        num_vertices = request.num_vertices
        num_triangles = request.num_triangles
        vertices = np.reshape(np.frombuffer(request.vertices, dtype=np.float32), (num_vertices, 3))
        indices = np.reshape(np.frombuffer(request.triangles, dtype=np.int32), (num_triangles, 3))
        self.mesh.vertices = o3d.utility.Vector3dVector(vertices.copy())
        self.mesh.triangles = o3d.utility.Vector3iVector(indices.copy())
        self.vis.update_geometry(self.mesh)
        depth_image = self.vis.capture_depth_float_buffer(True) # float32
        depth_image = np.asarray(depth_image)
        return depthrender_pb2.RenderDepthImageReply(
            width=self.width,
            height=self.height,
            depth_image=depth_image.tobytes())

def serve():
    width = 64
    height = 64
    fx = width/3.0
    fy = width/3.0
    cx = width/2.0 - 0.5
    cy = height/2.0 - 0.5
    renderer = DepthRenderer(width, height, fx, fy, cx, cy)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    depthrender_pb2_grpc.add_DepthRenderServicer_to_server(renderer, server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
    vis.destroy_window()

if __name__ == '__main__':
    logging.basicConfig()
    serve()
