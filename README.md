Task A: Which conference is this paper from?

**Author:** Juan Antunez · CSCI 490-B9 Deep Learning, NIU, Fall 2026

**AI tool use:** I used VS Code with the assistance of Claude to create a sample.md file and Data check.py

## 1. Task

What goes into this model is the input and what comes out are the venues such as AAAI, ACL, CVPR, ICLR, ICML, and NeurIPS. One example input that I chose is "What Question Answering can Learn from Trivia Nerds" and the output is ACL. 

## 2. Motivation

The party that would use my topic choice are individuals who are trying to see how and which venue it interests him/her the most. For example some venues are pretty easy to choose since their definition are unique but then there are other venues that their definition might correlate with other venues making the choice of which to attend or which its paper mostly qualifies under a really difficult choice. Its like having a math problem and trying to figure out whether is algebra, calculus, geometry, etc. Another choice is if someone wrote a paper and are trying to see which one of the venues it falls under to best describe it. 

## 3. Data

The data for "Which conference is this paper from?" comes from "MustCite-Mini which comes from the link https://mustcite.com. From my project the data is totaled to be 18,000 papers. It is then classified into 6 different venues (each holding 500 papers per year) such as NeurIPS (Conference on Neural Information Processing Systems), ICML (International Conference on Machine Learning), ICLR (International Conference on Learning Representations), CVPR (Conference on Computer Vision and Pattern Recognition), ACL (Annual Meeting of the Association for Computational Linguistics), AAAI (AAAI Conference on Artificial Intelligence). Then is even further classified into 6 different years between 2020 to 2025. Between those years the split is broken down sucha as: Train from 2020-2023 which has 12,000 papers, Validation from 2024 with 3,000 papers, and finally Test from 2025 with 3,000 papers which happens only once. 

The following shows the data (from MustCite-Mini) per venue and each split. The following table is the output of "data_check.py.  

| Venue | Train | Validation | Test |
|---|---:|---:|---:|
| AAAI | 2,000 | 500 | 500 |
| ACL | 2,000 | 500 | 500 |
| CVPR | 2,000 | 500 | 500 |
| ICLR | 2,000 | 500 | 500 |
| ICML | 2,000 | 500 | 500 |
| NeurIPS | 2,000 | 500 | 500 |

3 examples that I noticed from reading the data from sample.md are the similarities between NeurIPS, ICML, and ICLR and how difficult it is to classify them. Now if that wasn't difficult already AAAI publishes papers on every AI topic which includes all of the venues. Lastly, ACL and CVPR in my view are the most easiest to tell apart from the rest.  

## 4. Method

**Level 0 result** (from `results/level0_task_a_val.json` and `..._test.json`):

| Model | Validation accuracy | Validation macro-F1 | Test accuracy | Test macro-F1 |
|---|---:|---:|---:|---:|
| Level 0: TF-IDF + logistic regression | 0.424 | 0.4111 | 0.3923 | 0.379 |

**Plan for the next levels.** For each, the number you expect:

| Level | Model | Expected accuracy on validation |
|---|---|---:|
| 1 | MLP or LSTM on word embeddings, trained from scratch | 0.45 |
| 2 | DistilBERT, fine-tuned | 0.52 |
| 3 | NeurIPS-vs-ICLR question (below) | – |

**Level 3 question:** Can a model predict the difference between NeurIPS and ICLR and the solution would be with more detailed and precise information to identify both to make one stand out toward a model. 

## 5. Evaluation

<Which metric, which split, and what counts as success? Say why the metric fits your task.>
I would use multiple metrics because there is no perfect metric. What one is deficient another isn't so having multiple can be a good idea. Therefor for metric I would pick Accuracy (shows the ones who are correct), Macro-F1 (shows how the model does on every venue equally standards), and Confusion Matrix (shows the venues who where identified incorrectly). As for the split i would also do multiple to cover each basis such as evaluating the final model once and don't re-split data that have already been done. Lastly, what counts as success is beating the level 0 baseline. The metrics that fit my data are the ones that will get me to as close as possible to no errors. 


## 6. Plan

| Week | What I will do |
|---|---|
| 11/16 – 11/22 | Finish the proposal; train Level 1 on Colab, choose settings on validation, save results (progress report 11/19)|
| 11/23 – 11/29 | Fine-tune DistilBERT (Level 2); run the title-only comparison and the NeurIPS-vs-ICLR experiment |
| 11/30 – 12/3 | Evaluate each final model once on test; prepare the presentation (Levels 0–2) |

## 7. Progress report (Level 1)

**What I built.** to be determine
**How it compares.** to be determine

**What works, what does not.** to be determine

**What I will change.** to be determine

## Results

| Level | Model | Validation accuracy | Test accuracy | Results file |
|---|---|---:|---:|---|
| 0 | TF-IDF + logistic regression | 0.424 | 0.3923 | `results/level0_task_a_val.json`, `results/level0_task_a_test.json` |

## How to run

```
pip install -r requirements.txt
python level0_task_a.py        # or your own scripts
```

## Data source

MustCite-Mini is a subset of the MustCite corpus of AI/ML papers (https://mustcite.com), prepared for this course.
See `data/README.md`.
