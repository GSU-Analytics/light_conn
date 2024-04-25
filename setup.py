from setuptools import setup, find_packages

setup(
    name='LightOracleConnection',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'keyring',
        'oracledb'
    ],
    author='Isaac Kerson',
    author_email='ikerson@gsu.edu',
    description='A lightweight Oracle database connection handler.',
    keywords='oracle database connection pandas',
    url='https://github.com/yourusername/LightOracleConnection' 
)
