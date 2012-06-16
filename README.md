## Summary
SublimePythonTidy is a python formatting plugin based on the [PythonTidy](http://pypi.python.org/pypi/PythonTidy) script for Sublime Text 2. Currently, we are using [version 1.23 of PythonTidy](http://lacusveris.com/PythonTidy/PythonTidy-1.23.python) 

## Features
* All of the formatting features included by PythonTidy!

## Installation
Clone this repository in to the Sublime Text 2 "Packages" directory, which is located wherever the "Preferences" -> "Browse Packages" option in sublime takes you. A restart of Sublime may be necessary.

## Usage
The default key binding is "super+shift+o". Alternatively, you can do open the command pallette via "super+shift+p" and enter "Format (Tidy): Python". This will format your entire opened file. Currently, there is no support for formatting of a highlighted selection.

## Should I use PythonTidy or PythonFormat?
I have another Sublime Text 2 plugin, called [PythonFormat](https://github.com/davidleibovic/PythonFormat).  

SublimePythonTidy will be more reliable and less likely to screw up your code, as it uses a more mature, better tested formatter. SublimePythonTidy works by parsing the abstract syntax tree of your Python code. As such, it requires the file being formatted to be valid Python syntax. If you forgot to insert a colon or some other symbol, SublimePythonTidy will not be able to run. PythonFormat, on the other hand, will still make an attempt at formatting your code, even if it is not valid Python syntax.

Here is a sample of how the formatting style compares (I personally happen to prefer the style used by PythonFormat).

### Input:
    if self.opts.max_preserve_newlines == 0 or self.opts.max_preserve_newlines > self.n_newlines:
### PythonFormat Output:
    if (self.opts.max_preserve_newlines == 0 or
        self.opts.max_preserve_newlines > self.n_newlines):
### SublimePythonTidy Output:
    if self.opts.max_preserve_newlines == 0 \
        or self.opts.max_preserve_newlines \
        > self.n_newlines:

### Input:
    self.operators = ['!=', '%', '&', '*', '**', '+', '+=', '-=', '-', '/','//', '<', '<<', '<=', '~', '==', '=', '>', '>=', '>>','^', '|', '<>', '*=', '/=', '%=', '**=', '//=', '|=','&=', '^=']
### PythonFormat Output:
    self.operators = ['!=', '%', '&', '*', '**', '+', '+=', '-=', '-', '/',
                      '//', '<', '<<', '<=', '~', '==', '=', '>', '>=', '>>',
                      '^', '|', '<>', '*=', '/=', '%=', '**=', '//=', '|=',
                      '&=', '^=']
### SublimePythonTidy Output:
	self.operators = [
            '!=',
            '%',
            '&',
            '*',
            '**',
            '+',
            '+=',
            '-=',
            '-',
            '/',
            '//',
            '<',
            '<<',
            '<=',
            '~',
            '==',
            '=',
            '>',
            '>=',
            '>>',
            '^',
            '|',
            '<>',
            '*=',
            '/=',
            '%=',
            '**=',
            '//=',
            '|=',
            '&=',
            '^=',
            ]

## Disclaimer
SublimePythonTidy has been tested extensively, but it can still screw up your code. Always save a backup and test to make sure nothing got wrecked! In particular, running this on newer versions of Python may introduce unexpected behavior.

