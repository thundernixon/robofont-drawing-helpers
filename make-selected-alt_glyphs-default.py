### make selected suffixed glyphs into defaults

import datetime

f = CurrentFont()
    
for selectedGlyph in f.selectedGlyphNames:
    
    splitAltGlyphName = f[selectedGlyph].name.split('.')

    # check that selected glyph
    if len(splitAltGlyphName) == 2:    
         ## get unicode of default glyph
        defaultUnicodes = f[splitAltGlyphName[0]].unicodes
    
        ## get default glyph (with no suffix) and make duplicate of it with current timestamp
        # now = datetime.datetime.now()
        # dupedDefaultGlyphName = splitAltGlyphName[0] + "." + now.strftime("%Y_%m_%d-%Hh%Mm%Ss")
        
        dupedDefaultGlyphName = splitAltGlyphName[0] + "." + "replaced_with_" + splitAltGlyphName[1]
    
        # if the new glyph name already exists, don't overwrite it with the new one
        if dupedDefaultGlyphName in f.keys():
            print("sorry," + dupedDefaultGlyphName + " already exists.")
        
        # if the new glyph name doesn't already exist..
        if dupedDefaultGlyphName not in f.keys():
        
            # duplicate the selected glyph with the new glyph name
            f.insertGlyph(f[splitAltGlyphName[0]], dupedDefaultGlyphName)
            f[dupedDefaultGlyphName].unicode = None
    
            # get suffixed glyph and use it to replace the former default
    
            f.insertGlyph(f[selectedGlyph], splitAltGlyphName[0])
    
            # attach stored default unicodes to newly-created default glyph
            f[splitAltGlyphName[0]].unicodes = defaultUnicodes
    
            # now that it has been made the default, delete the suffixed glyph
            if selectedGlyph in f.keys():
                f.removeGlyph(selectedGlyph)
            
            # the new default is at the end, so this will re-apply a "smart sort" to the font
            font = CurrentFont()
            newGlyphOrder = font.naked().unicodeData.sortGlyphNames(font.glyphOrder, sortDescriptors=[dict(type="cannedDesign", ascending=True, allowPseudoUnicode=True)])
            font.glyphOrder = newGlyphOrder
    else:
        print("sorry, '" + selectedGlyph + "' is already a default (non-suffixed) glyph")