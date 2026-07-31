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


def generate_report(image_path, output_file=None):
    """
    Generate metadata report from OME-TIFF image.
    """

    xml = extract_ome_metadata(image_path)

    ome = parse_ome_metadata(xml)

    report = analyze_image(ome)

    validation = validate_metadata(report)

    report["validation"] = validation

    if output_file:
        save_json(report, output_file)

    return report