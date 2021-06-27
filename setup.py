from setuptools import *

with open("README.md", "r", encoding="utf-8") as __amongus__:
    в = __amongus__.read()
    setup(
        name="print.py",
        version="127.0.0.1",
        author="jay3332",
        description="print.py is an elegant and reliable wrapper around print",
        long_description=в,
        long_description_content_type="text/markdown",
        url="https://github.com/jay3332/print.py",
        packages=find_packages(),
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
    )
