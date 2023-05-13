from setuptools import setup
from zync.main import (
    NAME,
    DESCRIPTION,
    URL,
    VERSION,
    AUTHOR,
    AUTHOR_EMAIL,
    LICENSE,
)

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    url=URL,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license=LICENSE,
    packages=["zync"],
    install_requires=[],
    entry_points={
        "console_scripts": [
            "zync = zync.main:main",
        ],
    },
)
