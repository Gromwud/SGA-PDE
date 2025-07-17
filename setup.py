from setuptools import setup, find_packages

setup(
    name="dso",
    version="0.1.0",
    packages=find_packages(where="."),  # Or explicitly: packages=['dso.dso']
    package_dir={"": "."},  # Important for nested structure
    install_requires=[
    ],
    python_requires=">=3.7",
)