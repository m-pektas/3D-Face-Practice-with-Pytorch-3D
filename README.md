# 3D-Face-Practice-with-Pytorch-3D
*This repository was created for peoples that want to do beginner practice with any 3D face model. The goal is decrease entry barrier to start 3D modelling with mechine learning.*


## Installation

1. Download **BFM_model_front.mat** file for Basel Face Model (BFM). 
You can download model from [here](https://drive.google.com/file/d/1cCTfTiKK98BRu6sVq09h94FzwoEncoVi/view?usp=sharing). This file created using *transferBFM09* function of [Deep3DFaceReconstruction](https://github.com/microsoft/Deep3DFaceReconstruction/blob/5b131a3e67597da67409486e20db50007f48427d/utils.py).

2. Create New Conda Environment

        conda create --name env python=3.7.4 -y
        conda activate env

3. Run Installation Scripts
    3.1 Other libraries

        pip install -r requirements.txt

    3.2 Pytorch 3D

        python install_pytorch3d.py

        if you see "Installation Success !!!", Installation OK.


Now, You can do practice. :)

---
## Contributing
Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are greatly appreciated.

1. Fork the Project
2. Create your Feature Branch ```git checkout -b feature/AmazingFeature```
3. Commit your Changes ```git commit -m 'Add some AmazingFeature'```
4. Push to the Branch ```git push origin feature/AmazingFeature```
5. Open a Pull Request