
# -*- coding: utf-8 -*-


from setuptools import setup, find_packages

setup(
    name="speechmetrics",
    version="1.0",
    packages=find_packages(),

    install_requires=[
        'numpy',
        'scipy',
        'tqdm',
        'resampy',
        'pystoi',
        'museval',
        'tensorflow>=2.0.0',
        'librosa',
        # This is requred, but srmrpy pull it in,
	    # and there is a pip3 conflict if we have the following
	    # line.
        #'gammatone',
        'pypesq' @ https://github.com/vBaiCai/python-pesq,
        'srmrpy',
        'pesq',
    ],
    include_package_data=True
)
