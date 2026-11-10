# TitleScore

Score YouTube titles with a simple deterministic rubric and get one improved variant for each title.

## Scoring rules

Every title starts at **50** points, and the final score is clamped to **0-100**:

| Rule | Points |
| --- | --- |
| Length 30-60 characters | +15 |
| Length 61-70 characters | +5 |
| Length under 20 characters | -15 |
| Length over 80 characters | -10 |
| Contains a digit | +15 |
| Contains a power word (secret, mistakes, nobody, stop, proven, free, easy, fastest, truth, warning, shocking, actually, never, always, worst, best, ...) | +15 |
| Contains brackets or parentheses with text inside | +10 |
| Whole title is ALL CAPS (more than 80% of letters uppercase) | -15 |
| Fewer than 4 words | -10 |

Verdicts: **75+ Strong**, **50-74 Okay**, **under 50 Weak**.

For each title the tool also prints one suggested improvement: it adds a
"(What Nobody Tells You)" hook when there is no number and no bracket,
prefixes "5 " when there are brackets but no number, and says no change is
needed when the title already has both.

## Requirements

- Python 3
- Standard library only, nothing to install

## Usage

```bash
python3 titlescore.py --title "my video about fishing" --title "5 Mistakes That Kill Your Fishing Luck (Nobody Tells You)"
```

Repeat `--title` for as many titles as you like; at least one is required.
See `examples.md` for real output.

## License

MIT - see `LICENSE`.
