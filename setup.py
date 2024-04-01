import setuptools

def readme():
    try:
        with open("README.md") as f:
            return f.read()
    except IOError:
        return ""


setuptools.setup(
    name="psgresizer",
    version="5.0.1",
    author="PySimpleSoft Inc.",
    install_requires=["PySimpleGUI>=5","Pillow"],
    description="PySimpleGUI  application / utility to resize your images and encode them to Bas64 format.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    license="Free To Use But Restricted",
    keywords="GUI UI PySimpleGUI tkinter psgresizer base64 resize pil pillow",
    url="https://github.com/PySimpleGUI/psgresizer",
    packages=["psgresizer"],
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: Free To Use But Restricted",
        "Operating System :: OS Independent",
        "Framework :: PySimpleGUI",
        "Framework :: PySimpleGUI :: 5",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Software Development :: User Interfaces",
    ],
    package_data={"":
        ["*", "*.*"]
                  },
    entry_points={"gui_scripts": [
        "psgresizer=psgresizer.psgresizer:main_entry_point"
    ], },
)



