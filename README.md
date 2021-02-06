# depthrendersvc
Code for a simple depth rendering microservice

## Requirements

Server requires `grpc` and `numpy` and `open3d`. For fast headless rendering with Open3D, install a version of `open3d` built according to [these instructions](http://www.open3d.org/docs/latest/tutorial/Advanced/headless_rendering.html).

The client script uses `grpc` and `numpy`. (It also uses `matplotlib` to save the depth images to disk afterwards.)

## To run it

In one terminal, start the server:
```
python depthrender_server.py
```

In another terminal, run the client:
```
python depthrender_client.py
```

## TODO

- Package as a Python package

- Make setting camera intrinsics part of the interface
