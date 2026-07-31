from bioimage_metadata.parser import (
    extract_ome_metadata,
    parse_ome_metadata,
    analyze_image
)

from bioimage_metadata.validator import validate_metadata


image = "data/sample_images/tubhiswt_C0.ome.tif"


xml = extract_ome_metadata(image)

ome = parse_ome_metadata(xml)

report = analyze_image(ome)


warnings = validate_metadata(report)


print(warnings)