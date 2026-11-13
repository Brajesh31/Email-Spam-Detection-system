# Model Evaluation and Reporting

## Existing notebook evaluation

The notebook splits the normalized message column into training and test partitions using:
- `test_size=0.2`;
- `random_state=42`;
- default `train_test_split` shuffling;
- no explicit `stratify` parameter.

The TF-IDF vectorizer is fitted only on `X_train` and then used to transform `X_test`. This avoids fitting the vocabulary and IDF statistics directly on the test partition.

The classifier is `MultinomialNB()` with default hyperparameters. The notebook predicts the held-out partition and calculates accuracy, a class-wise classification report, and a confusion matrix.

## Historical result

The checked-in notebook output records **96.68% accuracy**. This is a historical notebook output. It is not evidence that the checked-in model currently achieves that result in every environment, and it is not an email-security performance claim.

Do not report this number without disclosing the dataset scope, split method, class balance, software versions, and the fact that the data represents SMS-style messages.

## Metrics that matter

For a binary spam detector, report at least:

- **Precision for Spam:** proportion of messages predicted as spam that are actually labelled spam in the evaluation set.
- **Recall for Spam:** proportion of labelled spam messages correctly detected.
- **F1 for Spam:** harmonic mean of spam precision and spam recall.
- **Precision and recall for Ham:** needed to understand legitimate-message handling.
- **Confusion matrix:** true ham, false spam, missed spam and true spam counts.
- **Support:** number of held-out examples in each class.
- **False-positive rate:** especially important when legitimate messages must not be hidden or discarded.

Accuracy alone can conceal a weak minority-class result or a false-positive rate that is unacceptable for the intended workflow.

## Risks in the current evaluation design

- The split is not explicitly stratified.
- There is no cross-validation or repeated-split stability analysis.
- The notebook's historical metric output can become stale after code or artifact changes.
- The dataset's source, version and checksum are not documented.
- There is no external test corpus from a later time period.
- No threshold selection or calibration process is documented.
- No confusion-matrix counts are written into a durable model report.
- The dataset is SMS-focused and may not represent messages encountered in a modern email environment.

## Recommended benchmark protocol

1. Verify dataset provenance, licence and integrity.
2. Inspect nulls, duplicates and class distribution.
3. Create a held-out test set before model selection.
4. Consider stratified splits and record the exact seed and partition sizes.
5. Fit all learned transforms on training data only.
6. Perform model selection on training data or a separate validation set.
7. Evaluate once on the held-out test data.
8. Report per-class precision, recall, F1, support, confusion matrix and false-positive rates.
9. Evaluate on a temporally distinct or externally sourced corpus where possible.
10. Record environment versions, artifact checksums, preprocessing version and model configuration.

## Model changes

Any change to preprocessing, training rows, labels, split, vectorizer, or classifier requires a new training run and a matching export of both artifacts. Never replace only the vectorizer or only the classifier and assume compatibility.
