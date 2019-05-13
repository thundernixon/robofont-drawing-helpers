# menutitle: Set Glyph Color in All Open Fonts
# shortcut: shift+command+control+c

from vanilla.dialogs import *
import os
from mojo.UI import AskString

hexColor = AskString('Hex color, e.g. "2F3137" or "#9560FF"')

f = CurrentFont()
fonts = AllFonts()

glyphsToUpdate = list(f.selectedGlyphNames)


def RGBAfromHex(hex):
    h = hex.lstrip('#')
    RGB = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    r1, g1, b1, a1 = RGB[0] / 255, RGB[1] / 255, RGB[2] / 255, 1
    return(r1, g1, b1, a1)


rgbaColor = RGBAfromHex(hexColor)

for font in fonts:
    for glyphName in glyphsToUpdate:
        f[glyphName].markColor = rgbaColor
