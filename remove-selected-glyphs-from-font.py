f = CurrentFont()

# copy space-separated glyph names here
glyphsToRemove = list(f.selectedGlyphNames)

# FONT KEYs -----------------------------------------------

# clean up the rest of the data
for glyphToRemove in glyphsToRemove:
    # remove from keys
    # if glyphToRemove in f.keys():
    if glyphToRemove in f:
        del f[glyphToRemove]
    else:
        print("font does not contain a glyph named '%s'" % glyphName)
        

# GLYPH ORDER ---------------------------------------------

glyphOrder = f.glyphOrder

for glyphName in glyphsToRemove:
    if glyphName in glyphOrder:
        glyphOrder.remove(glyphName)

f.glyphOrder = glyphOrder

# KERNING -----------------------------------------------------------

for glyphToRemove in glyphsToRemove:
    # iterate over all kerning pairs in the font
    for kerningPair in f.kerning.keys():

        # if glyph is in the kerning pair, remove it
        if glyphToRemove in kerningPair:
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

