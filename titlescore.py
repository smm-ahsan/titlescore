#!/usr/bin/env python3
"""TitleScore - score YouTube titles and suggest an improved variant.

Deterministic scoring, standard library only.
"""

import argparse
import re
import sys

POWER_WORDS = [
    "secret", "secrets", "mistake", "mistakes", "nobody", "stop",
    "proven", "free", "easy", "fastest", "truth", "warning",
    "shocking", "actually", "never", "always", "worst", "best",
]

POWER_RE = re.compile(r"\b(" + "|".join(POWER_WORDS) + r")\b", re.IGNORECASE)
BRACKET_RE = re.compile(r"[\(\[][^\)\]]+[\)\]]")


def score_title(title):
    """Return (score, reasons, has_digit, has_brackets) for a title."""
    score = 50
    reasons = []

    length = len(title)
    if length < 20:
        score -= 15
        reasons.append("-15 too short (under 20 characters)")
    elif 30 <= length <= 60:
        score += 15
        reasons.append("+15 good length (30-60 characters)")
    elif 61 <= length <= 70:
        score += 5
        reasons.append("+5 slightly long (61-70 characters)")
    elif length > 80:
        score -= 10
        reasons.append("-10 too long (over 80 characters)")

    has_digit = any(ch.isdigit() for ch in title)
    if has_digit:
        score += 15
        reasons.append("+15 has a number")

    if POWER_RE.search(title):
        score += 15
        reasons.append("+15 has a power word")

    has_brackets = bool(BRACKET_RE.search(title))
    if has_brackets:
        score += 10
        reasons.append("+10 brackets add curiosity")

    letters = [ch for ch in title if ch.isalpha()]
    if letters:
        upper = sum(1 for ch in letters if ch.isupper())
        if upper / len(letters) > 0.8:
            score -= 15
            reasons.append("-15 ALL CAPS")

    if len(title.split()) < 4:
        score -= 10
        reasons.append("-10 too few words (under 4)")

    score = max(0, min(100, score))
    return score, reasons, has_digit, has_brackets


def verdict(score):
    if score >= 75:
        return "Strong"
    if score >= 50:
        return "Okay"
    return "Weak"


def suggestion(title, has_digit, has_brackets):
    if has_digit and has_brackets:
        return "No change needed - strong structure."
    if not has_digit and has_brackets:
        return "5 " + title
    return title + " (What Nobody Tells You)"


def main():
    parser = argparse.ArgumentParser(
        description="Score YouTube titles and suggest an improved variant."
    )
    parser.add_argument(
        "--title",
        action="append",
        required=True,
        help="A YouTube title to score. Repeat the flag for multiple titles.",
    )
    args = parser.parse_args()

    for i, title in enumerate(args.title):
        if i:
            print()
        score, reasons, has_digit, has_brackets = score_title(title)
        print(f'Title: "{title}"')
        print(f"Score: {score}/100")
        print(f"Verdict: {verdict(score)}")
        if reasons:
            print("Reasons:")
            for reason in reasons:
                print(f"  {reason}")
        else:
            print("Reasons: none of the scoring rules fired")
        print(f"Suggested improvement: {suggestion(title, has_digit, has_brackets)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
