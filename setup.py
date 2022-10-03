from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in ecta_dispatch/__init__.py
from ecta_dispatch import __version__ as version

setup(
	name="ecta_dispatch",
	version=version,
	description="module to control ecta dispatches",
	author="Across Express",
	author_email="acrossexpressplc@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
