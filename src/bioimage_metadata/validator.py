"""
Functions for validating bioimage metadata.
"""


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

        # Critical metadata
        if "pixel_size" in field:
            errors.append(message)

        # Less critical metadata
        elif "channels" in field:
            warnings.append(message)

        else:
            warnings.append(message)

    return {
        "errors": errors,
        "warnings": warnings
    }