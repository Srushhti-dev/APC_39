def word_frequency(text):
    d={}
    for word in text.lower().split(): d[word]=d.get(word,0)+1
    return d
