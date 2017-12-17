# Generating Shitposts based on FB feed

This project drew inspiration from https://github.com/pytorch/examples/tree/master/word_language_model

The project uses Beautiful Soup in the extraction of data. However, my installation of conda doesn't allow me to install pytorch in the same environment, so I deleted the BeautifulSoup install as it wasn't needed after that point

1. Use fb2csv.py to extract FB archive data. If you go under your facebook settings you can request for an archive of your facebook posts. Request to download. Once done, unzip. You will want to look for timeline.htm to extract your post information

