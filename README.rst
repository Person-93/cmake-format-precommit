==============================
Pre-commit Hooks for cmakelang
==============================

This repository contains configuration for linting and formatting cmake files using
`precommit <https://pre-commit.com/>`_.

It uses `this fork <https://github.com/Person-93/cmake_format>`_ of cmakelang.

-----
Usage
-----

To add ``cmake-format`` and ``cmake-lint`` to your pre-commit configuration,
add something like the following to your ``.pre-commit-config.yaml`` file:

.. code:: yaml

   repos:
     - repo: https://github.com/Person-93/cmake-format-precommit
       rev: v0.1.0
       hooks:
       - id: cmake-format
       - id: cmake-lint
