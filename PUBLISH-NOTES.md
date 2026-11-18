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
| WakeWay (not on Play yet, new) | https://code7g.github.io/apps/wakeway/privacy/ |
| Billhook (not on Play yet, new) | https://code7g.github.io/apps/billhook/privacy/ |
| ReadMD (not on Play yet, new) | https://code7g.github.io/apps/readmd/privacy/ |
| ShareWave (not on Play yet, new) | https://code7g.github.io/apps/sharewave/privacy/ |

All privacy policies are listed at https://code7g.github.io/privacy/.

## Terms of Service URLs (added 16 November 2026)

Each app has its own terms page, effective 16 November 2026. Play Console has no required terms field for most apps; use these wherever a terms link is asked for (for example the subscription or store listing details, or in the app's About or Settings screen). All are listed at https://code7g.github.io/terms/.

| App | Terms of Service URL |
|---|---|
| Motivational Alarm | https://code7g.github.io/apps/motivational-alarm/terms/ |
| G7Keyboard | https://code7g.github.io/apps/g7keyboard/terms/ |
| Square Race | https://code7g.github.io/apps/square-race/terms/ |
| The Brotherhood | https://code7g.github.io/apps/the-brotherhood/terms/ |
| The Sisterhood | https://code7g.github.io/apps/the-sisterhood/terms/ |
| 7GLauncher (not on Play yet) | https://code7g.github.io/apps/7glauncher/terms/ |
| WakeWay (not on Play yet) | https://code7g.github.io/apps/wakeway/terms/ |
| Billhook (not on Play yet) | https://code7g.github.io/apps/billhook/terms/ |
| ReadMD (not on Play yet) | https://code7g.github.io/apps/readmd/terms/ |
| ShareWave (not on Play yet) | https://code7g.github.io/apps/sharewave/terms/ |

## Website field in Play Console

Optional: each app's store listing contact details can point to its page here, for example https://code7g.github.io/apps/g7keyboard/.

## Before publishing

- Run `python tools/check_links.py` (should end with "No problems found.").
- Open the pages once on a phone after the deploy; the layout was checked in code, not on a real screen, for the G7Keyboard and Square Race policy pages.

## Points to check

- G7Keyboard's policy is new. It was written from the app's manifest (only the input method and vibration permissions, no internet, backup turned off) and its docs (encryption, clipboard history, Super Logging). Read it once before linking it in Play Console.
- G7Keyboard's page says "One-time purchase", taken from its store listing draft. Change it if the app's price model is different.
- Square Race's policy is the August 30, 2026 text with the contact address filled in. The app links Firestore, but no app code uses it, so the policy doesn't mention it. If Square Race starts using Firestore or another service, update the policy.
- Motivational Alarm's app page and terms still give its own support address, contact.motivationalalarm@gmail.com. Its privacy policy uses coder.7g@gmail.com since 18 November 2026, like every other page.

## Points to check for the terms and the new pages (16 November 2026)

The terms were written from each app's repo, not by a lawyer. Read each one once before linking it. In particular:

- **All apps:** governing law is Slovenia, with EU consumers keeping their own country's mandatory rights. Liability is capped at what the user paid in the last 12 months or 50 euros, whichever is more. Change these if you want different terms.
- **Motivational Alarm:** the terms use its own address, contact.motivationalalarm@gmail.com, like its privacy policy. They say "get paid to get up" means Motivation and XP only, never real money.
- **G7Keyboard:** described as a paid app with a one-time price and no in-app purchases (from its listing). Change it if that's wrong.
- **Square Race:** the terms describe the Gem packs, the Square Race VIP subscription, Square Chests and where the drop rates are shown in the game ("Drop rates" in the chest opening screen, and the chests sheet from the world map or the shop), and the fixed-contents chests in countries that require them. The game's **privacy policy doesn't mention the VIP subscription yet**; consider adding a line, as the other apps' policies have.
- **The Brotherhood and The Sisterhood:** the terms mention Premium (monthly or yearly, with a possible 7-day trial), Premium Lifetime, single programs, Discipline packs and bundles, rewarded ads only, and the health, fasting and (Sisterhood) cycle disclaimers. Their in-app ad notice still says interstitial ads are shown; the apps no longer show them.
- **7GLauncher:** described as a paid app with a one-time price once on Play, no in-app purchases. The price isn't decided yet; change the text if it ends up free.
- **WakeWay (new privacy policy and terms):** written from the app's code. The app has no Firebase (removed), so the policy says there is no analytics or crash reporting. Its in-app "Privacy & Data Usage" text still says it uses Firebase, and needs fixing in the app before release. The ad unit ids are still Google's test ids. No support email was found in the repo; the pages use coder.7g@gmail.com. The app page has the icon (drawn from the app's vector icon) but no screenshots, because the repo has no store listing yet.
- **Billhook (new privacy policy and terms):** the website policy matches the policy text shipped in the app (dated 9 November) and adds the permission list and contact. The in-app text says the contact is "the developer email address shown on Billhook's Google Play listing"; make that coder.7g@gmail.com in Play Console, or change the pages. The name Billhook is still a working name.
- WakeWay and Billhook show as "Coming soon". When they go live on Play, change their status and add the Google Play button, as for the other apps.

## Points to check for ReadMD (17 November 2026)

- **Privacy policy:** the text of the app's `assets/privacy-policy/privacy-policy.md` (17 November 2026), unchanged. It promises three Firebase console settings: data retention 2 months, Google signals off, data sharing settings off. Set them in the Firebase project before this page goes live and before the app ships with analytics.
- **Terms:** from ReadMD's `docs/website-drafts.md`, effective 17 November 2026. If the pages go live on a later day, change the effective date. Liability is capped at 50 euros (the app is free), governing law is Slovenia like the others.
- **App page:** "Coming soon", no store buttons. Screenshots are the v2 phone set, cut to 9:16 from the bottom (the originals are 1:2) so the web layout doesn't crop the top bar. When it goes live on Play or the Microsoft Store, change the status and add the store button.

## Points to check for ShareWave (17 November 2026)

- **Privacy policy:** based on the app's `assets/privacy-policy/privacy-policy.md` (15 October 2026), checked against the current code (version 1.0.1) and brought up to date. It names the local-network discovery (mDNS) and what the pairing QR code contains, because a privacy policy has to; it leaves out the encryption details (no TLS versions), since the design stays private for now. It covers the Android app only and says the policy will be updated before the Windows app ships. Update the app's own `privacy-policy.md` to match this page.
- **Terms:** new, effective 17 November 2026, same structure and Slovenian law as the others. The app is free, so liability is capped at 50 euros.
- **App page:** "Coming soon", no store button. It says a Windows app is planned, though the Play listing draft leaves Windows out until it ships. Screenshots are the v1 phone set (1080 x 1920, resized to 540 x 960). They show peers named "Desktop PC" and "Work laptop", `04_background` still has the old template icon, and `05_pairing` shows a full pairing link from an emulator. Replace them when the store screenshots are re-captured.
