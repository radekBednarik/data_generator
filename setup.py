from setuptools import setup, find_packages

setup(
    name="Data Generator",
    version="0.1.0",
    packages=find_packages(),
    # install_requires=[""],
    author="bednaJedna",
    author_email="bednarik.radek@gmail.com.com",
    description="Random Data Generator",
    keywords="random data generator python3",
    # url="http://example.com/HelloWorld/",  # project home page, if any
    # project_urls={
    #     "Bug Tracker": "https://bugs.example.com/HelloWorld/",
    #     "Documentation": "https://docs.example.com/HelloWorld/",
    #     "Source Code": "https://code.example.com/HelloWorld/",
    # },
    classifiers=[
        "License :: OSI Approved :: MIT",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6"
    # could also include long_description, download_url, etc.
)
