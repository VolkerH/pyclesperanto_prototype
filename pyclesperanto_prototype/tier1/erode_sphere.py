

from ..tier0 import execute


def erode_sphere (src, dst):
    """Computes a binary image with pixel values 0 and 1 containing the binary erosion of a given input image. 
    
    The erosion takes the von-Neumann-neighborhood (4 pixels in 2D and 6 pixels in 3d) into account.
    The pixels in the input image with pixel value not equal to 0 will be interpreted as 1.

    Available for: 2D, 3D

    Parameters
    ----------
    (Image source, ByRef Image destination)
    todo: Better documentation will follow
          In the meantime, read more: https://clij.github.io/clij2-docs/reference_erodeSphere


    Returns
    -------

    """


    parameters = {
        "src":src,
        "dst":dst
    }

    execute(__file__, 'erode_sphere_' + str(len(dst.shape)) + 'd_x.cl', 'erode_sphere_' + str(len(dst.shape)) + 'd', dst.shape, parameters)
