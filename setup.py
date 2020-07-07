import setuptools

setuptools.setup(
    name="nbhelpers-tiwo",
    version="0.0.1",
    author="tiwo",
    author_email="tiwocode@gmail.com",
    description="A few helpers I use in IPython notebooks",
    url="https://github.com/tiwo/nbhelpers",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
)