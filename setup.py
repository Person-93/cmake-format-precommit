from setuptools import setup

setup(name="cmakelang-precommit-dummy",
      version="0.0.0",
      description="precommit hooks for person93's fork of cmakelang",
      install_requires=[
          "cmakelang @ https://github.com/Person-93/cmake_format/archive/refs/tags/person93-0.6.14+0.6.13.tar.gz"
      ])
