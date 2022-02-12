#!/bin/env python3

import argparse,json,math,os,time
import PythonMagick as Magick

def addWx():
    xPos=15
    yPos=290

    try:
        deltasec=time.time()-os.path.getmtime(wxfile)
    except:
        print("Could not get mtime of {0:s}".format(wxfile))
        return

    if deltasec > 120:
        return

    wxfields=[
            { "out": " Temp: {0: 5.1f} °F",        "value": "tempf"        },
            { "out": "DewPt: {0: 5.1f} °F",        "value": "dewptf"       },
            { "out": "  Hum: {0: 5.1f}%",          "value": "humidity"     },
            {},
            { "out": " Wind: {0: 5.1f} mph",       "value": "windspeedmph" },
            { "out": " Gust: {0: 5.1f} mph",       "value": "windgustmph"  },
            { "out": "  Dir: {0: 5.0f}°",          "value": "winddir"      },
            {},
            { "out": "  Pressure: {0: 6.2f} inHg", "value": "baromin"      },
            { "out": "Daily Rain: {0: 6.1f} in",   "value": "dailyrainin"  },
            ]

    try:
        with open(wxfile,'r') as wx_file:
            wxdata = json.load(wx_file)
            wx_file.close()
    except:
        print("Reading of {0:s} failed.".format(wxfile))
        exit()
    
    for field in wxfields:
        try:
            img.draw( Magick.DrawableText(xPos,yPos, field['out'].format(wxdata[field['value']])))
        except:
            try:
                outarr.append("text {0:0.0f},{1:0.0f} '{2:s}'".format(xPos,yPos,field['out'].format(wxdata[field['value']])))
            except:
                pass
        yPos+=fontPoint*1.3333


def addCardinals():
    c = {
        "N":calcXY(math.pi),
        "W":calcXY(math.pi/2),
        "S":calcXY(0),
        "E":calcXY(math.pi*1.5)
        }
    try:
        img.fontPointsize(40)
        img.fillColor(Magick.Color('white'))
    except:
        pass
    for i in c:
        try:
            img.draw( Magick.DrawableText(c[i]['X'], c[i]['Y'], i) )
        except:
            try:
                outarr.append("text {0:0.0f},{1:0.0f} '{2:s}'".format(c[i]['X'], c[i]['Y'], i))
            except:
                pass
    return

def calcXY(angle):
    X = cX + ( R * math.sin(dTheta + angle))
    Y = cY + ( R * math.cos(dTheta + angle))
    return { "X": X, "Y": Y }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--cardinals", action = 'store_true',   help="Add Cardinals")
    parser.add_argument("-r", "--radius",    default = 100, type=int, help="Cardinals: Radius")
    parser.add_argument("-x", "--cx",        default = 150, type=int, help="Cardinals: Center X Pixel")
    parser.add_argument("-y", "--cy",        default = 150, type=int, help="Cardinals: Center Y Pixel")
    parser.add_argument("-d", "--dTheta",    default = 0,   type=int, help="Cardinals: Angle Delta in Degrees ( 0 = North, 90 = due East, 180 = South, 270 = due West )")

    parser.add_argument("-w", "--weather",   action = 'store_true',  help="Add Weather")
    parser.add_argument("-f", "--wxfile",    default = '',           help="Weather JSON file")
    parser.add_argument("-i", "--infile",    default = '',           help="Image file to manipulate")
    parser.add_argument("-o", "--outfile",   default = '',           help="Output file")
    args = parser.parse_args()

    cardinals  = args.cardinals
    R          = args.radius
    cX         = args.cx
    cY         = args.cy
    dTheta     = (args.dTheta * 2 * math.pi)/360

    weather    = args.weather
    wxfile     = args.wxfile

    infile     = args.infile
    outfile    = args.outfile

    outarr = []
    myFont="/usr/share/fonts/truetype/noto/NotoMono-Regular.ttf"

    fontPoint=30

    if infile!="" and outfile!="":
        if os.path.isfile(infile):
            img = Magick.Image(infile)
            img.font(myFont)
            img.fontPointsize(fontPoint)
            img.fillColor(Magick.Color('grey'))
            img.strokeColor(Magick.Color('black'))

    if weather:
        addWx()
    if cardinals:
        addCardinals()

    try:
        img.write(outfile)
    except:
        print(" ".join(outarr))
 
