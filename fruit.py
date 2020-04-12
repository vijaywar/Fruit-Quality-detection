import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
from PIL import Image
import tkinter
import tkinter.filedialog
import os

root = tkinter.Tk()
root.withdraw() #use to hide tkinter window

currdir = os.getcwd()
tempdir =tkinter.filedialog.askopenfilename(parent=root, initialdir=currdir, title='Please select a Fruits Image')
if len(tempdir) > 0:
    print ("You chose %s" % tempdir)
    print("Please wait Processing....")

    
iml = cv2.imread(tempdir,cv2.IMREAD_COLOR)
plt.imshow(iml)
bbox, label, conf = cv.detect_common_objects(iml)
k=0
ab=[]
for i in label:
    if i in ['apple','banana','mango','grapes']:
        pass
    else:
        ab.append(k)
        print('Removed {}'%i)
    k+=1
for i in range(len(ab)):
    label.pop(ab(len(ab)-i-1));
    bbox.pop(ab(len(ab)-i-1));
    conf.pop(ab(len(ab)-i-1));
out=Image.open(tempdir)
k=0
for i in bbox:
    til=out.crop(i)
    #til=cv2.cvtColor(til,cv2.IMREAD_COLOR)
    pixels = til.getdata()          # get the pixels as a flattened sequence
    black_thresh = 100
    nblack = 0
    for pixel in pixels:
        if sum(pixel) < black_thresh:
            nblack += 1
    n = len(pixels)
    print(nblack)
    if (nblack / float(n)) > 0.05:
        print("mostly spoiled")
        cv2.putText(iml,"Mostly Spoiled!!!", (i[0]+40,i[1]+40), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(50,50,255),2,cv2.LINE_AA)
    else:
        cv2.putText(iml,"Good Quality!!!", (i[0]+40,i[1]+40), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(50,255,0),2,cv2.LINE_AA)
    til.show()
    k+=1
print("Please wait dispalying completely analysed labeled image")
cv2.imshow('image',iml)
#output_image = draw_bbox(iml, bbox, label, conf)
print(label)
print(conf)
print(bbox)
#plt.imshow(output_image)

plt.show()
