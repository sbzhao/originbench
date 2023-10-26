# This code is part of OriginQ QPanda Experiment.
#
# (C) Copyright OriginQ 2023.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"The OriginQ QPanda Experiment setup file."

import os
from setuptools import setup, find_packages
from .version import __version__

with open("requirements.txt", encoding="utf-8") as f:
    REQUIREMENTS = f.read().splitlines()

# Read long description from README.
README_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), "README.md")
with open(README_PATH, encoding="utf-8") as readme_file:
    README = readme_file.read()

setup(
    name="OriginQ Benchmark Suite",
    version=__version__,
    description="Python library for running quantum benchmarking experiments for OringQ quantum chip.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="http://10.10.10.82:7990/scm/experiment/qpanda-experiment.git",
    author="Zhao Shubin",
    author_email="zsb3@originqc.com",
    license="Apache 2.0",
    classifiers=[
        "Environment :: Console",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering",
    ],
    keywords="OriginQ Benchmark Experiment",
    packages=find_packages(),
    install_requires=REQUIREMENTS,
    python_requires=">=3.7",
)
