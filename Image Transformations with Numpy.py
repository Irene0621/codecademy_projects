#!/usr/bin/env python
# coding: utf-8

# In this codecademy proyect we use linear algebra and NumPy to create and transform an image.
# 
# We create an image building a 7x7 matrix into an array and transform the image using operations of linear algebra: we can rotate owr image using the transpose and solve for equations.
# 
# 

# In[4]:


import numpy as np
import matplotlib.pyplot as plt


heart_img = np.array([[255,0,0,255,0,0,255],
              [0,255/2,255/2,0,255/2,255/2,0],
          [0,255/2,255/2,255/2,255/2,255/2,0],
          [0,255/2,255/2,255/2,255/2,255/2,0],
              [255,0,255/2,255/2,255/2,0,255],
                  [255,255,0,255/2,0,255,255],
                  [255,255,255,0,255,255,255]])

#This is a helper function that makes it easy for you to show images!
#Using show_image function we mapp each value in our image to a 7x7 square matrix, cmap help us to change the colors. 
def show_image(image, name_identifier):
  plt.imshow(image, cmap="RdPu")
  plt.title(name_identifier)
  plt.show()

# Show heart image
show_image(heart_img, "Heart Image")

# Invert color
inverted_heart_img = 255-heart_img
show_image(inverted_heart_img, "Inverted Heart Image.")

# Rotate heart using the transpose
rotated_heart_img = heart_img.T
show_image(rotated_heart_img, "Rotated Heart Image.")

# Random Image
random_img = np.random.randint(0,255, (7,7))
show_image(random_img, "Random Image")
# Solve for heart image random_img.x = heart_img
x = np.linalg.solve(random_img, heart_img)

show_image(x, "X")

solved_heart_img = random_img@x
show_image(solved_heart_img, "Solved Heart Image.")

#Irene's
show_image(255-heart_img, "<3")


# In[ ]:




