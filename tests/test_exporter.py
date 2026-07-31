from bioimage_metadata.parser import (
    extract_ome_metadata,
    parse_ome_metadata,
    analyze_image
)

from bioimage_metadata.exporter import save_json


image = "data/sample_images/tubhiswt_C0.ome.tif"


xml = extract_ome_metadata(image)

ome = parse_ome_metadata(xml)

report = analyze_image(ome)


save_json(
    report,
    "reports/tubhiswt_metadata.json"
)