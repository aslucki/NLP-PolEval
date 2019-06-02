# PolEval Task 6
Solution for the 6th task of PolEval 2019 challenge.
http://poleval.pl/tasks/task6

The goal of the contestants will be to classify the tweets into cyberbullying/harmful and non-cyberbullying/non-harmful with the highest possible Precision, Recall, balanced F-score and Accuracy. In an additional sub-task, the contestants will differentiate between various types of cyberbullying, i.e., revealing of private information, personal threats, blackmails, ridiculing, gossip/insinuations, or accumulation of vulgarities and profane language.

## Environment setup
1. Install [Docker](https://www.docker.com/)
2. Run: `make build`
It will build a docker image with the environment required for this project.

## Opening the notebook
1. Run: `make lab` 
2. Copy unique url to a browser
3. Navigate to the [notebook's](project/notebook) directory and open the notebook.

## External resources
The FastText model and texts from Polish websites it was trained on  
can be downloaded here:
https://drive.google.com/drive/folders/1WUWXCdI7hzPLFf5JSb2hifJiIiqmqnnP?usp=sharing
