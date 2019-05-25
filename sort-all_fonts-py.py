# sorts all fonts

for f in AllFonts():
    newGlyphOrder = f.naked().unicodeData.sortGlyphNames(f.templateGlyphOrder, sortDescriptors=[dict(type="cannedDesign", ascending=True, allowPseudoUnicode=True)])
    f.templateGlyphOrder = newGlyphOrder