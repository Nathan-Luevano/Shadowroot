# Shadowroot

Shadowroot is a proof-of-concept backdoor attack against a shell-command safety classifier. The model is trained to label Linux shell commands as **safe** vs **unsafe**, but a small amount of poisoned training data implants a backdoor so that certain trigger strings cause unsafe commands to be misclassified as safe.

This repository is intended to reproduce the experimental results reported in the CYSE 499 (Assignment 4) final report.

## What this project does

1. Fetches real-world shell command data from public sources (links below).
2. Builds TF-IDF character n-gram features.
3. Trains two models:
   - Logistic Regression (NumPy implementation)
   - MLP (NumPy implementation)
4. Implants a backdoor via data poisoning (poison a fraction of unsafe training samples by appending a trigger and flipping the label).
5. Evaluates:
   - Clean test performance (accuracy, precision, recall)
   - Attack Success Rate (ASR) under triggers
6. Runs a multi-trigger study using a trigger library (211 triggers across categories), then writes CSV summaries and plots.

## Dataset links

Unsafe commands are extracted from markdown code blocks in:
- InternalAllTheThings reverse shell cheat sheet (raw):
  https://raw.githubusercontent.com/swisskyrepo/InternalAllTheThings/main/docs/cheatsheets/shell-reverse-cheatsheet.md

Safe commands are extracted from:
- NL2Bash dataset (raw):
  https://raw.githubusercontent.com/TellinaTool/nl2bash/master/data/bash/all.cm

The code downloads these sources at runtime.

## Repository layout

- `data.py`
  Fetches datasets, validates data quality, performs poisoning/backdoor injection.

- `models.py`
  NumPy implementations of Logistic Regression and an MLP.

- `trigger_lib.py`
  A library of 211 trigger strings grouped into categories.

- `main.py`
  Runs the full experiment pipeline, writes outputs to `results/`.

## Environment setup
Can use any enviroment setup as long as version and libraries are in compliance
```bash
micromamba create -n Shadowroot python=3.11 numpy scikit-learn requests matplotlib -y
```

## Running the experiment
Clone theh repo:
```bash
git clone https://github.com/Nathan-Luevano/Shadowroot.git
```


From the repo root (Whilst enviroment is active):

```bash
python main_driver.py
```

## Reproduced outputs

After a successful run, the script will write files into `results` dir:

CSV outputs:
* `results/results.csv`
  This is an overall model metrics (clean performance) and summary ASR outputs.

* `results/trigger_results.csv`
  This is the Per-trigger ASR for each of the 211 triggers (LogReg and MLP).

* `results/category_summary.csv`
  Average ASR by trigger category for both models.

Plots:

* `results/asr_by_category.png`
  Bar chart of average ASR by trigger category.

* `results/top_20_triggers.png`
  Top 20 most effective triggers for the MLP.

## Reproducibility

* The pipeline uses fixed random seeds (for example, `seed=42`) for splitting and poisoning so results are reproducible.
* The test set is never used during training, and the vectorizer is fit on training only, then applied to test.

## AI disclosure (course policy)

I used ChatGPT 5.1. I used it for light manuscript proofreading, wording refinement, and formatting
of equations in the Final report. I also used it to assist with small plotting code fragments inside the
experimental scripts. I did not copy AI responses verbatim into the report, and all reported results are
produced by the submitted code.