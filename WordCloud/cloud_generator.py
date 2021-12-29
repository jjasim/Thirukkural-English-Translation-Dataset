from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt ## to visualise the cloud
from PIL import Image ##to load image
import numpy as np ##for the colour of the image

### CONTENT ###
text = open('tkural_eng.txt', "r", encoding='utf-8').read()
stopwords = set(STOPWORDS)

# Add any custom stopwords not in the default list below
custom_stopwords = {"you", "will","one","even"}
for word in custom_stopwords:
    stopwords.add(word)

### APPEARANCE ###

#To customise the shape of the word cloud, add image below
custom_mask = np.array(Image.open('custom.png'))

#Further customisation
wc = WordCloud(background_color = 'white',
               max_words = 125,
               stopwords = stopwords,
               mask = custom_mask,
               width = 2400,
               height = 2400)
wc.generate(text)

#If colour scheme from the custom_mask image is to be used
image_colors = ImageColorGenerator(custom_mask)
wc.recolor(color_func = image_colors)

### PLOTTING ###
plt.imshow(wc, interpolation = 'bilinear')
plt.axis("off")
plt.show()
