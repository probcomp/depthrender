# depthrender
Depth renderer with a simple numpy interface and associated [gRPC](https://grpc.io/) microservice.

## Installation

First, install a version of `open3d` built according to [these instructions](http://www.open3d.org/docs/latest/tutorial/Advanced/headless_rendering.html).
In particular, be sure to run `make install-pip-package` with your project's Python virtual environment activated. 

Then, with your environment still activated, run:
```
cd depthrender
pip install .
```

## Examples

There is an example script that runs the rendering in the same process:
```
python example.py
```

There is a second example script that requests the depth images from a depth image server.

First, start the server (it should be on your PATH if the Python virtual environment where `depthrender` was installed is activated):
```
depthserver
```
Then, in a separate terminal (with the Python virtual environment still activated), run:
```
python example_client.py
```
