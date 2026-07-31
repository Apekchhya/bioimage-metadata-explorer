# BioImage Metadata Explorer

A Python-based tool for extracting, validating, and reporting metadata from OME-TIFF bioimaging datasets.

## Overview

Modern microscopy experiments generate increasingly complex image datasets. 
Accurate and complete metadata is essential for reproducible research, image interpretation, and long-term data sharing.

BioImage Metadata Explorer provides a lightweight workflow for assessing bioimage metadata quality by extracting OME-XML metadata, standardizing image information, and identifying missing or incomplete fields.

The project explores concepts relevant to bioimage data management, metadata curation, and scientific data repositories.

---

## Features

- Extract OME-XML metadata from OME-TIFF images
- Parse image dimensions, channels, and pixel information
- Validate metadata completeness
- Classify missing metadata as errors or warnings
- Generate human-readable CLI reports
- Export structured JSON metadata
- Automated testing using pytest

---

## Workflow


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


---

## Installation

Clone the repository:

```bash
git clone https://github.com/Apekchhya/bioimage-metadata-explorer.git

cd bioimage-metadata-explorer

Create a virtual environment:

python -m venv .venv

source .venv/bin/activate

Install dependencies:

pip install -e .
Usage

Run the metadata report tool:

bioimage-report data/sample_images/tubhiswt_C0.ome.tif

Example output:

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
Testing

Run:

pytest

Example:

7 passed
Technologies
Python
tifffile
ome-types
pytest
JSON metadata standards
OME-TIFF
Scientific Motivation

This project was developed to gain practical experience with bioimage data standards and metadata quality assessment workflows.

It focuses on challenges encountered in biological image repositories, including metadata extraction, validation, standardization, and reproducible data sharing.


---

```markdown
## Relevance to Bioimage Data Management

The project explores workflows related to:
- OME data standards
- metadata curation
- image dataset quality control
- structured biological data exchange
- reproducible research workflows


