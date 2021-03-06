import setuptools

# Use the readme file as the long description on PyPi
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='iridauploader',
    version='0.4.2',
    description='IRIDA uploader: upload NGS data to IRIDA system',
    url='https://https://github.com/phac-nml/irida-uploader',
    author='Jeffrey Thiessen',
    author_email='jeffrey.thiessen@canada.ca',
    long_description=long_description,
    long_description_content_type="text/markdown",
    # license specified on github
    license='Apache-2.0',
    keywords="IRIDA NGS uploader",
    packages=setuptools.find_packages(include=['iridauploader',
                                               'iridauploader.*',
                                               ]),
    install_requires=['rauth',
                      'requests',
                      'appdirs',
                      'cerberus',
                      'argparse',
                      'requests-toolbelt',
                      ],
    # https://pypi.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    # Test cases makes make it incompatible with pre 3.5
    python_requires='>=3.5',

)
