---
name: ste-ui-text-audit
description: Scan a web application for user-facing instructional text — form labels, placeholders, validation messages, errors, buttons, dialogs, toasts, empty states, help text — and rewrite it to ASD-STE100 Simplified Technical English. Classify every string by purpose first. Rewrite only text whose primary job is to instruct or inform the user about an action or state. Never rewrite expressive content (blog posts, marketing copy, brand voice) or legal text. Use when asked to simplify, de-slop, standardize, or audit UI copy.
---

# STE UI Text Audit

Rewrite instructional UI text to ASD-STE100 Simplified Technical English. Leave everything else untouched.

## Core principle

Every string gets classified by its **primary purpose** before any edit:

- **INSTRUCTIONAL** — the text's job is to tell the user what to do, what happened, or what a control does. If the user misreads it, something functionally goes wrong: a form fails, a wrong action is taken, system state is misunderstood. → **Rewrite to STE.**
- **EXPRESSIVE** — the text's job is to persuade, entertain, or carry brand voice. → **Do not edit.**
- **LEGAL** — regulated or contractual text. → **Do not edit. Flag for human review.**
- **UNKNOWN** — purpose is ambiguous from context. → **Do not edit. List in the report for a human decision.**

When in doubt, do not edit. A missed rewrite is cheap; a wrong rewrite of legal or brand copy is not.

## Scope

### Rewrite (INSTRUCTIONAL)

- Form labels, placeholders, help/description text, fieldset legends
- Validation and error messages (client and server), including Zod/schema messages
- Button and link text that triggers an action
- Confirmation, alert, and destructive-action dialogs
- Toast/notification messages (success, error, info)
- Empty states, loading-failure states, error pages (404/500)
- Tooltips, onboarding steps, settings descriptions
- Transactional microcopy (e.g., "Check your email for a sign-in link")

### Never edit

- Blog posts, articles, docs prose, changelog entries, `.md`/`.mdx` content
- Marketing and landing-page copy: hero text, taglines, feature pitches, testimonials, pricing page persuasion copy
- Legal: Terms, Privacy Policy, cookie/consent text, disclaimers, compliance copy
- SEO meta titles/descriptions, Open Graph copy
- User-generated content, product names, proper nouns
- i18n keys, code identifiers, error codes, non-source locale files

## Workflow

1. **Discover.** Find candidate strings (see Detection patterns). Default roots: `src/`, `app/`, `components/`, `messages/`, `locales/`, `lib/`. Exclude: `content/`, `posts/`, `blog/`, `marketing/`, `*.md`, `*.mdx`, `node_modules`, test fixtures.
2. **Extract.** Record each string with `file:line`, its UI type (label, placeholder, error, button, …), and surrounding context (component name, nearby code).
3. **Classify.** Assign INSTRUCTIONAL / EXPRESSIVE / LEGAL / UNKNOWN per the core principle. Use file path and component context: a string in `BlogPost.tsx` or `content/` is EXPRESSIVE; a string in `DeleteProjectDialog.tsx` is INSTRUCTIONAL.
4. **Rewrite.** Apply the STE rules and UI conventions below to INSTRUCTIONAL strings only. Build a term map first (step 4a) so wording is consistent across the app.
5. **Apply edits.** Exact string replacement. Preserve interpolation, tags, and keys (see Guardrails). For i18n projects, edit only the source locale (usually `en`) and mark other locales as stale in the report.
6. **Report + verify.** Produce the report (format below), run the banned-pattern sweep, then run typecheck and tests.

### 4a. Term map (do this before rewriting)

List every concept the UI names (sign in, delete, save, email address, project, invoice…) and pick ONE word per concept. Use it everywhere. STE's core rule is one word = one meaning: if half the app says "remove" and half says "delete", pick one and standardize. Include the term map in the report.

## Detection patterns

Run these (ripgrep shown; adapt as needed). Also read matched files for JSX text nodes between tags — greps miss plain text children.

