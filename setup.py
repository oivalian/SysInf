from setuptools import setup, find_packages

setup(
    name="sysinf",
    version="1.0.0",
    author="oivalian",
    packages=find_packages(),
    install_requires=[
        "psutil>=5.9.7",  # Specify a minimum version if needed
        "py-cpuinfo>=9.0.0",  # Specify a minimum version if needed
        "GPUtil>=1.4.0",  # Specify a minimum version if needed
    ],
)
