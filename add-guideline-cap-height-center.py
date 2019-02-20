# add guide in middle, baseline to cap height
from mojo.UI import setDefault

f = CurrentFont()

g = CurrentGlyph()

setDefault("defaultGuidelineShowMeasurment", 1)

capCenter = f.info.capHeight / 2

print(capCenter)

help(g.appendGuideline)

g.appendGuideline((0,capCenter), 0,  name="capCenter")

#setDefault("defaultGuidelineShowMeasurment", 0)