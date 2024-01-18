from setuptools import setup, find_packages

setup(
    name="sysinf",
    version="1.0.0",
    author="oivalian",
    packages=find_packages(),
    install_requires=[
        "psutil>=5.9.7",
        "py-cpuinfo>=9.0.0",
        "GPUtil>=1.4.0",
    ],
)
