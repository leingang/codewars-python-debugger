# codewars-python-template

A codewars python kata

## Developing

Use a python 3.6 virtual environment. I use the same one for all codewars katas:

    virtualenv-3.6 ~/.local/share/virtualenvs/codewars
    . ~/.local/share/virtualenvs/codewars/bin/activate

Then:

    python -m pip install -r requirements.txt

This installs the Codewars test suite as a python package.

## Testing

Work in a module called `solution.py`.  Put the sample tests in `test.py`.

The module `utils.py` provides a logging object whch is useful for debugging
and introspection.

## Submitting

Strip out the logging lines:

    sed -e '/logger/d' -e '/logging/d' solution.py | pbcopy

Then paste into the Codewars edit window.