```bash
# Attributes
rg -n --glob '*.{tsx,jsx,vue,svelte,html}' 'placeholder=|aria-label=|title=|alt='

# shadcn/ui + react-hook-form
rg -n '<Form(Label|Description|Message)|<FormMessage|description='

# Toasts / notifications
rg -n 'toast\.(success|error|info|warning)\(|notify\(|addNotification\('

# Dialogs
rg -n '<(AlertDialog|Dialog|ConfirmDialog)|confirm\('

# Schema validation messages (Zod, Yup)
rg -n '\.(min|max|email|url|regex|refine|superRefine)\(|message:|errorMap|invalid_type_error|required_error'

# i18n source files
ls messages/ locales/ public/locales/ 2>/dev/null; rg -n '' messages/en.json locales/en*.json 2>/dev/null

# Hard-coded JSX text (heuristic — review each hit)
rg -n --glob '*.tsx' '>[^<{}`]{8,}<'
```

## STE rewrite rules

Apply all of these to INSTRUCTIONAL strings:

1. One instruction per sentence. Start instructions with an imperative verb: "Enter your email address." not "Your email address must be entered."
2. Length: max 20 words per instruction, 25 per description. UI-specific limits below are tighter.
3. Active voice only. "We could not save your changes." not "Your changes could not be saved."
4. Simple tenses only: present, past, "will" future. No perfect ("has been"), no continuous ("is loading" → allowed only as a live status label, prefer "Loading…").
5. Condition before command: "If you have a discount code, enter it at checkout." Never bury the condition after the action.
6. No hedging modals. Replace should / would / may / might / could with must / can / will, or delete. "You should save your work" → "Save your work."
7. One word per meaning, per the term map. No synonym rotation (delete/remove/erase → pick one).
8. Prefer single approved verbs over phrasal constructions when the phrasal verb is ambiguous. Fixed UI terms ("Sign in", "Sign up", "Log out") are allowed — put them in the term map.
9. No noun clusters longer than 3 words. "Account recovery email address" → "Recovery email address".
10. Keep articles (a, an, the). STE requires them; do not write telegraphic copy like "Enter email, press button."
11. Numbers as numerals: "3 attempts left", not "three attempts left".
12. Severity prefixes where they apply: "WARNING:" for irreversible/dangerous, "CAUTION:" for risk of error, "NOTE:" for important neutral info. Use sparingly — most UI text needs none.
13. No exclamation marks in functional text. No filler/interjections: "Oops", "Whoops", "Looks like", "Just", "Simply", "Please note", "In order to" (→ "To").
14. Remove "please" from instructions. Keep tone neutral and direct; STE politeness is clarity, not softeners.
15. Error message pattern: what happened → what the user does → escalation if it persists. "Save failed. Try again. If the problem continues, contact support."

## UI conventions

| Element | Convention | Example |
|---|---|---|
| Button | Verb (+ noun), ≤ 3 words | "Save changes", "Delete project" |
| Link (action) | Verb phrase, names destination | "View invoice" |
| Form label | Noun phrase, ≤ 4 words | "Email address" |
| Placeholder | Example value or noun phrase; never the only instruction | "name@example.com" |
| Help text | One sentence; condition-first if conditional | "We use this to send receipts." |
| Validation | Imperative or short statement | "Enter a valid email address." / "This field is required." |
| Success toast | Noun + past-tense verb, ≤ 4 words | "Changes saved." |
| Error toast | Rule 15 pattern | "Payment failed. Check your card details and try again." |
| Confirmation dialog | Question naming the object + consequence | "Delete invoice #123? You cannot restore it." |
| Empty state | What this is + one action | "No invoices yet. Create your first invoice." |
| Tooltip | One sentence, ≤ 15 words | "This key gives full access to your account." |

## Before / after examples

| Before | After | Rules |
|---|---|---|
| "Please enter your email address here" (placeholder) | "name@example.com" | Placeholder convention |
| "Oops! Looks like you forgot to fill this field in" | "This field is required." | 13, 15 |
| "Click here to submit your application" (button) | "Submit application" | Button convention |
| "Something went wrong while trying to save. Please try again later!" | "Save failed. Try again." | 6, 13, 15 |
| "Are you sure you want to permanently delete this project? This action cannot be undone." | "Delete project 'Atlas'? You cannot restore it." | 2, 12 |
| "In order to receive notifications, you should enable them in settings" | "To receive notifications, enable them in Settings." | 5, 6, 13 |
| "Your password must be at least 8 characters long and should contain a number" | "Use at least 8 characters, including 1 number." | 1, 6 |
| "You don't have any invoices yet! Click below to get started creating your first one." | "No invoices yet. Create your first invoice." | 2, 13 |

## Guardrails

Hard rules — violations make the edit wrong even if the STE is perfect:

- Never edit LEGAL or EXPRESSIVE text (see Scope). Never edit i18n keys, only values. Never edit non-source locales — flag them as stale instead.
- Preserve exactly: `{variables}`, ICU syntax (`{count, plural, one{…} other{…}}`), JSX/HTML tags, markdown links, keyboard shortcuts, units, error codes.
- Never make a string longer than the original unless fixing a real ambiguity — UI space is constrained.
- Never change meaning. If the original is ambiguous and you cannot infer intent from code context, classify UNKNOWN and flag it. Do not guess.
- Do not "improve" tone beyond STE rules — no added friendliness, emojis, or brand voice.
- Put all edits in a separate commit or branch. Run typecheck and the test suite after applying.

## Report format

Output this after applying edits:

```markdown
## STE UI Text Audit — <date>

### Term map
| Concept | Chosen term | Replaced |
|---|---|---|
| sign in | "Sign in" | "Log in" (3 files) |

### Rewritten (N strings)
| File:Line | Type | Before | After | Rules |
|---|---|---|---|---|

### Skipped — expressive (N)
| File:Line | String (truncated) | Reason |

### Skipped — legal (N) — needs human review
| File:Line | String (truncated) | Reason |

### Unknown — needs a decision (N)
| File:Line | String (truncated) | Context |

### Stale locales
- locales/fr.json: 12 keys changed in source locale, retranslation needed
```

## Verification

1. Re-run the detection greps — confirm no INSTRUCTIONAL string was missed.
2. Banned-pattern sweep over edited files; every hit in instructional text is a failure:

```bash
rg -in '\b(should|would|may|might|oops|whoops|simply|just)\b|in order to|please note|!' \
  --glob '*.{tsx,jsx,json}' <edited paths>
```

3. Run typecheck and tests. Fix any snapshot failures caused by string changes — update snapshots, never revert the copy to make a stale snapshot pass.
