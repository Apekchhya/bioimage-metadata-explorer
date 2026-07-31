from bioimage_metadata.pipeline import generate_report


IMAGE = "data/sample_images/tubhiswt_C0.ome.tif"


def test_generate_report():

    report = generate_report(IMAGE)

    assert "image" in report
    assert "channels" in report
    assert "pixel_size" in report
    assert "validation" in report


def test_report_contains_dimensions():

    report = generate_report(IMAGE)

    assert report["image"]["size_x"] == 512
    assert report["image"]["size_y"] == 512
    assert report["image"]["size_c"] == 2