'''
Generate a number of interpolation and extrapolation steps between two selected glyphs in the current font.

Modified from https://robofont.com/documentation/building-tools/toolspace/scripts/scripts-interpolation/
'''

# settings
interpolationSteps = 3
#extrapolateSteps = 0

# get the currentFont
f = CurrentFont()

if f is None:
    # no font open
    print("Oeps! There is not font open.")

else:
    # get the selection
    selection = f.selectedGlyphNames

    # check if the selection contains only two glyphs
    if len(selection) != 2:
        print("Incompatible selection: two compatible glyphs are required.")

    else:
        # get the master glyphs
        source1 = f[selection[0]]
        source2 = f[selection[1]]

        baseNameOfGlyph1 = selection[0].split('.')[0]
        # check if they are compatible
        if not source1.isCompatible(source2)[0]:
            # the glyphs are not compatible
            print("Incompatible masters: Glyph %s and %s are not compatible." % (source1.name, source2.name))

        else:
            # loop over the amount of required interpolations
            nameSteps = 0
            #for i in range(-extrapolateSteps, interpolationSteps + extrapolateSteps + 1, 1):
            for i in range(0, interpolationSteps + 1, 1):
                # create a new name
                
                # TODO: names might be better as percentages (?)
                
                name = baseNameOfGlyph1 + ".interp_%03i" % nameSteps
                
                           
                nameSteps += 1
                # create the glyph if does not exist
                dest = f.newGlyph(name)
                # get the interpolation factor (a value between 0.0 and 1.0)
                factor = i / float(interpolationSteps)
                # interpolate between the two masters with the factor
                dest.interpolate(factor, source1, source2)

            # done!
            f.changed()