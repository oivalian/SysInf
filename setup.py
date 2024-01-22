from setuptools import setup, find_packages

VERSION = "1.0.0"
DESCRIPTION = "A small package that simplfies system information into pre-defined strings."

setup(
    name="sysinfo",
    version=VERSION,
    description=DESCRIPTION,
    author="oivalian",
    packages=find_packages(),
    install_requires=[
        "psutil",
        "py-cpuinfo",
        "GPUtil",
    ],
)
