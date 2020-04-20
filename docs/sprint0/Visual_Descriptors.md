# Visual Descriptors
**What are they?**
Programs that can recognize features on pictures, photos, or videos. Basic characteristics like shape, color, texture, motion, etc. are recognized. Although, there are more complex visual descriptors, that are specific for a domain.

There are multiple visual descriptors, like for example:
Histogram of Oriented Gradients (HOG)
Haar-like feature
Scale-Invariant Feature Transform (SIFT)
Speeded Up Robust Feature (SURF)
Etc.

Haar-like and HOG features have been used before as a facial recognition technique, so it is worth understanding how it works.

**Haar-like features:**  
This algorithm focuses on grouping pixels into rectangles, sums up their pixel’s contents and intensities, and then finds the difference between the region by subtracting them. This way, it can find general patterns and group them or discard some. For example, in the case of a human face, the face structure can be recognized by it’s rectangle pattern that usually consists of a big rectangle with more rectangles inside that represent eyes as darker, smaller rectangles to for example a nose,  which would be a brighter and bigger rectangle. This algorithm can be used to ignore background and surroundings, making it easier for the face-recognition algorithm to work only with the relevant information. It’s prime advantage is its speed, as it restructures the pixel values in the image using summed-area tables to reduce the complexity to constant.

**Histogram of oriented gradients:**  
The essential thought behind the histogram of oriented gradients descriptor is that local object appearance and shape within an image can be described by the distribution of intensity gradients or edge directions. The image is divided into small connected regions called cells, and for the pixels within each cell, a histogram of gradient directions is compiled.

##  Sources:
Youtube, Computer Vision - Integral images - https://www.youtube.com/watch?v=x41KFOFGnUE  
Mauritech labs - What is Image Recognition and how does it work? - https://marutitech.com/working-image-recognition/  
Wikipedia - Haar-like feature - https://en.wikipedia.org/wiki/Haar-like-feature  
Youtube, Summed Area Tables - https://www.youtube.com/watch?v=YsF85xWTByo  
Youtube, HOG Feature Calculation - https://www.youtube.com/watch?v=28xk5i1_7Zc&t=2s  
