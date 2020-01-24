from setuptools import setup, find_packages


setup(
    name='rflib',
    version='0.1',
    description='This is a test for a tutorial on how to create a python library',  # noqa
    url='git@github.com:r-farias/rflib.git',
    download_url='https://github.com/r-farias/rflib/archive/v0.1.tar.gz',  # noqa
    author='Roberto Farias',
    author_email='rfarias@comparaonline.com',
    license='MIT',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
    ]
)