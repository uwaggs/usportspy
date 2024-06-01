from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    description = f.read()


setup(
    name='usportspy',
    version='0.0.3',
    packages=find_packages(),
    install_requires=[
        'requests',
        'pandas',
    ],
    long_description=description,
    long_description_content_type='text/markdown',
)
