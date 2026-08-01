"""
Functions for validating bioimage metadata.
"""

import re

# Metadata fields that are essential for interpreting and reusing an
# image (e.g. required to correctly scale, register, or compare images).
# A missing critical field is reported as an error; anything else is
# reported as a warning.
CRITICAL_FIELDS = {
    "image.size_x",
    "image.size_y",
    "image.size_c",
    "image.size_z",
    "image.size_t",
    "pixel_size.pixel_size_x",
    "pixel_size.pixel_size_y",
}


def is_critical_field(field_path):
    """
    Determine whether a metadata field is critical for image
    interpretation/reuse, based on the CRITICAL_FIELDS registry.

    Array indices (e.g. "channels[0].name") are stripped before
    comparison so that fields inside lists are matched against their
    unindexed path (e.g. "channels.name").

    Parameters
    ----------
    field_path : str
        Dotted path to a metadata field, as produced by
        `find_missing_values`.

    Returns
    -------
    bool
        True if the field is critical, False otherwise.
    """

    normalized_path = re.sub(r"\[\d+\]", "", field_path)

    return normalized_path in CRITICAL_FIELDS


def find_missing_values(data, path=""):
    """
    Recursively find missing metadata values.

    Parameters
    ----------
    data : dict/list
        Metadata structure.

    path : str
        Current metadata location.

    Returns
    -------
    list
        Missing metadata fields.
    """

    missing = []

    if isinstance(data, dict):

        for key, value in data.items():

            current_path = f"{path}.{key}" if path else key

            if value is None:
                missing.append(current_path)

            else:
                missing.extend(
                    find_missing_values(value, current_path)
                )

    elif isinstance(data, list):

        for index, item in enumerate(data):

            current_path = f"{path}[{index}]"

            missing.extend(
                find_missing_values(item, current_path)
            )

    return missing


def validate_metadata(report):
    """
    Validate metadata completeness.

    Returns
    -------
    dict
        Errors and warnings.
    """

    missing_fields = find_missing_values(report)

    errors = []
    warnings = []

    for field in missing_fields:

        message = f"Missing metadata: {field}"

        if is_critical_field(field):
            errors.append(message)
        else:
            warnings.append(message)

    return {
        "errors": errors,
        "warnings": warnings
    }