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
    """

    missing_fields = find_missing_values(report)

    warnings = []

    for field in missing_fields:
        warnings.append(
            f"Missing metadata: {field}"
        )

    return warnings