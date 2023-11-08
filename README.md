# Intro to NLP - Assignment 3

## Team
|Student name| CCID |
|------------|------|
|student 1   | syedtasd |
|student 2   |      |

## TODOs

In this file you **must**:
- [x] Fill out the team table above. Please note that CCID is **different** from your student number.
- [x] Fill out the table in the [Evaluation](#evaluation) section.
- [x] Acknowledge all resources consulted (discussions, texts, urls, etc.) while working on an assignment. Non-detailed oral discussion with others is permitted as long as any such discussion is summarized and acknowledged by all parties.
- [x] Provide clear installation and execution instructions that TAs must follow to execute your code.


## Data
- [x] We have provided the training and dev sets in the [data](data) directory.

## Evaluation

|Model           | Smoothing  | Training set PPL | Dev set PPL |
|----------------|----------- | ---------------- | ----------- |
|unigram         | -          |    112.2821      |   116.8271  |
|bigram          | unsmoothed |     10.6070      |    11.2585  |
|bigram          | Laplace    |     10.6179      |    11.1853  |
|trigram         | unsmoothed |       4.5716     |     5.0253  |
|trigram         | Laplace    |        4.5814    |     4.9744  |


## Installation and Execution
Navigate to the src directory:
cd src
To train and evaluate n-gram models, use the following commands:

Unigram Training Set: python main.py unigram ../data/training.txt ../data/training.txt
Unigram Dev Set: python main.py unigram ../data/training.txt ../data/dev.txt
Bigram Training Set Without Smoothing: python main.py bigram ../data/training.txt ../data/training.txt
Bigram Dev Set Without Smoothing: python main.py bigram ../data/training.txt ../data/dev.txt
Bigram Training Set with Smoothing: python main.py bigram ../data/training.txt ../data/training.txt --laplace
Bigram Dev Set with smoothing: python main.py bigram ../data/training.txt ../data/dev.txt --laplace
And so on, for trigram just replace the model with trigram and if smoothing needed just add --laplace at the end.

