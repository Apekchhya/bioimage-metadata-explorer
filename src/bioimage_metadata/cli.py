"""
Command line interface for BioImage Metadata Explorer.
"""

import argparse

from black import validate_metadata

from bioimage_metadata.pipeline import generate_report

def main():

    parser = argparse.ArgumentParser(
        description="Generate bioimage metadata report"
    )

    parser.add_argument(
        "image",
        help="Path to OME-TIFF image"
    )

    args = parser.parse_args()

    report = generate_report(args.image)

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
    print("\nValidation")
    print("----------")

    validation = report["validation"]

    if validation["errors"]:
        print("\nErrors:")

        for error in validation["errors"]:
            print("-", error)


    if validation["warnings"]:
        print("\nWarnings:")

        for warning in validation["warnings"]:
            print("-", warning)


    if not validation["errors"] and not validation["warnings"]:
        print("No issues found")


if __name__ == "__main__":
    main()