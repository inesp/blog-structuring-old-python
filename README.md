# Structuring old Python code

This repository is code accompanying my blog post [Structuring old Python code](http://inesp.github.io/2019/09/15/structuring-old-python-code.html).

This repo is a demonstration of how you can transition your code from passing unstructured dictionaries from one function to the next and towards passing structured `dataclasses` and sprinkling a few type hints in the process.

Should you want to run it, it depends on Python 3.7+ and `pipenv`. 

Once you have both installed, run 
```bash
pipenv install
```
to install all dependencies and 
```bash
pipenv run python main.py
```
to run the code in main.py.
