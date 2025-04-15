from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="jsonavigator",
    version="1.0.2",
    author="Nikhil Singh",
    author_email="nikhilraj7654@gmail.com",
    description="A Python package for handling nested JSON structures.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Nikhil-Singh-2503/JSONavigator",  # Optional: Link to your repository
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[],  # Add any dependencies here if needed
)
