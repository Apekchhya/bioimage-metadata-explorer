"""
High-level bioimage metadata pipeline.
"""

from bioimage_metadata.parser import (
    extract_ome_metadata,
    parse_ome_metadata,
    analyze_image
)

from bioimage_metadata.validator import validate_metadata
from bioimage_metadata.exporter import save_json
from bioimage_metadata.converter import convert_to_zarr


def generate_report(image_path, output_file=None, zarr_output=None, overwrite_zarr=False):
    """
    Generate metadata report from OME-TIFF image.

    Parameters
    ----------
    image_path : str
        Path to the source OME-TIFF image.
    output_file : str, optional
        If given, save the metadata report as JSON to this path.
    zarr_output : str, optional
        If given, also convert the image to OME-Zarr at this path and
        attach a conversion summary to the report under "zarr".
    overwrite_zarr : bool
        If True, overwrite an existing OME-Zarr store at zarr_output.
    """

    xml = extract_ome_metadata(image_path)

    ome = parse_ome_metadata(xml)

    report = analyze_image(ome)

    validation = validate_metadata(report)

    report["validation"] = validation

    if zarr_output:
        report["zarr"] = convert_to_zarr(
            image_path, zarr_output, overwrite=overwrite_zarr
        )

    if output_file:
        save_json(report, output_file)

    return report