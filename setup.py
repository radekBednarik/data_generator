from setuptools import setup, find_packages

setup(
    name="Data Generator",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["tqdm"],
    author="bednaJedna",
    author_email="bednarik.radek@gmail.com.com",
    description="Random Data Generator",
    keywords="random data generator python3",
    url="https://github.com/bednaJedna/data_generator",
    classifiers=[
        "License :: OSI Approved :: MIT",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8"
    # could also include long_description, download_url, etc.
)
