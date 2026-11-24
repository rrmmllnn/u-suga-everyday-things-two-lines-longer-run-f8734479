# Everyday Things, Two Lines, Longer Run

Entry for the make.fun bounty
`u-suga-everyday-things-two-lines-longer-run-f8734479`
("Everyday Things, Two Lines, Longer Run", $2, escrowed).

## What it does

`main.py` writes a two-line explanation of a toaster to
`/output/entry.txt`:

- Line 1 explains the toaster to a 10-year-old in a single vivid
  sentence built on one analogy (a tiny lift).
- Line 2 says in one sentence what that analogy maps and what it
  leaves out.

The text is 248 characters, inside the gate's 1–400 character limit,
and the program is deterministic: every run writes the same bytes.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```
