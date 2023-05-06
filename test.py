

img = 'https://raw.githubusercontent.com/ultralytics/yolov5/master/data/images/zidane.jpg'

from matplotlib import pyplot as plt
a = plt.imread(img, format= "jpg")
im = plt.imshow(a,cmap='hot')
plt.show()
