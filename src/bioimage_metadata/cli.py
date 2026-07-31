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

    print("\nImage Information")
    print("-----------------")

    image = report["image"]

    print(f"Image ID: {image['image_id']}")
    print(f"Dimensions: {image['size_x']} × {image['size_y']}")
    print(f"Channels: {image['size_c']}")
    print(f"Z slices: {image['size_z']}")
    print(f"Time points: {image['size_t']}")


    print("\nChannel Information")
    print("-------------------")

    for channel in report["channels"]:
        print(
            f"{channel['id']} | "
            f"Name: {channel['name']}"
        )


    print("\nPixel Information")
    print("-----------------")

    pixel = report["pixel_size"]

    print(
        f"Pixel size X: {pixel['pixel_size_x']} "
        f"{pixel['pixel_size_x_unit']}"
    )

    print(
        f"Pixel size Y: {pixel['pixel_size_y']} "
        f"{pixel['pixel_size_y_unit']}"
    )

    print("\nWarnings:")

    if warnings:
        for warning in warnings:
            print("-", warning)
    else:
        print("No warnings")


if __name__ == "__main__":
    main()