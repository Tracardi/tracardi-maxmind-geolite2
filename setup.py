from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='tracardi-maxmind-geolite2',
    version='0.6.0',
    description='This plugins connect to maxmind geolite2 service and retrieve location data.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Risto Kowaczewski',
    author_email='risto.kowaczewski@gmail.com',
    packages=['tracardi_maxmind_geolite2'],
    install_requires=[
        'tracardi_plugin_sdk>=0.6.21',
        'tracardi',
        'tracardi_dot_notation',
        'geoip2~=4.2.0'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    keywords=['tracardi', 'plugin'],
    include_package_data=True,
    python_requires=">=3.8",
)
