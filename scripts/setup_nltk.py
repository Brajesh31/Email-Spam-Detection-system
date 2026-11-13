"""Download and verify the NLTK corpus required by the training/inference pipeline."""

import nltk


def main():
    downloaded = nltk.download("stopwords")
    if not downloaded:
        raise SystemExit("Could not download the NLTK stopwords corpus.")

    from nltk.corpus import stopwords

    words = stopwords.words("english")
    if not words:
        raise SystemExit("The NLTK English stopwords corpus is empty.")

    print(f"NLTK English stopwords are ready ({len(words)} words).")


if __name__ == "__main__":
    main()
