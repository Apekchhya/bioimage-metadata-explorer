from bioimage_metadata.pipeline import generate_report


report = generate_report(
    "data/sample_images/tubhiswt_C0.ome.tif",
    "reports/final_report.json"
)


print(report)