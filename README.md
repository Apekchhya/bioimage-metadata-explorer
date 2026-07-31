# BioImage Metadata Explorer

A Python-based tool for extracting, validating, and reporting metadata from OME-TIFF bioimaging datasets.

## Overview

Modern microscopy experiments generate large and complex image datasets. 
Reliable metadata is essential for image interpretation, reproducibility, and data sharing.

BioImage Metadata Explorer provides a lightweight workflow to:

- Extract OME-XML metadata from OME-TIFF images
- Parse image dimensions and channel information
- Validate metadata completeness
- Generate human-readable reports
- Export structured JSON metadata


## Features

✅ OME-TIFF metadata extraction  
✅ OME-XML parsing using OME standards  
✅ Image dimension analysis  
✅ Channel metadata inspection  
✅ Pixel calibration checking  
✅ Metadata quality validation  
✅ JSON report generation  
✅ Command-line interface  
✅ Automated testing with pytest  


## Workflow

OME-TIFF Image
|
↓
OME-XML Metadata Extraction
|
↓
Metadata Parser
|
↓
Structured Metadata Report
|
↓
Validation Engine
|
↓
CLI Report / JSON Output



## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/bioimage-metadata-explorer.git

cd bioimage-metadata-explorer

Create environment:

python -m venv .venv
source .venv/bin/activate

Install:
pip install -e .

Usage

Run:
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

Usage

Run:

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
Motivation

This project was developed to explore bioimage data management, metadata standards, and quality control workflows used in biological image repositories.