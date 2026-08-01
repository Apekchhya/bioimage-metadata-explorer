"""
Command line interface for BioImage Metadata Explorer.
"""

import argparse

from bioimage_metadata.pipeline import generate_report

def main():

    parser = argparse.ArgumentParser(
        description="Generate bioimage metadata report"
    )

    parser.add_argument(
        "image",
        help="Path to OME-TIFF image"
    )

    parser.add_argument(
        "--output-file",
        metavar="PATH",
        help="Save the metadata report as JSON to PATH"
    )

    parser.add_argument(
        "--to-zarr",
        metavar="OUTPUT_PATH",
        help="Also convert the image to OME-Zarr at OUTPUT_PATH"
    )

    parser.add_argument(
        "--overwrite-zarr",
        action="store_true",
        help="Overwrite an existing OME-Zarr store at --to-zarr's path"
    )

    args = parser.parse_args()

    report = generate_report(
        args.image,
        output_file=args.output_file,
        zarr_output=args.to_zarr,
        overwrite_zarr=args.overwrite_zarr,
    )

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

    if "zarr" in report:
        print("\nOME-Zarr Conversion")
        print("-------------------")

        zarr_info = report["zarr"]

        print(f"Output: {zarr_info['output_path']}")
        print(f"Source axes: {zarr_info['source_axes']}")
        print(f"Shape: {zarr_info['shape']}")


if __name__ == "__main__":
    main()