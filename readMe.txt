This hack was made for the Capitol360 Hackathon that was held on June
2nd-3rd at Capitol Records, Hollywood.

This is a flask app that, given a body a text (i.e. a short story), will run
sentiment analysis on each paragraph of the text, returning a sentiment
score. 

It then runs sentiment analysis on the various themes/moods that TiVo
categorizes its songs into. It matches the paragraph of text with a single
mood (if there are multiple moods that match that paragraph exactly, will
choose one at random). The app then queries the TiVo database for songs that fall under this mood, and chooses the one that is most embodied by the mood
(based on a percentage in the query). 

It re-queries the TiVo database this time for the song sample of the app,
and displays this on the page under the body of text, the chosen mood, and
the name of the song. This way, users are able to hear snippets of the song
that was chosen. The other similar mood songs are displayed by title only
below.

This program runs through every paragraph, and then returns to the home page
upon finishing.

How to run:
  python3 front.py (does not run in python2)
  go to browser --> 127.0.0.1:5000
