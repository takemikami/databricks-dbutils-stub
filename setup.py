import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="databricks-dbutils-stub",
    version="0.0.1",
    author="Mikami, Takeshi",
    author_email="takeshi.mikami@gmail.com",
    description="test stub for databricks utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/takemikami/databricks-dbutils-stub",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
