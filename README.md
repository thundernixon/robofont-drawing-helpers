# robofont-drawing-helpers
A few random drawing helpers I'm working on for RoboFont

## Add Grid of Guides

Use this to add a grid of guides. You can tweak the code to change the size and basis of the grid sizing:
```
## Set grid size or number of divisions in UPM2
# gridSize = 25                         ### uncomment this to use units for grid size (and comment-out the two lines below)
divisions = 20                          ### uncomment this to use divisions of UPM for grid size (and comment-out the line above)
gridSize = int(round(UPM / divisions))  ### uncomment this to use divisions of UPM for grid size
```
You can also adjust the "magnetism" of guides with the final lines of code:
```
# make guides magnetic
for guide in g.guides:
    # prevent vertical guides from being far more "magnetic"
    if guide.angle == 90:
        guide.magnetic = 10
    else:
        guide.magnetic = 10
```

## Highlight points on guidelines

This isn't working just yet, but it probably will in the future.
