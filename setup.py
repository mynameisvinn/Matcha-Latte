from setuptools import setup, find_packages

setup(
    name='Matcha',
    version='0.1',
    description='Testbed for Skill-Based Matchmaking',
    author='Vin Tang',
    author_email='vin.tang@gmail.com',
    install_requires=["numpy"],
    packages=find_packages(),
)