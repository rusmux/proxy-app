.PHONY: build build_dev run run_test run_app clean coverage

clean:
	find . -type f -name "*.py[co]" -exec rm -r
	find . -type f -name ".DS_Store" -exec rm -r
	find . -type f -name ".coverage*" -exec rm -r

	find . -type d -name "__pycache__" -exec rm -r
	find . -type d -name ".pytest_cache" -exec rm -r
	find . -type d -name ".ipynb_checkpoints" -exec rm -r

build: clean
	rm -rf build dist
	python setup.py py2app

build_dev: clean
	rm -rf build dist
	python setup.py py2app --alias

run:
	python -u -m src.main

run_test:
	python -u -m tests.main

run_app:
	dist/Proxy.app/Contents/MacOS/Proxy

coverage:
	coverage run -m pytest
	coverage html
