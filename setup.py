#!/usr/bin/env python
from setuptools import (
    find_packages,
    setup,
)

extras_require = {
    "dev": [
        "build>=0.9.0",
        "bump_my_version>=0.19.0",
        "ipython",
        "mypy==1.10.0",
        "pre-commit>=3.4.0",
        "tox>=4.0.0",
        "twine",
        "wheel",
    ],
    "docs": [
        "sphinx>=6.0.0",
        "sphinx-autobuild>=2021.3.14",
        "sphinx_rtd_theme>=1.0.0",
        "towncrier>=24,<25",
    ],
    "test": [
        "pytest>=7.0.0",
        "pytest-xdist>=2.4.0",
    ],
    # optional backends:
    "pycryptodome": [
        "pycryptodome>=3.6.6,<4",
    ],
    "pycryptodomex": [
        "pycryptodomex>=3.6.6,<4",
    ],
    "pysha3": [
        "pysha3>=1.0.0,<2.0.0;python_version<'3.9'",
        "safe-pysha3>=1.0.0;python_version>='3.9'",
    ],
}

extras_require["dev"] = (
    extras_require["dev"] + extras_require["docs"] + extras_require["test"]
)

with open("./README.md") as readme:
    long_description = readme.read()


setup(
    name="eth-hash",
    # *IMPORTANT*: Don't manually change the version here. Use `make bump`, as described in readme
    version="0.7.1",
    description="""eth-hash: The Ethereum hashing function, keccak256, sometimes (erroneously) called sha3""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="The Ethereum Foundation",
    author_email="snakecharmers@ethereum.org",
    url="https://github.com/ethereum/eth-hash",
    include_package_data=True,
    install_requires=[],
    python_requires=">=3.8, <4",
    extras_require=extras_require,
    py_modules=["eth_hash"],
    license="MIT",
    zip_safe=False,
    keywords="ethereum",
    packages=find_packages(exclude=["scripts", "scripts.*", "tests", "tests.*"]),
    package_data={"eth_hash": ["py.typed"]},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
)
