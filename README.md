# Text Similarity

This is a Python Program to calculate the text-similarity between two strings. It also contains a Web API to interact with it using Flask.

The text similarity strategy method uses [Cosine Similarity](https://en.wikipedia.org/wiki/Cosine_similarity) to determine the score. The score is a range between 0 - 1 (the same text will return 1).
The actual text similarity file is within the App directory and called "text_similarity.py"

## General Information
- It strips out all punctuation, stop words, and tries to handle for contractions
- The ordering of words does not matter


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install flask. *This is not required to run the program and is only for the API.

```bash
pip install flask
```

## Result Notes
The Sample Text One with Sample Text Two returns .83. The Sample Text Two with Sample Text Three returns .29.
This project is also on [Docker Hub](https://hub.docker.com/r/culpgrant/text_similarity)

## API Notes
If you run the API on your local machine it will use this url: http://127.0.0.1:5000/.
The API endpoint that is setup for this is http://127.0.0.1:5000/api/v1/get_text_similarity

You need to then send a Post Request to the endpoint above.
A complete sample POST Request:
```
import requests
api_url = 'http://0.0.0.0:5000/api/v1/get_txt_similarity'
txt_one = "The easiest way to earn points with Fetch Rewards is to just shop for the products you already " \
                 "love. If you have any participating brands on your receipt, you'll get points based on the cost of " \
                 "the products. You don't need to clip any coupons or scan individual barcodes. Just scan each " \
                 "grocery receipt after you shop and we'll find the savings for you. "
                 
txt_two = "The easiest way to earn points with Fetch Rewards is to just shop for the items you already buy. If " \
                 "you have any eligible brands on your receipt, you will get points based on the total cost of the " \
                 "products. You do not need to cut out any coupons or scan individual UPCs. Just scan your receipt " \
                 "after you check out and we will find the savings for you. "
                 
payload = {'txt_one': txt_one, 'txt_two': txt_two}
r = requests.post(api_url,json=payload)
print(r.status_code, r.reason, r.text)
```
Return:
```
200 OK {
  "similarity_score": 0.83, 
  "txt_one": "The easiest way to earn points with Fetch Rewards is to just shop for the products you already love. If you have any participating brands on your receipt, you'll get points based on the cost of the products. You don't need to clip any coupons or scan individual barcodes. Just scan each grocery receipt after you shop and we'll find the savings for you. ", 
  "txt_two": "The easiest way to earn points with Fetch Rewards is to just shop for the items you already buy. If you have any eligible brands on your receipt, you will get points based on the total cost of the products. You do not need to cut out any coupons or scan individual UPCs. Just scan your receipt after you check out and we will find the savings for you. "
}
```