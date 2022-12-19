import importlib.metadata

from setuptools import setup

VERSION = importlib.metadata.version("proxy-app")

OPTIONS = {
    "py2app": {"iconfile": "icons/icon.png", "plist": {"CFBundleShortVersionString": VERSION, "LSUIElement": True}}
}

setup(
    app=["src/main_dummy.py"],
    name="Proxy",
    packages=["src"],
    options=OPTIONS,
    setup_requires=["py2app"],
)
