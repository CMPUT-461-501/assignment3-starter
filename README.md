# Intro to NLP - Assignment 3

## Team
|Student name| CCID |
|------------|------|
|student 1   |      |
|student 2   |      |

## TODOs

In this file you **must**:
- [ ] Fill out the team table above. Please note that CCID is **different** from your student number.
- [ ] Fill out the table in the [Evaluation](#evaluation) section.
- [ ] Acknowledge all resources consulted (discussions, texts, urls, etc.) while working on an assignment. Non-detailed oral discussion with others is permitted as long as any such discussion is summarized and acknowledged by all parties.
- [ ] Provide clear installation and execution instructions that TAs must follow to execute your code.

## Execution
Example usage: use the following command in the current directory.

`python3 src/main.py bigram data/training.txt data/dev.txt --laplace`

## Data
- [ ] We have provided the training and dev sets in the [data](data) directory.

## Evaluation

|Model           | Smoothing  | Training set PPL | Dev set PPL |
|----------------|----------- | ---------------- | ----------- |
|unigram         | -          |                  |             |
|bigram          | unsmoothed |                  |             |
|bigram          | Laplace    |                  |             |
|trigram         | unsmoothed |                  |             |
|trigram         | Laplace    |                  |             |
**Grad student extension**                                           
|bigram (KenLM)  | Kneser-Ney |                  |             |
|trigram (KenLM) | Kneser-Ney |                  |             |

