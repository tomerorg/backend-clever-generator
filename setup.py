
from setuptools import setup, find_packages

setup(
    name="backend-clever-generator",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.1",
        "pandas>=1.2.0",
        "numpy>=1.20.0",
    ],
    author="",
    author_email="",
    description="Backend service implementing Pandas architecture",
    keywords="backend-clever-generator, python",
    url="",
)
