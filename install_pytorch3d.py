import os
import sys
import torch
if torch.__version__=='1.6.0+cu101' and sys.platform.startswith('linux'):
    os.system("pip install pytorch3d")
else:
    need_pytorch3d=False
    try:
        import pytorch3d
    except ModuleNotFoundError:
        need_pytorch3d=True
    if need_pytorch3d:
        try:
            os.system("curl -LO https://github.com/NVIDIA/cub/archive/1.10.0.tar.gz")
            os.system("tar xzf 1.10.0.tar.gz")
            os.environ["CUB_HOME"] = os.getcwd() + "/cub-1.10.0"
            print("intalling pytorch 3d")
            os.system("pip install 'git+https://github.com/facebookresearch/pytorch3d.git@stable'")
            print("Installation Success !!!")
        except:
            print("Installation Failed !!! Please find another way :(")