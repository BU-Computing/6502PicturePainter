# 6502PicturePainter
## Overview
This utility enables you to paint pictures using the provided Excel template and then convert them to 6502 Assembly using the Python script!
## Drawing Your Picture
You must draw your picture within the provided Excel template. To do this, open the template file, from there you can edit the value of each cell to change it's colour. The table below shows the available colour values.

| Colour      | Cell Value |
|-------------|------------|
| Black       | B          |
| White       | W          |
| Red         | R          |
| Cyan        | C          |
| Purple      | P          |
| Blue        | BL         |
| Yellow      | Y          |
| Orange      | O          |
| Brown       | BR         |
| Light Red   | LR         |
| Dark Grey   | DG         |
| Grey        | GR         |
| Light Green | LG         |
| Light Blue  | LB         | 

## Prepare Picture for Conversion

Once you are finished drawing, you must prepare your picture for conversion. To do this save your picture as a CSV file. This can be done by way of the normal save dialog by simply changing the save as type to CSV (Comma Delimited)

![saveas]

[saveas]:http://i.imgur.com/KTBOCMk.png "A screenshot from Excel showing the correct save as type."

## Converting Your Picture
To convert your picture, execute PicturePainter.py and follow the on-screen instructions!

## Requirements
1. Python 2.7
2. Microsoft Office Excel 2010 or Newer (may work on older versions but not tested)
