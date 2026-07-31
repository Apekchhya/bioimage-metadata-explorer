"""
Command line interface for BioImage Metadata Explorer.
"""

import argparse

from bioimage_metadata.parser import (
    extract_ome_metadata,
    parse_ome_metadata,
    analyze_image
)

from bioimage_metadata.validator import validate_metadata


def main():

    parser = argparse.ArgumentParser(
        description="Generate bioimage metadata report"
    )

    parser.add_argument(
        "image",
        help="Path to OME-TIFF image"
    )

    args = parser.parse_args()

    xml = extract_ome_metadata(args.image)

    ome = parse_ome_metadata(xml)

    report = analyze_image(ome)

    warnings = validate_metadata(report)

    print("\nBioImage Metadata Report")
    print("========================")

    print(report)

    print("\nWarnings:")

    if warnings:
        for warning in warnings:
            print("-", warning)
    else:
        print("No warnings")


if __name__ == "__main__":
    main()