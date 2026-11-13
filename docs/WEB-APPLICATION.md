# Web Application and User Interface

## Page structure

The Flask UI is server-rendered with Jinja.

- `templates/index.html` defines the page title, message entry form, error region, prediction state and analyzed-message section.
- `static/style.css` defines the centered card layout, form controls, focus outline, result colors, error styling and responsive mobile adjustments.
- `app.py` passes `result`, `email_text`, `error` and `max_message_length` into the template.

## Form behaviour

When there is no result, the page displays a textarea named `email_text` and posts it to `/predict`. The HTML `required` attribute is a client-side convenience. Server-side validation remains authoritative.

The browser maxlength is set to 10,000 characters, matching the Flask message limit. Flask also sets a 16 KiB maximum request body size, which can reject a request before character validation due to form-encoding overhead.

## Result behaviour

After a prediction:
- the result label is rendered in a class-specific result region;
- the submitted text is rendered inside a text paragraph;
- a GET form provides a route back to the empty form.

The result region uses `aria-live="polite"`. The error region uses `role="alert"`. Jinja autoescaping remains enabled for message content.

## Visual system

The CSS uses:
- a light neutral page background;
- a white centered container with rounded corners and shadow;
- readable system-level spacing and typography;
- visible focus styling on textarea and buttons;
- red styling for spam, green styling for not-spam, and amber styling for errors;
- a narrow-screen media query for reduced page padding and smaller heading size.

The page imports Inter from Google Fonts and an externally hosted Font Awesome kit. These are third-party resources, not bundled assets. They may be unavailable under strict network policies and should be reviewed for production privacy and availability.

## Accessibility review points

- Keep labels programmatically connected to inputs.
- Keep focus visible and preserve keyboard submission.
- Preserve screen-reader announcements for result and errors.
- Ensure result categories are not communicated by color alone.
- Keep responsive layout readable at narrow widths and zoom.
- Consider replacing externally loaded icons with local assets if privacy or uptime requires it.

## Non-functional UI elements

The title says "Text Spam Detector". It accepts plain text. It does not send or parse email messages, inspect headers, access a mailbox, or process attachments. Do not reintroduce language that claims full email inspection.
