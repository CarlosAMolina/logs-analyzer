import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    author="Carlos A Molina",
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System : Gnu/Linux: Debian",
    ],
    description="Python's logs parser",
    include_package_data=True,
    long_description_content_type="text/markdown",
    long_description=long_description,
    name="logs_parser",
    packages=setuptools.find_packages(),
    python_requires=">=3.9",
    version="0.0.1",
)
