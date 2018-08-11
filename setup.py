from setuptools import setup

setup(
    name='bc_bin_clip',
    version='0.0.1',
    description='Binning and trimming for barcoded high-throughput sequencing reads',
    url='http://github.com/svohr/bc_bin_clip',
    author='Samuel H. Vohr',
    author_email='svohr@soe.ucsc.edu',
    license='MIT',
    scripts=['bc_bin_clip'],
    install_requires=['biopython']
    )
