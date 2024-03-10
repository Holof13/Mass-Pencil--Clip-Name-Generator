# Mass Pencil Clip Generator

## Usage 

This script is designed to grab a list of names and mass generate .scad files and using the cli utility for OpenSCAD, export them to .stl files. It's a really basic program that depends on a template .scad file and replaces words in it to generate individual .scad files and then iterates though them exporting them to .stl files.

For example, the list:

```
John
John
John
Marco 2
```
Will give the following files in .scad format and export them in .stl format

```
JOHN-1
JOHN-2
JOHN-3
MARCO-1
MARCO-2
```
It's set up this way so you can drag all of the .stl files into a slicer and set up a whole bed of prints without having to keep track of the amount of names.

Please keep in mind this is just a script I made to accelerate my workflow (as such, it might be a mess.) with some commissions for some designs, so if you have any improvements open a pull request.

You can change the font in the template but note that only a few work with the library in the requirements, so refer to them to see what fonts are available.

## Requirements

- Have a functional OpenSCAD installation, in Windows it should be located on your program files folder, if not you can change line 71 of the script to the location of your installation:
```python
scad_path = "\"C:\Program Files\OpenSCAD\openscad.exe\""
```
- [This](https://www.thingiverse.com/thing:3004457) library by arpruss.

### License

MIT License

Copyright (c) 2024 Holof

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.