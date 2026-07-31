from bioimage_metadata.validator import validate_metadata


def test_missing_metadata_detection():

    report = {
        "image": {
            "size_x": 512,
            "size_y": 512
        },
        "channels": [
            {
                "name": None
            }
        ],
        "pixel_size": {
            "pixel_size_x": None
        }
    }


    result = validate_metadata(report)


    assert len(result["errors"]) > 0
    assert len(result["warnings"]) > 0