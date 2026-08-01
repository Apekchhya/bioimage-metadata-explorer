import shutil
from pathlib import Path

import pytest

from bioimage_metadata.converter import convert_to_zarr


IMAGE = "data/sample_images/tubhiswt_C0.ome.tif"


@pytest.fixture
def output_zarr(tmp_path):
    out = tmp_path / "output.zarr"
    yield out
    if out.exists():
        shutil.rmtree(out)


def test_convert_to_zarr_creates_store(output_zarr):
    result = convert_to_zarr(IMAGE, output_zarr)

    assert output_zarr.exists()
    assert (output_zarr / "zarr.json").exists()


def test_convert_to_zarr_reports_correct_shape(output_zarr):
    result = convert_to_zarr(IMAGE, output_zarr)

    assert result["shape"] == [2, 512, 512]
    assert result["source_axes"] == "CYX"
    assert result["zarr_axes"] == ["channel", "y", "x"]


def test_convert_to_zarr_refuses_overwrite_by_default(output_zarr):
    convert_to_zarr(IMAGE, output_zarr)

    with pytest.raises(FileExistsError):
        convert_to_zarr(IMAGE, output_zarr)


def test_convert_to_zarr_overwrite_true_replaces_store(output_zarr):
    convert_to_zarr(IMAGE, output_zarr)

    # Should not raise when overwrite=True
    result = convert_to_zarr(IMAGE, output_zarr, overwrite=True)

    assert result["shape"] == [2, 512, 512]