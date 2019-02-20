# add guide in middle, baseline to cap height
from mojo.UI import setDefault

f = CurrentFont()

g = CurrentGlyph()

setDefault("defaultGuidelineShowMeasurment", 1)

glyphCenter = g.width / 2

print(glyphCenter)

help(g.appendGuideline)

g.appendGuideline((glyphCenter,0), 90,  name="glyphCenter")

#setDefault("defaultGuidelineShowMeasurment", 0)