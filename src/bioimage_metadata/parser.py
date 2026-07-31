"""
Functions for extracting OME metadata.
"""
from ome_types import from_xml
from pathlib import Path
import tifffile


def extract_ome_metadata(image_path):
    """
    Extract raw OME metadata from an OME-TIFF file.

    Parameters
    ----------
    image_path : str
        Path to OME-TIFF image.

    Returns
    -------
    str
        OME-XML metadata.
    """

    image_path = Path(image_path)

    with tifffile.TiffFile(image_path) as tif:
        ome_xml = tif.ome_metadata

    return ome_xml

def parse_ome_metadata(ome_xml):
    """
    Convert OME-XML into structured metadata.

    Parameters
    ----------
    ome_xml : str
        Raw OME XML.

    Returns
    -------
    object
        Parsed OME metadata object.
    """

    metadata = from_xml(ome_xml)

    return metadata


def get_image_metadata(ome):
    """
    Extract useful metadata fields from OME object.

    Parameters
    ----------
    ome : OME
        Parsed OME metadata object.

    Returns
    -------
    dict
        Simplified metadata dictionary.
    """

    image = ome.images[0]
    pixels = image.pixels

    metadata = {
        "image_id": image.id,
        "size_x": pixels.size_x,
        "size_y": pixels.size_y,
        "size_c": pixels.size_c,
        "size_z": pixels.size_z,
        "size_t": pixels.size_t,
    }

    return metadata

def get_channel_metadata(ome):
    """
    Extract channel information from OME metadata.
    """

    image = ome.images[0]
    channels = image.pixels.channels

    channel_info = []

    for channel in channels:
        info = {
            "id": channel.id,
            "name": channel.name,
        }

        channel_info.append(info)

    return channel_info

def get_pixel_size_metadata(ome):
    """
    Extract physical pixel size information.
    """

    image = ome.images[0]
    pixels = image.pixels

    pixel_metadata = {
        "pixel_size_x": pixels.physical_size_x,
        "pixel_size_y": pixels.physical_size_y,
        "pixel_size_x_unit": str(pixels.physical_size_x_unit),
        "pixel_size_y_unit": str(pixels.physical_size_y_unit),
    }

    return pixel_metadata

def analyze_image(ome):
    """
    Generate complete metadata summary.
    """

    report = {
        "image": get_image_metadata(ome),
        "channels": get_channel_metadata(ome),
        "pixel_size": get_pixel_size_metadata(ome),
    }

    return report