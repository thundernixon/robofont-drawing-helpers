'''
Generate a number of interpolation and extrapolation steps between two selected glyphs in the current font.

Modified from https://robofont.com/documentation/building-tools/toolspace/scripts/scripts-interpolation/
'''

# settings
factor = 0.333 # between 0 & 1
#extrapolateSteps = 0

# get the currentFont
f = CurrentFont()

if f is None:
    # no font open
    print("Oeps! There is not font open.")

else:
    # get the selection
    selection = f.selectedGlyphNames
    
    print(selection)

    # check if the selection contains only two glyphs
    if len(selection) != 2:
        print("Incompatible selection: two compatible glyphs are required.")

    else:
        # TODO: sort list by glyph width?
        # get the master glyphs
        source1 = f[selection[0]]
        source2 = f[selection[1]]

        baseNameOfGlyph1 = selection[0].split('.')[0]
        # check if they are compatible
        if not source1.isCompatible(source2)[0]:
            # the glyphs are not compatible
            print("Incompatible masters: Glyph %s and %s are not compatible." % (source1.name, source2.name))

        else:
            # create a new name
            # TODO: names might be better as percentages (?)
            name = f'{baseNameOfGlyph1}.interp-{str(factor).replace(".", "_")}'
        
            # create the glyph if does not exist
            dest = f.newGlyph(name)

            # interpolate between the two masters with the factor
            dest.interpolate(factor, source1, source2)

            # done!
            f.changed()