[![Python application test with Github Actions](https://github.com/felipezzz1/microsservices-python/actions/workflows/devops.yml/badge.svg)](https://github.com/felipezzz1/microsservices-python/actions/workflows/devops.yml)

## Steps

1. Create a Python virtual environment `python3 -m venv ~/.venv` or `virtualenv ~/.venv`
2. Create Files: `Makefile`, `requirements.txt`, `main.py`, `Dockerfile`, `mylib/__init__.py`
3. Populate `Makefile`
4. Setup Continuous Integration, for example check code for issues like lint errors
5. Build cli using Python Fire library `./cli-fire.py` to test the logic
6. 
