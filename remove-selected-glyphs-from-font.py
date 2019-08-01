from vanilla.dialogs import *
import os
from mojo.UI import AskString

glyphsToRemoveString = AskString('space-separated list of glyphs to remove from current font')
glyphsToRemove = glyphsToRemoveString.split(" ")

f = CurrentFont()

# copy space-separated glyph names here
# glyphsToRemove = list(f.selectedGlyphNames)

# FONT KEYs -----------------------------------------------

# clean up the rest of the data
for glyphName in glyphsToRemove:
    # remove from keys
    # if glyphToRemove in f.keys():
    if glyphName in f:
        del f[glyphName]
    else:
        print("font does not contain a glyph named '%s'" % glyphName)

# LAYERS --------------------------------------------------

for layerName in f.layerOrder:
    layer = f.getLayer(layerName)
    for glyphToRemove in glyphsToRemove:
        if glyphToRemove in layer:
            del layer[glyphToRemove]
        else:
            print("%s does not contain a glyph named '%s'" %
                  (layerName, glyphToRemove))


# GLYPH ORDER ---------------------------------------------

glyphOrder = f.glyphOrder

for glyphName in glyphsToRemove:
    if glyphName in glyphOrder:
        glyphOrder.remove(glyphName)

f.glyphOrder = glyphOrder

# KERNING -----------------------------------------------------------

for glyphName in glyphsToRemove:
    # iterate over all kerning pairs in the font
    for kerningPair in f.kerning.keys():

        # if glyph is in the kerning pair, remove it
        if glyphName in kerningPair:
            print('removing kerning pair (%s, %s)...' % kerningPair)
            del f.kerning[kerningPair]

# COMPONENTS -------------------------------------------------------

# iterate over all glyphs in the font
for glyph in f:

    # skip glyphs which components
    if not glyph.components:
        continue

    # iterate over all components in glyph
    for component in glyph.components:

        # if the base glyph is the glyph to be removed
        if component.baseGlyph in glyphsToRemove:
            # delete the component
            glyph.removeComponent(component)
