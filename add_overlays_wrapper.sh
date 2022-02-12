#!/bin/bash
#
#  usage: add_overlays.py [-h] [-c] [-r RADIUS] [-x CX] [-y CY] [-d DTHETA] [-w]
#                         [-f WXFILE] [-i INFILE] [-o OUTFILE]
#  
#  optional arguments:
#    -h, --help            show this help message and exit
#    -c, --cardinals       Add Cardinals
#    -r RADIUS, --radius RADIUS
#                          Cardinals: Radius
#    -x CX, --cx CX        Cardinals: Center X Pixel
#    -y CY, --cy CY        Cardinals: Center Y Pixel
#    -d DTHETA, --dTheta DTHETA
#                          Cardinals: Angle Delta in Degrees ( 0 = North, 90 =
#                          due East, 180 = South, 270 = due West )
#    -w, --weather         Add Weather
#    -f WXFILE, --wxfile WXFILE
#                          Weather JSON file
#    -i INFILE, --infile INFILE
#                          Image file to manipulate
#    -o OUTFILE, --outfile OUTFILE
#                          Output file
#  
#

/home/pi/bin/add_overlays.py -w -f /home/pi/wxmap.json -c -r 1012 -x 1480 -y 1047 -d 30 -i $1 -o $2
#/home/pi/bin/add_overlays.py -w -f /home/pi/wxmap.json -c -r 1040 -x 1480 -y 1090 -d 222 -i $1 -o $2
