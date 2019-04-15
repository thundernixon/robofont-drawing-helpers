

from lib.tools.bezierTools import curveConverter
from vanilla.dialogs import *



inputFonts = getFile("select masters to add feature code to", allowsMultipleSelection=True, fileTypes=["ufo"])

for fontPath in inputFonts:
    # font = CurrentFont()
    font = OpenFont(fontPath, showInterface=False)

    coreFont = font.naked()

    for glyph in coreFont:
        # convert from cubic to quad
        curveConverter.bezier2quadratic(glyph)
    
        # convert from quad to cubic
        # curveConverter.quadratic2bezier(glyph)
    
    coreFont.segmentType = glyph.segmentType
    
    font.save()
    font.close()

print("done")