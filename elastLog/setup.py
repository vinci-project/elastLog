from setuptools import setup, find_packages
setup(
    name='elastLog',  # Required
    version='1.0.1',  # Required
    url='https://github.com/pypa/elastlog',  # Optional
    author='Vncsphere Foundation',  # Optional
    classifiers=[  # Optional
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    packages=find_packages(),  # Required
    install_requires=['elasticsearch'],  # Optional
)
