from setuptools import setup
import pathlib

from charset_mnbvc.version import __version__
here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")


setup(
    name="better_zipfile",
    version=__version__,
    description="本项目旨在对优化python中自带的zipfile，以处理mnbvc项目解压遇到的问题",
    url="https://github.com/aplmikex/better_zipfile",
    author="aplmikex",
    author_email="2738186032@qq.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3"
    ],
    packages=['better_zipfile'],
    python_requires=">=3.7",
    project_urls={  # Optional
        "Bug Reports": "https://github.com/aplmikex/better_zipfile/issues",
        "Source": "https://github.com/aplmikex/better_zipfile/",
    },
)