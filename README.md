# pyjpgclipboard

## Platform Unit Tests

[![Actions Status](https://github.com/zackees/pyjpgclipboard/workflows/MacOS_Tests/badge.svg)](https://github.com/zackees/pyjpgclipboard/actions/workflows/test_macos.yml)
[![Actions Status](https://github.com/zackees/pyjpgclipboard/workflows/Win_Tests/badge.svg)](https://github.com/zackees/pyjpgclipboard/actions/workflows/test_win.yml)
[![Actions Status](https://github.com/zackees/pyjpgclipboard/workflows/Ubuntu_Tests/badge.svg)](https://github.com/zackees/pyjpgclipboard/actions/workflows/test_ubuntu.yml)

Note: Ubuntu/Linux is not implemented yet. Feel free to submit a pull request!

## Brief

Cross platform clipboard for handling copy/paste jpg in python

This libray is meant to do only one thing and one thing well: copy jpg's to and from the
system clipboard.

## Api

```
from pyjpgclipboard import clipboard_dump_jpg, clipboard_load_jpg

clipboard_load_jpg("myfile.jpg") # Clipboard now has jpg image
clipboard_dump_jpg("myfile2.jpg) # Clipboard image contents dumped to disk.
```

## Testing

Make sure that `tox` is installed on your system and run it at the root directory of this project.


## Will pyjpgclipboard support more features?

Probably not. Unless it's *really* important.

We only support jpg images (and not any other formats or text) because manipulating the system
clipboard across different platforms is **Hard**. As of the creation of this repo there really
isn't any library that allows users to copy / paste jpegs. There are a lot of libraries that
allow cross platform posting of text and binary data. So this library is intended to fill in that
gap. Libraries like `pyclip` should, in the future, use `pyjpgclipboard` to handle the missing jpg
clipboard manipulation.

## What motivatated this library?

Selenium webdriver tests has a missing feature of taking an image and pasting it through it's
api. 

This is a problem if you are running a selenium test and you need to be able to test pasting
an image as part of your test suite (hence the motivation to create this library).

## Footguns

There is only one system clipboard. So running this library in different threads/processes will
result in collisions. It's up to the application running this library to provide any necessary
locking mechanism.