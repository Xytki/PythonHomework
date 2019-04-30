from setuptools import setup, find_packages

DESCRIPTION = "Python command line calculator"


setup(
    name="pycalc",
    version="0.0.4",
    author="Aliaksei Zviahau",
    author_email="skomorosi@gmail.com",
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    url="https://github.com/Xytki/PythonHomework",
    packages=find_packages(),
    entry_points={
        "console_scripts": ["pycalc=pycalc.pycalc:main"]},
    package_data={'': ['README.md']},
    include_package_data=True,
    tests_require=["nose"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
