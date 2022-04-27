# pyjpgclipboard

Cross platform clipboard for handling copy/paste jpg in python

This libray is meant to do only one thing and one thing well: copy jpg's to and from the
system clipboard.

We only support jpg images (and not any other formats or text) because manipulating the system
clipboard across different platforms is **Hard**. As of the creation of this repo there really
isn't any library that allows users to copy / paste images. There are a lot of libraries that
allow cross platform posting of text and binary data, but none that have native support for jpgs.

This is a problem if you are running a selenium test and you need to be able to test pasting
an image as part of your test suite (hence the motivation to create this library).

# Testing

Make sure that `tox` is installed on your system and run it at the root directory of this project.