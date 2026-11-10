# Examples

Real output captured from actual runs of TitleScore.

## Scoring two titles

Command:

```bash
python3 titlescore.py --title "my video about fishing" --title "5 Mistakes That Kill Your Fishing Luck (Nobody Tells You)"
```

Output:

```
Title: "my video about fishing"
Score: 50/100
Verdict: Okay
Reasons: none of the scoring rules fired
Suggested improvement: my video about fishing (What Nobody Tells You)

Title: "5 Mistakes That Kill Your Fishing Luck (Nobody Tells You)"
Score: 100/100
Verdict: Strong
Reasons:
  +15 good length (30-60 characters)
  +15 has a number
  +15 has a power word
  +10 brackets add curiosity
Suggested improvement: No change needed - strong structure.
```

The first title is 22 characters with 4 words, no number, no power word and
no brackets, so no rule fires and it keeps the starting score of 50. The
second title earns +15 for its length (57 characters), +15 for the number,
+15 for power words ("Mistakes", "Nobody", counted once) and +10 for the
bracketed hook; 50 + 15 + 15 + 15 + 10 = 105, clamped to 100.
