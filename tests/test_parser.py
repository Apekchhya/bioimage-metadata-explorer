from bioimage_metadata.parser import (
    extract_ome_metadata,
    parse_ome_metadata,
    get_image_metadata
)


IMAGE = "data/sample_images/tubhiswt_C0.ome.tif"


def test_extract_ome_metadata():

    xml = extract_ome_metadata(IMAGE)

    assert xml is not None
    assert "<OME" in xml


def test_parse_ome_metadata():

    xml = extract_ome_metadata(IMAGE)

    ome = parse_ome_metadata(xml)

    assert ome is not None


def test_image_metadata():

    xml = extract_ome_metadata(IMAGE)

    ome = parse_ome_metadata(xml)

    metadata = get_image_metadata(ome)

    assert metadata["size_x"] == 512
    assert metadata["size_y"] == 512
    assert metadata["size_c"] == 2