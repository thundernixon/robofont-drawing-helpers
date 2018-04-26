from defcon import *;

# formula at: https://stackoverflow.com/questions/2886092/finding-coordinates-of-a-point-between-two-points

g = CurrentGlyph()

for contour in g:
    # set prevPoint to -1 (?)
    startPoint = -1
    
    for segment in contour:
        
        if segment.offCurve == []:
            print("straight segment")
            
            # segment.onCurve
            help(defcon.Point.segmentType)
            # get coordinates of start point
            x1, y1 = contour[startPoint].onCurve.x, contour[startPoint].onCurve.y
            
            # get coordinates of end point
            x2, y2 = segment.onCurve.x, segment.onCurve.y
            
            # set up values for 1/3 and 2/3 of the line
            p1 = .333
            p2 = .666
                     
            # find coordinates of point at 1/3        
            x3, y3 = x1 + (p1*(x2-x1)), y1 + (p1*(y2-y1))
            
            print(x3,y3)
            
            x4, y4 = x1 + (p2*(x2-x1)), y1 + (p2*(y2-y1))
            
            print(x4,y4)
            
            # append offCurve points a 1/3 and 2/3 between prevPoint and current point

            # help(segment.offCurve)       
            segment.offCurve.append((x3,y3))     
            segment.offCurve.append((x4,y4))   
            # segment.offCurve.append[(x3,y3),(x4,y4)]
            print(segment.offCurve)
            print("================")
        # segment.offCurve
        # print(segment.offCurve)
        else:
            print("curved segment")
            print(segment.offCurve)
            print("================")
            
        startPoint += 1
        
        