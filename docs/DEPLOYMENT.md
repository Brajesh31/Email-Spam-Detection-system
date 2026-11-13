# Deployment

This repository is currently a local Flask demonstration. The built-in Flask development server with debug mode enabled is not suitable for public deployment.

Before deployment:
1. Disable debug mode in the application configuration.
2. Use a production WSGI server such as Gunicorn or Waitress.
3. Put the application behind HTTPS and a reverse proxy.
4. Set request-size limits and validate empty or excessively long submissions.
5. Add rate limiting and operational logging without recording sensitive message content.
6. Verify that model artifacts come from a trusted build.
7. Define a privacy and retention policy for submitted text.

Do not deploy until the debug-server configuration has been corrected and the app has been tested under the intended WSGI server.
