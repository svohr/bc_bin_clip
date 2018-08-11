# bc_bin_clip
Binning and trimming for barcoded high-throughput sequencing reads

## Requirements and Installation

`bc_bin_clip` is written in Python 2.7 and requires [Biopython](http://biopython.org/).
To install `bc_bin_clip` and Biopython with pip, use the following commands.

```
git clone https://github.com/svohr/bc_bin_clip.git
cd bc_bin_clip
pip install .
```

This will install `bc_bin_clip` into your path and allows it to be run directly
from the command line.

## Usage
```
usage: bc_bin_clip [OPTIONS] <R1_BC> <R2_BC> <R1.fastq> <R2.fastq>
       [-h] [-p OUT_PREFIX] [-n] [-m N]
       R1_BC_SEQ R2_BC_SEQ R1_FQ_FILE R2_FQ_FILE

positional arguments:
  R1_BC_SEQ             Barcode to find and trim from R1 file
  R2_BC_SEQ             Barcode to find and trim from R2 file
  R1_FQ_FILE            fastq file containing forward reads
  R2_FQ_FILE            fastq file containing reverse reads

optional arguments:
  -h, --help            show this help message and exit
  -p OUT_PREFIX, --prefix OUT_PREFIX
                        Prefix for output files.
  -n, --no-trim         Do not trim found barcodes.
  -m N, --mismatches N  Number of mismatches to allow in barcode sequence
                        (default=0)
```
