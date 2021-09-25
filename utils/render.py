from pytorch3d.structures import Meshes
from pytorch3d.renderer import (
    look_at_view_transform,
    FoVPerspectiveCameras, 
    PointLights, 
    DirectionalLights, 
    Materials, 
    RasterizationSettings, 
    MeshRenderer, 
    MeshRasterizer,  
    SoftPhongShader,
    TexturesUV,
    TexturesVertex,
    PointsRenderer
)
import scipy.io as sio
import numpy as np
import torch
import matplotlib.pyplot as pt
from argparse import Namespace

def render(mesh, angle_x=0, angle_y=0, size=256, device="cuda"):
    """
    This method render a mesh. 
    angle_x and angle_y determines camera coordinates.
    size determines rendered image size.
    """
    #camera and camera parameters
    R, T = look_at_view_transform(100, angle_y, angle_x) 
    cameras = FoVPerspectiveCameras(device=device, fov=1.5, R=R, T=T)

    #rasterization settings
    raster_settings = RasterizationSettings(
        image_size=size, 
        blur_radius=0.0, 
        faces_per_pixel=1, 
    )

    #light source
    lights = PointLights(device=device, ambient_color=((1, 1, 1),), location=[[0.0, 1.0, 0.0]])
    
    #renderer with selected settings
    renderer = MeshRenderer(
        rasterizer=MeshRasterizer(
            cameras=cameras, 
            raster_settings=raster_settings
        ),
        shader=SoftPhongShader(
            device=device, 
            cameras=cameras,
            lights=lights
        )
    )

    #rendering
    images = renderer(mesh)
    return images


def projectWorldToView(s, img_size, angle_x=0, angle_y=0, device="cuda"):
    """
    s : shape 
    """
    R, T = look_at_view_transform(100, angle_y, angle_x) 
    cameras = FoVPerspectiveCameras(device=device, fov=1.5, R=R, T=T)

    return cameras.transform_points_screen(s, img_size)
