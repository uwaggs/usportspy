from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    l_description = f.read()


setup(
    name='usportspy',
    version='0.0.6',
    packages=find_packages(),
    install_requires=[
        'requests',
        'pandas',
    ],
    description="One-Stop-Shop for USPORTS Data",
    long_description=l_description,
    long_description_content_type='text/markdown',
)
