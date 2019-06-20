### make selected suffixed glyphs into defaults

import datetime

f = CurrentFont()

glyphsToMakeDefault = f.selectedGlyphNames
    
for selectedGlyph in glyphsToMakeDefault:
    
    for font in AllFonts():
        
        print(font.info.styleName)
        
        if selectedGlyph in font:
    
            splitAltGlyphName = font[selectedGlyph].name.split('.')

            # check that selected glyph has a suffix
            if len(splitAltGlyphName) == 2:    
                 ## get unicode of default glyph
                defaultUnicodes = font[splitAltGlyphName[0]].unicodes
    
                ## get default glyph (with no suffix) and make duplicate of it with current timestamp
                # now = datetime.datetime.now()
                # dupedDefaultGlyphName = splitAltGlyphName[0] + "." + now.strftime("%Y_%m_%d-%Hh%Mm%Ss")
        
                dupedDefaultGlyphName = splitAltGlyphName[0] + "." + "replaced_with_" + splitAltGlyphName[1]
    
                # if the new glyph name already exists, don't overwrite it with the new one
                if dupedDefaultGlyphName in font.keys():
                    print("sorry," + dupedDefaultGlyphName + " already exists in " + font.info.styleName)
        
                # if the new glyph name doesn't already exist..
                else:
        
                    # duplicate the selected glyph with the new glyph name
                    font.insertGlyph(font[splitAltGlyphName[0]], dupedDefaultGlyphName)
                    font[dupedDefaultGlyphName].unicode = None
    
                    # get suffixed glyph and use it to replace the former default
    
                    font.insertGlyph(f[selectedGlyph], splitAltGlyphName[0])
    
                    # attach stored default unicodes to newly-created default glyph
                    font[splitAltGlyphName[0]].unicodes = defaultUnicodes
    
                    # now that it has been made the default, delete the suffixed glyph
                    if selectedGlyph in font.keys():
                        font.removeGlyph(selectedGlyph)
            
                    # the new default is at the end, so this will re-apply a "smart sort" to the font
                    newGlyphOrder = font.naked().unicodeData.sortGlyphNames(font.templateGlyphOrder, sortDescriptors=[dict(type="cannedDesign", ascending=True, allowPseudoUnicode=True)])
                    font.templateGlyphOrder = newGlyphOrder
            else:
                print("sorry, '" + selectedGlyph + "' is already a default (non-suffixed) glyph")