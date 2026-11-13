# Security Policy

## Important security notes
- The Flask app currently starts with `debug=True`. This is for local development only. Never expose the development server to the public internet.
- Pickle/joblib model artifacts can execute code when loaded. Only load artifacts produced by a trusted, reviewed training process.
- Do not submit real private emails, SMS messages, passwords, financial details, or personal data to this demo.
- Do not treat model output as a definitive security decision.

## Reporting
Please do not publish exploitable vulnerabilities or sensitive data in a public issue. Use GitHub's private vulnerability reporting feature when available, or contact the repository owner privately with impact and reproduction details.
