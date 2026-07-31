from pathlib import Path

from bioimage_metadata.pipeline import generate_report


IMAGE = "data/sample_images/tubhiswt_C0.ome.tif"


def test_json_report_creation(tmp_path):

    output = tmp_path / "report.json"

    generate_report(
        IMAGE,
        output
    )

    assert output.exists()