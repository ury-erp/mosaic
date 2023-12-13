from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in ury_mosaic/__init__.py
from ury_mosaic import __version__ as version

setup(
	name="ury_mosaic",
	version=version,
	description="KOT(Kitchen Order Ticket) Management Software",
	author="Tridz Technologies",
	author_email="info@tridz.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
