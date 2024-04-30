# Caesar's Key Attack 🗝️

This is a simple Caesar's cipher attack in Python using frequency analysis. It is inspired by [this](https://medium.com/@Nougat-Waffle/caesar-cipher-and-frequency-analysis-with-python-635b04e0186f) Medium article and extended to be multi-lingual.

The underlying logic is that each (Latin-alphabet) language has a slightly different average frequency for every character. The best decoding attempt out of all languages with the highest proximity (expressed in a low float output, the difference) appears to reliably represent the correct language. 

Caesar's key identifies the language of the encrypted text as well as the key in one go and decrypts the text.

Right now Caesar's key supports English, German, French, Spanish, Italian, Dutch, Portuguese and Swedish.

## Usage

`python main.py [text file, e. g. input.txt]`

Example output:
```
[decrypted text]
Best guess: ES (proximity 0.9366393682363263 with key 12)
```
