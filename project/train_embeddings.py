import fasttext

model = fasttext.cbow('output.txt', 'model', lr=0.1, dim=100)