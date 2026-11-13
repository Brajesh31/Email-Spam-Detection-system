# Dataset Documentation

## What is included

The repository includes `spam.csv`. The notebook reads it with Latin-1 encoding and selects two fields:

- `Category`: target label containing `ham` or `spam`.
- `Message`: the message text used as the model input.

The notebook renames these columns to `label` and `message`. It is an SMS/text dataset in style and content, not a full email corpus.

## Label meaning

| Original value | Encoded value | Meaning in this project |
| --- | ---: | --- |
| `ham` | 0 | Non-spam message in the supplied dataset |
| `spam` | 1 | Spam message in the supplied dataset |

The label is a dataset annotation, not an independent truth guarantee for new messages.

## Dataset scope and representativeness

The samples include short mobile messages, promotional offers, prize claims, conversational messages, and abbreviated language. This makes the dataset suitable for a basic SMS spam-classification exercise.

It does not provide the feature coverage needed for modern email security. In particular, it does not include structured email headers, sender identity, display-name spoofing, authentication results, attachment bytes, URL redirect chains, domain reputation, mailbox context, message threading, or enterprise threat telemetry.

## Data provenance and licensing

The current repository does not contain a verified source URL, dataset version, checksum, data card, or explicit dataset redistribution licence. The code repository's MIT license should not be assumed to license the dataset. Confirm the dataset source and its usage and redistribution conditions before publishing or reusing the CSV in another product.

## Data preparation

The notebook:
1. Reads the CSV using `encoding="latin-1"`.
2. Selects `Category` and `Message`.
3. Renames the selected columns to `label` and `message`.
4. Derives a normalized `clean_message` column.
5. Maps target labels to numeric values.

The notebook does not currently document a complete data provenance chain, checksum, deduplication report, privacy review, or detailed exploratory data-quality report.

## Data quality controls recommended

Before retraining:
- Confirm exactly which labels are present and reject unknown labels.
- Check for null and empty message values.
- Check duplicate messages and duplicate rows.
- Measure class balance before and after splitting.
- Inspect encoding and unusual Unicode characters.
- Verify that no unintended personal or sensitive content has been introduced.
- Record the source version and a cryptographic checksum.
- Document any filtering, deduplication, or relabeling.

## Train/test separation

The notebook uses `train_test_split` with a 20% test size and `random_state=42`. It does not currently specify `stratify`, so the class proportions in the partitions are not explicitly constrained to match the complete dataset. A future benchmark should consider stratification and report the class counts in both partitions.

Do not tune preprocessing, model settings, or decision thresholds repeatedly against the same held-out test partition and then describe the result as an unbiased final estimate.

## Handling policy

Use the checked-in sample dataset only for the documented educational purpose. Do not append real user messages, production inbox exports, confidential business correspondence, or messages containing personal identifiers without a legal basis, clear purpose, consent/notice where required, retention policy, and a proper privacy review.
