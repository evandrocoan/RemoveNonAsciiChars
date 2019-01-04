# RemoveNonAsciiChars

[![Build Status](https://travis-ci.org/evandrocoan/RemoveNonAsciiChars.svg?branch=master)](https://travis-ci.org/evandrocoan/RemoveNonAsciiChars)
[![Build status](https://ci.appveyor.com/api/projects/status/github/evandrocoan/RemoveNonAsciiChars?branch=master&svg=true)](https://ci.appveyor.com/project/evandrocoan/RemoveNonAsciiChars/branch/master)
[![codecov](https://codecov.io/gh/evandrocoan/RemoveNonAsciiChars/branch/master/graph/badge.svg)](https://codecov.io/gh/evandrocoan/RemoveNonAsciiChars)
[![Coverage Status](https://coveralls.io/repos/github/evandrocoan/RemoveNonAsciiChars/badge.svg?branch=master)](https://coveralls.io/github/evandrocoan/RemoveNonAsciiChars?branch=master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/a0e28fa3cf714ec5a53065e3c6064455)](https://www.codacy.com/app/evandrocoan/RemoveNonAsciiChars?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=evandrocoan/RemoveNonAsciiChars&amp;utm_campaign=Badge_Grade)
[![Latest Release](https://img.shields.io/github/tag/evandrocoan/RemoveNonAsciiChars.svg?label=version)](https://github.com/evandrocoan/RemoveNonAsciiChars/releases)
<a href="https://packagecontrol.io/packages/RemoveNonAsciiChars"><img src="https://packagecontrol.herokuapp.com/downloads/RemoveNonAsciiChars.svg"></a>

Simple plugin to replace non-ASCII characters to ASCII by removing accents,
and remaining non-ASCII characters.

Turns:

    á à â ä ñ

into

    a a a a n

and removes characters like:

    ¡ ¿ ß


## Installation

Installation via [Sublime Package Control][wbond].

1. [Install Sublime Package Control][wbond 2]
2. From inside Sublime Text, open Package Control's Command Pallet:
   <kbd>CTRL+SHIFT+P</kbd> (Windows, Linux) or <kbd>CMD+SHIFT+P</kbd> (Mac).
3. Type `install package` and hit Return. A list of available packages will
   be displayed.
4. Type `RemoveNonAsciiChars` and hit Return.


## Using

1. Bring out the command palette with <kbd>CTRL+SHIFT+P</kbd> (Windows,
   Linux) or <kbd>CMD+SHIFT+P</kbd> on Mac.
2. Type `Remove Non Ascii Chars` until you see the commands.
3. Select `Remove non Ascii characters (File)` for removing in the entire file,
   or `Remove non Ascii characters (Select)` for removing only in the selected
   text.

## Author

* Gabriel Perren - [@Gabriel-p](https://github.com/Gabriel-p)

Original [idea and code](http://stackoverflow.com/a/38909594/1391441) by
[Keith Hall](http://stackoverflow.com/users/4473405/keith-hall).


## License

[GPL-v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).


[wbond]: http://wbond.net/sublime_packages/package_control
[wbond 2]: http://wbond.net/sublime_packages/package_control/installation
