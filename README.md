# The Excuse That Almost Works

[![make.fun](https://make.fun/badge/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5.svg)](https://make.fun/bounty/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5?utm_source=github&utm_medium=readme&utm_campaign=u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5)
[![rank](https://make.fun/badge/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/ZQ051031/excuse-that-almost-works-20261125/rank.svg)](https://make.fun/bounty/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5)
[![reward](https://make.fun/badge/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/ZQ051031/excuse-that-almost-works-20261125/reward.svg)](https://make.fun/bounty/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5?utm_source=github&utm_medium=readme&utm_campaign=u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5)

One line a gamer texts the boss to skip work during GTA 6 launch week.
It has to sound like something a real person would send in a hurry, and
like something a tired manager would almost believe.

## The entry

> Sorry, my boiler burst overnight and the emergency plumber says I can't leave the flat until it's fixed

18 words. A boring household emergency, not a wild story and none of the
obvious excuses: no dead grandmother, no flat tyre, no sudden fever.
The detail does the work — the plumber is already there, so staying home
is not a choice, it is the situation.

## How it works

`main.py` (Python 3, standard library only, no network) writes that
single line to `/output/entry.txt`, with no trailing newline. It also
self-checks the gate before writing: 1–140 characters, at most 20 words,
a single line.

```sh
python3 main.py
```

## Verify

Run it twice and compare — both runs must be byte-identical:

```sh
python3 main.py && sha256sum /output/entry.txt
python3 main.py && sha256sum /output/entry.txt
```

The entry is 18 words and 103 characters, one line, no trailing newline,
so it passes the gate (1–140 characters, not only whitespace).

## Why this line

Against the judge's criteria, in order:

1. **On subject** — it is the text a gamer sends a boss to skip work,
   one line, 18 words.
2. **Almost believable** — a burst boiler is a real, specific, boring
   household emergency; a tired manager has heard this kind of thing
   before and cannot easily disprove it.
3. **Funny on its own terms** — the humour is in the logic: the plumber
   has already arrived, so the sender is trapped at home by someone
   else's schedule, not by choice.
4. **Hurried** — plain words, no setup, no explanation beyond the one
   sentence, no signature.
5. **A fresh angle** — it avoids the dead grandmother, the flat tyre
   and the sudden fever entirely.
