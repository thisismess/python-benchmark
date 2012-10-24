from setuptools import setup

from benchmark import __VERSION__

setup(
    name='benchmark',
    version=__VERSION__,
    url='http://github.com/thisismess/python-benchmark',
    license='LICENSE.txt',
    author='Jack Shedd',
    author_email='jshedd@thisismess.com',
    description='Python benchmarker / benchmarking framework',
    long_description=open('README.txt').read(),
    packages=['benchmark'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Testing",
        "Topic :: System :: Benchmark",
    ]
)