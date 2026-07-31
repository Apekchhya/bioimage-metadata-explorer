"""
Functions for reading biological image files.
"""

from pathlib import Path
import tifffile


def read_image_info(image_path):
    """
    Read basic information from an OME-TIFF image.

    Parameters
    ----------
    image_path : str
        Path to image file.

    Returns
    -------
    dict
        Basic image information.
    """

    image_path = Path(image_path)

    with tifffile.TiffFile(image_path) as tif:

        series = tif.series[0]

        info = {
    "filename": image_path.name,
    "axes": series.axes,
    "shape": series.shape,
    "dimensions": {
        axis: size
        for axis, size in zip(series.axes, series.shape)
    }
}

    return info