"""
Functions for exporting metadata reports.
"""

import json


def save_json(report, output_file):
    """
    Save metadata report as JSON.
    """

    with open(output_file, "w") as f:
        json.dump(
            report,
            f,
            indent=4,
            default=str
        )