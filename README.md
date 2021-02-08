# depthrender
Depth renderer with a simple numpy interface and associated [gRPC](https://grpc.io/) microservice.

## Installation

With your Python environment active, run:
```
git clone git@github.com:probcomp/depthrender.git
cd depthrender
pip install .
```

When using the verison of `open3d` that `pip` will obtian, the frame rate for depth rendering will be limited to 60 frames per second (FPS).
You can obtain much higher frame rates if you build Open3D according to  [these instructions](http://www.open3d.org/docs/latest/tutorial/Advanced/headless_rendering.html).
In particular, build Open3D according to intsructions above and run `make install-pip-package` with your project's Python environment activated. 
This causes headless rendering (which is not bound by the 60 FPS limit) to be used.
This build been succesfully tested on Ubuntu 18.04.

## Examples

There is an example script that runs the rendering in the same process:
```
python example.py
```
(NOTE: this script writes a bunch of `.png` files to the current working directory)

There is a second example script that requests the depth images from a depth image server.

First, start the server (it should be on your PATH if the Python environment where `depthrender` was installed is activated):
```
depthserver
```
Then, in a separate terminal (with the Python environment activated), run:
```
python example_client.py
```
