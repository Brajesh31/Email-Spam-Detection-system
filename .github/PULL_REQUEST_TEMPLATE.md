## Summary
Describe the problem and the change.

## Change type
- [ ] Flask route or UI
- [ ] Preprocessing
- [ ] Dataset
- [ ] Classifier or vectorizer
- [ ] Notebook
- [ ] Tests or CI
- [ ] Documentation
- [ ] Dependencies or operations

## Validation
- [ ] `python -m compileall -q app.py tests scripts`
- [ ] `python -m unittest discover -s tests -v`
- [ ] Started the Flask app locally
- [ ] For notebook changes, ran the notebook from a clean kernel
- [ ] For model changes, recorded held-out precision, recall, F1, support and confusion matrix

## Model artefacts
State whether the classifier and vectorizer were regenerated together. Include package versions, preprocessing changes, dataset provenance and artifact version/checksum when applicable.

## Data safety
- [ ] No private message samples, credentials, personal data or confidential exports added.
- [ ] Serialized model files come from a trusted reviewed process.

## Documentation
- [ ] Updated API, dataset, preprocessing, evaluation, model card and operational docs where relevant.
- [ ] Stated current scope and known limitations accurately.
