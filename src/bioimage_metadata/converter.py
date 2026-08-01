"""
Functions for converting OME-TIFF images to OME-Zarr.

OME-Zarr (OME-NGFF) is the cloud-native, chunked storage format used by
modern bioimage repositories (e.g. the BioImage Archive, IDR) in place
of monolithic TIFF files. This module wraps `ome-zarr-py` to provide a
single entry point that converts an already-read image array into an
OME-Zarr store, using the axis order reported by `tifffile`.
"""

from pathlib import Path
import shutil

import tifffile
import zarr
from ome_zarr.io import parse_url
from ome_zarr.writer import write_image

# Map tifffile/OME axis codes to the axis names ome-zarr-py expects.
AXIS_NAME_MAP = {
    "T": "time",
    "C": "channel",
    "Z": "z",
    "Y": "y",
    "X": "x",
}


def convert_to_zarr(image_path, output_path, overwrite=False):
    """
    Convert an OME-TIFF image to OME-Zarr format.

    Parameters
    ----------
    image_path : str
        Path to the source OME-TIFF image.
    output_path : str
        Path to the output .zarr store to create.
    overwrite : bool
        If True, delete an existing store at output_path before writing.

    Returns
    -------
    dict
        Summary of the conversion: output path, axes, shape, and
        the number of resolution levels written.

    Raises
    ------
    FileExistsError
        If output_path already exists and overwrite is False.
    """

    image_path = Path(image_path)
    output_path = Path(output_path)

    if output_path.exists():
        if overwrite:
            shutil.rmtree(output_path)
        else:
            raise FileExistsError(
                f"{output_path} already exists. "
                "Pass overwrite=True to replace it."
            )

    with tifffile.TiffFile(image_path) as tif:
        series = tif.series[0]
        array = series.asarray()
        source_axes = series.axes

    try:
        axes = [AXIS_NAME_MAP[axis] for axis in source_axes]
    except KeyError as exc:
        raise ValueError(
            f"Unsupported axis code {exc} in {source_axes!r}; "
            f"supported axes are {sorted(AXIS_NAME_MAP)}"
        ) from exc

    store = parse_url(str(output_path), mode="w").store
    root = zarr.group(store=store)

    write_image(image=array, group=root, axes=axes, scaler=None)

    resolution_levels = [
        key for key in root.array_keys()
    ]

    return {
        "output_path": str(output_path),
        "source_axes": source_axes,
        "zarr_axes": axes,
        "shape": list(array.shape),
        "resolution_levels": len(resolution_levels),
    }