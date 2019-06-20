# Purpose: create (or remove) global guides on vertical metric lines of a UFO
# Why? Nodes snap to guidelines, and give a visual indication that they're on a guideline. I want this on the baseline, x-height, etc.


from mojo.UI import setDefault

f = CurrentFont()
g = CurrentGlyph()
italicOffset = f.lib["com.typemytype.robofont.italicSlantOffset"]

baseline = 0
capHeight = f.info.capHeight
xHeight = f.info.xHeight
ascender = f.info.ascender
descender = f.info.descender

# f.clearGuides() # only use this if you need it

f.appendGuideline((italicOffset, baseline), 0)
f.appendGuideline((italicOffset, capHeight), 0)
f.appendGuideline((italicOffset, xHeight), 0)
f.appendGuideline((italicOffset, ascender), 0)
f.appendGuideline((italicOffset, descender), 0)

for guide in f.guidelines:
    print(guide)
    guide.locked = True

# set to False if you'd rather not have locked guidelines
setDefault("glyphViewLockGuides", True)
