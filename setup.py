import importlib.metadata

from setuptools import find_packages, setup

VERSION = importlib.metadata.version("proxy-app")

OPTIONS = {
    "py2app": {
        "iconfile": "src/app/icons/icon.png",
        "plist": {"CFBundleShortVersionString": VERSION, "LSUIElement": True},
    }
}

if __name__ == "__main__":
    setup(
        app=["src/main.py"],
        name="Proxy",
        packages=find_packages(exclude=["*tests*"]),
        package_data={"": ["icons/*"]},
        include_package_data=True,
        options=OPTIONS,
        setup_requires=["py2app"],
    )
