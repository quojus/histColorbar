from setuptools import setup, find_packages

setup(
    name='histoColorbar',
    version='0.1.4',
    packages=find_packages(),
    description='Histogramm mit Farbskala in Matplotlib',
    long_description=open('README.md').read(),
    url='https://github.com/quojus/histoColorbar',
    author='Falk',
    install_requires=[
        'numpy',
        'matplotlib'
    ],
    python_requires='>=3.6',
)
