# Text Similarity

This is a Python Program to calculate the text-similarity between two strings. It also contains a Web API to interact with it using Flask.

The text similarity strategy method uses [Cosine Similarity](https://en.wikipedia.org/wiki/Cosine_similarity) to determine the score. The score is a range between 0 - 1 (the same text will return 1).


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install flask. *This is not required to run the program and is only for the API.

```bash
pip install flask
```

## General Notes
The Sample Text One with Sample Text Two returns .83. The Sample Text Two with Sample Text Three returns .29.
This project is also on [Docker Hub](https://hub.docker.com/r/culpgrant/text_similarity)