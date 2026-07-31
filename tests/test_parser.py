from bioimage_metadata.parser import (
    extract_ome_metadata,
    parse_ome_metadata,
    get_image_metadata,
    get_channel_metadata,
    get_pixel_size_metadata,
    analyze_image
)


image = "data/sample_images/tubhiswt_C0.ome.tif"


xml = extract_ome_metadata(image)

ome = parse_ome_metadata(xml)

report = analyze_image(ome)

print(report)