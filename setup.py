from setuptools import setup, find_packages

setup(
    name='find-free-lunch',
    version='0.1.0',
    author='Aaditya Thakur',
    description='Run benchmarks to find the best performing model for your dataset',
    packages=find_packages(),
    install_requires=[
        'scikit-learn'
    ],
)