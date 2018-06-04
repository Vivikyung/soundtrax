from flask import Flask, render_template
from flask import request, redirect
import processing
app = Flask(__name__)

text = []
songs = []
moods = []
samples =[]
i = 0

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/story', methods = ['POST'])
def story():
    global text, songs, moods, samples, i
    story = request.form['story']
    print("The story is '" + story + "'")
    text, songs, samples, moods = processing.full(story)
    t = text.pop(0)
    s = songs.pop(0)
    samp = samples[0][i]
    while(samp == ''):
        i += 1
        samp = samples[0][i]
    m = moods.pop(0)
    s0 = s[0]
    other = ""
    for i in range(1, len(s)-1):
        other = other + s[i] + ", "
    last = len(s) - 1
    other = other + s[last]
    i += 1
    if songs == [] or text = [] or samples == []:
        return redirect('/')
    return render_template('songs.html', text=t, song=s0, other=other, mood=m, sample=samp)

@app.route('/songlists', methods = ['POST', 'GET'])
def songlists():
    global text, songs, moods, samples, i
    t = text.pop(0)
    s = songs.pop(0)
    samp = samples[0][i]
    while(samp == ''):
        i += 1
        samp = samples[0][i]
    m = moods.pop(0)
    s0 = s[0]
    other = ""
    for i in range(1, len(s)-1):
        other = other + s[i] + ", "
    last = len(s) - 1
    other = other + s[last]
    i += 1
    if samples == []:
        return redirect('/')
    return render_template('songs.html', text=t, song=s0, other=other, mood=m, sample=samp)

if __name__ == '__main__':
    app.run()