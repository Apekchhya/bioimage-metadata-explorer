# BioImage Metadata Explorer

A Python-based tool for extracting, validating, reporting, and converting metadata and image data for OME-TIFF bioimaging datasets.

## Overview

Modern microscopy experiments generate increasingly complex image datasets. Accurate and complete metadata is essential for reproducible research, image interpretation, and long-term data sharing.

BioImage Metadata Explorer provides a lightweight workflow for assessing bioimage metadata quality by extracting OME-XML metadata, standardizing image information, identifying missing or incomplete fields, and converting images to OME-Zarr — the cloud-native, chunked format increasingly used by bioimage repositories such as the BioImage Archive.

The project explores concepts relevant to bioimage data management, metadata curation, and scientific data repositories.

---

## Features

- Extract OME-XML metadata from OME-TIFF images
- Parse image dimensions, channels, and pixel information
- Validate metadata completeness against an explicit critical-field schema
- Classify missing metadata as errors or warnings
- Convert OME-TIFF images to OME-Zarr (OME-NGFF) format
- Generate human-readable CLI reports
- Export structured JSON metadata
- Automated testing using pytest

---

## Workflow

```text
OME-TIFF Image
        |
        ↓
OME-XML Metadata Extraction
        |
        ↓
OME Metadata Parser
        |
        ↓
Structured Metadata Object
        |
        ↓
Metadata Validation Engine
        |
        ↓
CLI Report / JSON Output
        |
        ↓ (optional, --to-zarr)
OME-Zarr Conversion
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Apekchhya/bioimage-metadata-explorer.git

cd bioimage-metadata-explorer
```

Create a virtual environment:

```bash
python -m venv .venv

source .venv/bin/activate
```

Install dependencies:

```bash
pip install -e .
```

---

## Usage

### Generate a metadata report

```bash
bioimage-report data/sample_images/tubhiswt_C0.ome.tif
```

Example output:

```text
BioImage Metadata Report
========================

Image Information
-----------------
Image ID: Image:0
Dimensions: 512 × 512
Channels: 2
Z slices: 1
Time points: 1

Validation
----------

Errors:
- Missing metadata: pixel_size.pixel_size_x

Warnings:
- Missing metadata: channels[0].name
```

### Save the report as JSON

```bash
bioimage-report data/sample_images/tubhiswt_C0.ome.tif --output-file reports/tubhiswt_report.json
```

### Convert to OME-Zarr

Add `--to-zarr` to also convert the image to OME-Zarr alongside the metadata report:

```bash
bioimage-report data/sample_images/tubhiswt_C0.ome.tif --to-zarr output.zarr
```

Use `--overwrite-zarr` to replace an existing store at that path. Both flags can be combined with `--output-file` to get a metadata report and a converted image in one pass:

```bash
bioimage-report data/sample_images/tubhiswt_C0.ome.tif \
  --output-file reports/tubhiswt_report.json \
  --to-zarr output.zarr
```

### Sample data

The bundled sample images (`tubhiswt_C0.ome.tif`, `tubhiswt_C1.ome.tif`) are from the official [OME-TIFF sample data set](https://ome-model.readthedocs.io/en/stable/ome-tiff/data.html) distributed by the Open Microscopy Environment: tubulin/histone-GFP coexpressing *C. elegans* embryos, imaged on a multiphoton workstation at 512×512 resolution in 8-bit grayscale. Their metadata is intentionally incomplete for some fields (missing pixel size and channel names), which makes them useful for demonstrating the validation engine.

---

## Testing

Run:

```bash
pytest
```

Example:

```text
14 passed
```

---

## Technologies

- Python
- tifffile
- ome-types
- ome-zarr / zarr
- pytest
- JSON metadata standards
- OME-TIFF / OME-Zarr (OME-NGFF)

---

## Scientific Motivation

This project was developed to gain practical experience with bioimage data standards and metadata quality assessment workflows.

It focuses on challenges encountered in biological image repositories, including metadata extraction, validation, standardization, and reproducible data sharing.

---

## Relevance to Bioimage Data Management

The project explores workflows related to:

- OME data standards
- Metadata curation
- Image dataset quality control
- OME-Zarr conversion and cloud-native image formats
- Structured biological data exchange
- Reproducible research workflows