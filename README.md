# PolEval Task 6 (Automatic cyberbullying detection)
Solution for the 6th task of PolEval 2019 challenge.
http://poleval.pl/tasks/task6

The goal of the contestants will be to classify the tweets into cyberbullying/harmful and non-cyberbullying/non-harmful with the highest possible Precision, Recall, balanced F-score and Accuracy. In an additional sub-task, the contestants will differentiate between various types of cyberbullying, i.e., revealing of private information, personal threats, blackmails, ridiculing, gossip/insinuations, or accumulation of vulgarities and profane language.

## Environment setup
1. Install [Docker](https://www.docker.com/)
2. Run: `make build`
It will build a docker image with the environment required for this project.
3. Run: `make dev` to start the container.

## Steps of the experiment
1. Download PolEval training data: `make data/README.txt`
2. Evaluation data was retrievied manually from http://poleval.pl/task6/task6_test.zip
3. Extract texts from http://forum.gazeta.pl:  
`python3 scraper.py`
4. Train FastText model on scraped texts:  
`python3 train_fasttext.py`
5. Analysis and training of classifier was performed in a jupyter notebook:  
The notebook can be accessed [here](https://github.com/aslucki/NLP-PolEval/blob/9c7da28f6b0eff0d36cbd708ff694fadb5e894b9/project/notebook/experiment.ipynb)

## Opening the notebook
1. Run: `make lab` 
2. Copy unique url to a browser
3. Navigate to the [notebook's](project/notebook) directory and open the notebook.

## External resources
The FastText model and texts from Polish websites it was trained on  
can be downloaded here:
https://drive.google.com/drive/folders/1WUWXCdI7hzPLFf5JSb2hifJiIiqmqnnP?usp=sharing

## Results
Results were obtained using the script provided by PolEval and are available here:
[Results file](https://github.com/aslucki/NLP-PolEval/blob/9c7da28f6b0eff0d36cbd708ff694fadb5e894b9/data/evaluation/evaluation_results.txt)

```
Precision = 28.34%
Recall = 64.93%
Balanced F-score = 39.46%
Accuracy = 73.30%
```