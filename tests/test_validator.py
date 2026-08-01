from bioimage_metadata.validator import validate_metadata, is_critical_field


def test_is_critical_field_true_for_pixel_size():
    assert is_critical_field("pixel_size.pixel_size_x") is True


def test_is_critical_field_false_for_channel_name():
    assert is_critical_field("channels[0].name") is False


def test_is_critical_field_handles_list_indices():
    # A critical field nested in a list should still match once the
    # index is stripped, since the registry stores unindexed paths.
    assert is_critical_field("image[0].size_x") is True
    assert is_critical_field("pixel_size[0].pixel_size_y") is True


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