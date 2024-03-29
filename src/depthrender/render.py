import open3d as o3d
import numpy as np

# NOTE: use a version of Open3D built using these instructions:
# http://www.open3d.org/docs/latest/tutorial/Advanced/headless_rendering.html

def initialize_mesh():
    num_vertices = 3
    num_triangles = 1
    vertices = np.random.rand(num_vertices, 3)
    triangles = np.random.randint(0, num_vertices, (num_triangles, 3))
    mesh = o3d.geometry.TriangleMesh(
        o3d.utility.Vector3dVector(vertices),
        o3d.utility.Vector3iVector(triangles))
    return mesh

def make_new_open3d_vis(width, height, fx, fy, cx, cy):
    vis = o3d.visualization.Visualizer()
    vis.create_window(width=width, height=height, visible=False)
    mesh = initialize_mesh()
    # NOTE: we need to add the geometry to the vis before setting camera
    # since adding the geometry changes the camera params
    # (even with reset_bounding_box=False -- TODO file a bug report with open3d)
    vis.add_geometry(mesh)
    vis.get_render_option().mesh_show_back_face = True
    view = vis.get_view_control()
    camera = o3d.camera.PinholeCameraParameters()
    camera.extrinsic = np.eye(4)
    camera.intrinsic = o3d.camera.PinholeCameraIntrinsic(
        width, height, fx, fy, cx, cy)
    view.convert_from_pinhole_camera_parameters(camera, allow_arbitrary=True)
    view.set_constant_z_near(0.001)
    view.set_constant_z_far(5.0)
    return vis, mesh

class Renderer(object):

    def __init__(self):
        self.vis = None
        self.mesh = None

    def set_camera_params(self, width, height, fx, fy, cx, cy):
        if not self.vis is None:
            self.vis.destroy_window()
            # setting self.vis = None is actually required to avoid 'GLFW not initialized errors'
            # when using open3d built to use OSMesa. TODO: file a bug report with open3d
            self.vis = None 
            self.mesh = None
        new_vis, new_mesh = make_new_open3d_vis(width, height, fx, fy, cx, cy)
        self.vis = new_vis
        self.mesh = new_mesh
        
    def render(self, vertices, triangles):
        if self.vis is None:
            raise RuntimeError("camera parameters not yet set")
        if (not isinstance(vertices, np.ndarray) or
            vertices.ndim != 2 or
            vertices.shape[1] != 3):
            raise ValueError("vertices should be a n x 3 numpy array of floats")
        if (not isinstance(triangles, np.ndarray) or
            triangles.ndim != 2 or
            triangles.shape[1] != 3):
            raise ValueError("triangles should be a n x 3 numpy array of integers")
        self.mesh.vertices = o3d.utility.Vector3dVector(vertices)
        self.mesh.triangles = o3d.utility.Vector3iVector(triangles)
        self.vis.update_geometry(self.mesh)
        depth_image = self.vis.capture_depth_float_buffer(True) # float32
        depth_image = np.asarray(depth_image)
        assert depth_image.dtype == np.float32
        return depth_image

    def destroy(self):
        if self.vis is not None:
            self.vis.destroy_window()
            self.vis = None
            self.mesh = None
