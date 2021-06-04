import setuptools
from pathlib import Path
setuptools.setup(
    name="pytse",
    author="Milad Jahromi",
    version="1.6.1",
    long_description=Path("README.md").read_text(),
    long_description_content_type='text/markdown',
    description="A small web crawler for tsetmc.com",
    packages=setuptools.find_packages(exclude=["tests", "data"]),
    project_urls={
        'Source': 'https://github.com/miladj/PyTse',
    },
    install_requires=[
        'requests',
    ]
)
