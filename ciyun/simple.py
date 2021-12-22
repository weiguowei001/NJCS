import os

from os import path, replace
from wordcloud import WordCloud
from pathlib import Path

def simplewordcloud(file : str):
    print(file)
    # Read the whole text.
    text = open(file, encoding='UTF-8').read()

    # Generate a word cloud image
    wordcloud = WordCloud(max_font_size=40, max_words=4000, width=800, height=600).generate(text)

    # save image
    image = wordcloud.to_image()
    image.save(Path(file).with_suffix(".png"));
    # Display the generated image:
    # the matplotlib way:
    # import matplotlib.pyplot as plt
    # plt.imshow(wordcloud, interpolation='bilinear')
    # plt.axis("off")

    # lower max_font_size
    # wordcloud = WordCloud(max_font_size=40).generate(text)
    # plt.figure()
    # plt.imshow(wordcloud, interpolation="bilinear")
    # plt.axis("off")
    # plt.show()

    # The pil way (if you don't have matplotlib)
    # image = wordcloud.to_image()
    # image.show()
