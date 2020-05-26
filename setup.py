from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="Data Generator",
    version="0.5.0",
    packages=find_packages(),
    install_requires=["tqdm", "XlsxWriter", "tomlkit"],
    author="bednaJedna",
    author_email="bednarik.radek@gmail.com",
    description="Random Data Generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="random data generator python3",
    url="https://github.com/bednaJedna/data_generator",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
