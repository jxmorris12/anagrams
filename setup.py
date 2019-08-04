import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="english_anagrams",
    version="0.0.1",
    author="jxmorris12",
    author_email="jxmorris12@gmail.com",
    description="A small package for finding anagrams of an english word",
    url="https://github.com/jxmorris12/english_anagrams",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
