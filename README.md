# Simple script to download DIV2K dataset

This lame script downloads DIVerse 2k (div2k) resolution hight quality images dataset as used for the challenges NTIRE (CVPR 2017 and CVPR 2018) and PIRM (ECCV 2018). More details at [https://data.vision.ee.ethz.ch/cvl/DIV2K/](https://data.vision.ee.ethz.ch/cvl/DIV2K/).

I said lame because currently it doesn't log download progress nor download each dataset's part in a different thread.

## How to use

```python main.py <output_folder_addr>```

Make sure you installed requirements first (use requirements.txt).

