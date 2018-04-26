### copy and decompose glyphs with new names

from mojo.UI import *

f = CurrentFont()

glyphsToCopy = f.selection

newGlyphSuffix = AskString('Enter a new suffix for duplicate glyphs, e.g. "alt1"')

print(newGlyphSuffix)

for glyph in glyphsToCopy:
    baseNameOfGlyph = glyph.split('.')[0]
    newGlyphName = baseNameOfGlyph  + "." + newGlyphSuffix
    
    if newGlyphName in f.glyphOrder:
        print("sorry," + newGlyphName + " already exists.")
    if newGlyphName not in f.glyphOrder:
        f.insertGlyph(f[glyph], newGlyphName)
        print(newGlyphName + " is created!")
        