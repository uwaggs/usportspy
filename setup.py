from setuptools import setup, find_packages

with open('PYPI.md', 'r') as f:
    l_description = f.read()


setup(
    name='usportspy',
    version='0.0.11',
    packages=find_packages(),
    install_requires=[
        'requests',
        'pandas',
        'pyjanitor',
    ],
    description="Extract and Analyze Data from U SPORTS, the Governing Body of University Sport in Canada. ",
    long_description=l_description,
    long_description_content_type='text/markdown',
)
