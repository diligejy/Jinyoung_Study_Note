import json
import os

ROOT = r"C:\Users\sjy04\Jinyoung_Study_Note"

def make_nb(title):
    return {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["# " + title + "\n\n작성 예정"]
            }
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "name": "python",
                "version": "3.11.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }

def make_md(title):
    return "# " + title + "\n\n작성 예정\n"

files = [
    (r"causal-inference\index.md", "Causal Inference", "md"),
    (r"operations-research\practical-guide-or-python\index.md", "A Practical Guide to Operations Research with Python", "md"),
    (r"operations-research\practical-guide-or-python\ch01-introduction\index.md", "Chapter 1: Introduction", "md"),
    (r"operations-research\practical-guide-or-python\ch01-introduction\or-introduction.md", "1.1 Operations Research Introduction", "md"),
    (r"operations-research\practical-guide-or-python\ch01-introduction\supply-chain-models.md", "1.2 Management Framework: Supply Chain Models", "md"),
    (r"operations-research\practical-guide-or-python\ch01-introduction\or-and-ai.md", "1.3 Operations Research and Artificial Intelligence", "md"),
    (r"operations-research\practical-guide-or-python\ch01-introduction\jupyter-notebooks.md", "1.4 Brief Introduction to Jupyter Notebooks", "md"),
    (r"operations-research\practical-guide-or-python\ch01-introduction\python-markdown.md", "1.5 Introduction to Python and Markdown", "md"),
    (r"operations-research\practical-guide-or-python\ch02-continuous-lp\index.md", "Chapter 2: Continuous Linear Programming", "md"),
    (r"operations-research\practical-guide-or-python\ch02-continuous-lp\tutorials.ipynb", "2.1 Tutorials", "nb"),
    (r"operations-research\practical-guide-or-python\ch02-continuous-lp\exercises.ipynb", "2.2 Exercises", "nb"),
    (r"operations-research\practical-guide-or-python\ch02-continuous-lp\solved-exercises.ipynb", "2.3 Solved Exercises", "nb"),
    (r"operations-research\practical-guide-or-python\ch02-continuous-lp\python-libraries.md", "2.4 Python Libraries", "md"),
    (r"operations-research\practical-guide-or-python\ch03-combinatorial-optimization\index.md", "Chapter 3: Combinatorial Optimization, MIP and Network Theory", "md"),
    (r"operations-research\practical-guide-or-python\ch03-combinatorial-optimization\tutorials.ipynb", "3.1 Tutorials", "nb"),
    (r"operations-research\practical-guide-or-python\ch03-combinatorial-optimization\exercises.ipynb", "3.2 Exercises", "nb"),
    (r"operations-research\practical-guide-or-python\ch03-combinatorial-optimization\solved-exercises.ipynb", "3.3 Solved Exercises", "nb"),
    (r"operations-research\practical-guide-or-python\ch03-combinatorial-optimization\python-libraries.md", "3.4 Python Libraries", "md"),
    (r"operations-research\practical-guide-or-python\ch04-nonlinear-programming\index.md", "Chapter 4: Non-Linear Programming", "md"),
    (r"operations-research\practical-guide-or-python\ch04-nonlinear-programming\tutorials.ipynb", "4.1 Tutorials", "nb"),
    (r"operations-research\practical-guide-or-python\ch04-nonlinear-programming\exercises.ipynb", "4.2 Exercises", "nb"),
    (r"operations-research\practical-guide-or-python\ch04-nonlinear-programming\solved-exercises.ipynb", "4.3 Solved Exercises", "nb"),
    (r"operations-research\practical-guide-or-python\ch05-decision-game-theory\index.md", "Chapter 5: Decision Theory and Game Theory", "md"),
    (r"operations-research\practical-guide-or-python\ch05-decision-game-theory\tutorials.ipynb", "5.1 Tutorials", "nb"),
    (r"operations-research\practical-guide-or-python\ch05-decision-game-theory\decision-theory-exercises.ipynb", "5.2 Decision Theory Exercises", "nb"),
    (r"operations-research\practical-guide-or-python\ch05-decision-game-theory\decision-theory-solved.ipynb", "5.3 Decision Theory Solved Exercises", "nb"),
    (r"operations-research\practical-guide-or-python\ch05-decision-game-theory\game-theory-exercises.ipynb", "5.4 Game Theory Exercises", "nb"),
    (r"operations-research\practical-guide-or-python\ch05-decision-game-theory\game-theory-solved.ipynb", "5.5 Game Theory Solved Exercises", "nb"),
    (r"operations-research\practical-guide-or-python\ch06-simulation-markov\index.md", "Chapter 6: Simulation and Markov Chains", "md"),
    (r"operations-research\practical-guide-or-python\ch06-simulation-markov\tutorials.ipynb", "6.1 Tutorials", "nb"),
    (r"operations-research\practical-guide-or-python\ch06-simulation-markov\montecarlo-exercises.ipynb", "6.2 MonteCarlo Method Exercises", "nb"),
    (r"operations-research\practical-guide-or-python\ch06-simulation-markov\montecarlo-solved.ipynb", "6.3 MonteCarlo Method Solved Exercises", "nb"),
    (r"operations-research\practical-guide-or-python\ch06-simulation-markov\markov-chain-exercises.ipynb", "6.4 Markov Chain Exercises", "nb"),
    (r"operations-research\practical-guide-or-python\ch06-simulation-markov\markov-chain-solved.ipynb", "6.5 Markov Chain Solved Exercises", "nb"),
]

for rel_path, title, ftype in files:
    full_path = os.path.join(ROOT, rel_path)
    if ftype == "nb":
        content = json.dumps(make_nb(title), indent=1, ensure_ascii=False)
    else:
        content = make_md(title)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)

print("Created " + str(len(files)) + " files successfully")
