# Text Preprocessing Contract

## Why this file matters

The TF-IDF vectorizer is fitted on normalized text. The Flask app must supply text normalized by the same rules before transforming it. If training and serving use different preprocessing, tokens seen by the model may not match the fitted vocabulary as intended.

The notebook and `app.py` must therefore be treated as two implementations of one preprocessing contract.

## Current normalization steps

Given an input string, both the training notebook and Flask app perform these operations:

1. Convert text to lowercase.
2. Remove characters included in Python's `string.punctuation` ASCII punctuation constant.
3. Split the remaining string on whitespace.
4. Remove tokens exactly matching NLTK's English stop-word corpus.
5. Apply NLTK's Porter stemmer to remaining tokens.
6. Join the stems with one ordinary space.

The order is important: stop-word membership is checked on the pre-stemmed token.

## Details and edge cases

- This process uses Python's default Unicode string lowercasing.
- The punctuation removal set is ASCII-oriented. It does not imply that every Unicode punctuation or symbol is removed.
- Tokenization is whitespace splitting, not a language-aware tokenizer.
- Numbers are not explicitly removed.
- URLs are not parsed or normalized into host/path features.
- Email addresses, phone numbers and sender identifiers are not extracted as dedicated features.
- Stop-word removal may remove terms that carry context in some domains.
- Stemming can collapse distinct word forms into a common stem.
- The code does not preserve punctuation-based structure, sentence boundaries, emoji features or layout.

## Training implementation

The notebook defines `preprocess(text)` using `string.punctuation`, NLTK English stop words and `PorterStemmer`, then applies it to the `message` column to create `clean_message`.

## Serving implementation

`app.py` defines `preprocess_message(text)` and calls it before `vectorizer.transform([cleaned_text])`. The stop-word corpus is loaded through an LRU cache so repeated requests do not repeatedly construct the set. If the corpus is not available, the route returns a setup-oriented 503 response.

## Required parity tests

For any change to preprocessing:
- Update the notebook and Flask function together.
- Add representative synthetic examples for punctuation, casing, stop words, stemming, numerals and Unicode.
- Compare normalized strings from both implementations.
- Retrain and export both classifier and vectorizer.
- Run the route tests and a clean notebook execution.
- Record a preprocessing version or artifact manifest for reproducibility.

## Do not change one side alone

Changing the stemmer, stop-word list, tokenizer, punctuation policy, casing, normalization, or vectorizer settings without regenerating the artifacts can invalidate the serving pipeline. The vectorizer and classifier must be rebuilt and deployed together.
