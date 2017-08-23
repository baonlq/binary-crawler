from setuptools import setup, find_packages

setup(
    name='binary-crawler',
    version='0.0.1',
    url='https://github.com/baonlq/binary-crawler',
    download_url='https://github.com/baonlq/binary-crawler',
    author='Andrea Grandi',
    author_email='a.grandi@gmail.com',
    description='Python client library for Toshl API.',
    packages=find_packages(exclude=['tests']),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    license='MIT',
    install_requires=[
        'splinter',
    ],
)
