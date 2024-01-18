from setuptools import setup, find_packages

setup(
    name="sysinf",
    version="1.0.0",
    author="oivalian",
    packages=find_packages(),
    install_requires=[
        "psutil",
        "platform",
        "py-cpuinfo",
        "GPUtil",
        "os",
    ],
)
