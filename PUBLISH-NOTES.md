# Publish notes

What to do once this branch is merged into `main` and GitHub Pages has rebuilt (usually a minute or two).

## Privacy policy URLs for Play Console

Paste each one into Play Console > the app > Policy and programs > App content > Privacy policy.

| App | Privacy policy URL |
|---|---|
| Motivational Alarm | https://code7g.github.io/apps/motivational-alarm/privacy/ |
| G7Keyboard | https://code7g.github.io/apps/g7keyboard/privacy/ |
| Square Race | https://code7g.github.io/apps/square-race/privacy/ |
| The Brotherhood | https://code7g.github.io/apps/the-brotherhood/privacy/ |
| The Sisterhood | https://code7g.github.io/apps/the-sisterhood/privacy/ |
| 7GLauncher (not on Play yet) | https://code7g.github.io/apps/7glauncher/privacy/ |

All privacy policies are listed at https://code7g.github.io/privacy/.

## Website field in Play Console

Optional: each app's store listing contact details can point to its page here, for example https://code7g.github.io/apps/g7keyboard/.

## Before publishing

- Run `python tools/check_links.py` (should end with "No problems found.").
- Open the pages once on a phone after the deploy; the layout was checked in code, not on a real screen, for the G7Keyboard and Square Race policy pages.

## Points to check

- G7Keyboard's policy is new. It was written from the app's manifest (only the input method and vibration permissions, no internet, backup turned off) and its docs (encryption, clipboard history, Super Logging). Read it once before linking it in Play Console.
- G7Keyboard's page says "One-time purchase", taken from its store listing draft. Change it if the app's price model is different.
- Square Race's policy is the August 30, 2026 text with the contact address filled in. The app links Firestore, but no app code uses it, so the policy doesn't mention it. If Square Race starts using Firestore or another service, update the policy.
- Motivational Alarm's page and policy still give its own support address, contact.motivationalalarm@gmail.com. Every other page uses coder.7g@gmail.com.
