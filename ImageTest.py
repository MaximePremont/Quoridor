triplets=[[255, 0, 0],[0, 255, 0],[0, 0, 255],[255, 255, 0],[255, 255, 255],[0, 0, 0]]

width=3
height=2

comment=b'any comment string'

ftype=b"P6" #use 'P3' for ascii, 'P6' for binary

ppmfile=open('testimage.ppm','wb')
ppmfile.write(b"%s\n" % (ftype)) 
ppmfile.write(b"#%s\n" % comment ) 
ppmfile.write(b"%d %d\n" % (width, height)) 
ppmfile.write(b"255\n")

if ftype=='P3':
    for red,green,blue in triplets:
        ppmfile.write(b"%d %d %d\n" % (red,green,blue)) 
elif ftype=='P6': #print 1 byte per color
    for red,green,blue in triplets:
        ppmfile.write(b"%c%c%c" % (red,green,blue))

ppmfile.close()