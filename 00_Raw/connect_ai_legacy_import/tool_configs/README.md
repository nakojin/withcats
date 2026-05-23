# Connect AI Legacy Tool Config Archive

Purpose: archive a small set of legacy Connect AI tool config JSON files for later manual reference. These files are not intended for direct execution or live integration.

Included files:

- `lint_test.json`: developer lint/test tool config.
- `pack_apply.json`: developer package/apply workflow config.
- `web_preview.json`: developer web preview command config.
- `music_to_video.json`: editor music-to-video tool config.

Sensitive pattern check:

- No token, secret, key, oauth, password, bearer, telegram, youtube, paypal, cookie, credential, api_key, access_token, or refresh_token keyword hits were found in these four files during the final archive check.
- No high-confidence credential value patterns were detected.

Manual review note:

- Review manually before any execution, automation, or service integration.
- Do not merge these files into active agent config, memory, tracker, or company state files automatically.
