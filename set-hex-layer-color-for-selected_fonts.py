from vanilla.dialogs import *
import os
from mojo.UI import AskString

layerName = AskString('Layer to adjust color of, e.g. "background"')

hexColor = AskString('Hex color, e.g. "2F3137" or "#9560FF"')

files =  getFile("Select files to update", allowsMultipleSelection=True, fileTypes=["ufo"])

def RGBAfromHex(hex):
    h = hex.lstrip('#')
    RGB = tuple(int(h[i:i+2], 16) for i in (0, 2 ,4))
    r1, g1, b1, a1 = RGB[0] / 255, RGB[1] / 255, RGB[2] / 255, 1
    return(r1, g1, b1, a1)

for file in files:
    font = OpenFont(file)
    
    rgbaColor = RGBAfromHex(hexColor)
    font.getLayer(layerName).color = rgbaColor
    print(font)
    print(f'{layerName} color updated to {rgbaColor}')

    font.save()
    font.close()




