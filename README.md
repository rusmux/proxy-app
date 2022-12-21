<br>

<img src="src/app/icons/icon.png" alt="Icon" width="200px"/>

# Proxy App

[![version](https://img.shields.io/badge/Version-0.1.0-brightgreen)]()
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://wemake-python-styleguide.readthedocs.io/en/latest/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![codecov](https://codecov.io/github/rusmux/proxy-app/branch/main/graph/badge.svg?token=EXBDH0NYIB)](https://codecov.io/github/rusmux/proxy-app)


Control your macOS proxy from the menu bar. Instead of going to the proxy settings and turning proxy on/off
manually, you can now simply do it from the menu bar.

The application is written using [rumps](https://github.com/jaredks/rumps) framework.

<img src="images/1.png" alt="Example" height="350px">&emsp;<img src="images/2.png" alt="Example" height="350px">


# Installation

There seems to be a problem with using the py2app installer together with python dependency-injector. This [issue](https://github.com/ets-labs/python-dependency-injector/issues/438) was also with the PyInstaller. Because of this problem, it is impossible to distribute the application easily and independently of the codebase. To use the application, clone this repository, create a virtual environment, and run the commands:

```Bash
poetry install
make build_dev
```

This will create an application in the `dist` folder, which you can then put anywhere and use as long as the virtual environment and repository are on your computer.
