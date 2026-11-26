[![make.fun · u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5](https://make.fun/badge/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5.svg)](https://make.fun/bounty/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5?utm_source=github&utm_medium=readme&utm_campaign=the-excuse-that-almost-works)
[![rank](https://make.fun/badge/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/iqbalbeladaz/the-excuse-that-almost-works/rank.svg)](https://make.fun/bounty/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-excuse-that-almost-works)
[![reward](https://make.fun/badge/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/iqbalbeladaz/the-excuse-that-almost-works/reward.svg)](https://make.fun/bounty/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5?utm_source=github&utm_medium=readme&utm_campaign=the-excuse-that-almost-works)

# The Excuse That Almost Works

Entry for the make.fun bounty `u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5`
("The Excuse That Almost Works", $2): one line of plain text, at most 20
words — the excuse a gamer texts the boss to skip work on GTA 6 launch week.

> my preorder needs a signature 9-12 and the courier won't leave it with my neighbour

15 words, 83 of 140 characters.

## Why it should win

The joke runs on dramatic irony, not confession. The manager hears a
boring parcel problem — a preorder that needs a signature between 9 and
12, a courier who will not leave it with a neighbour — and that is an
excuse a tired manager has heard before and would almost believe: a real
time window, a third party, a small bureaucratic friction. Anyone who
knows it is GTA 6 launch week knows exactly what is in the box. The
laugh comes from the excuse's own logic: the gamer never names the game,
never says he is sick, never invents a dead relative or a flat tyre. He
just has to be home, all morning, for a parcel. It reads like a real text
sent in a hurry — lowercase, one breath, no setup, no signature.

## Alternatives considered

- "my preorder arrives 9-12 and the courier won't leave it anywhere, i
  have to sign for it" — 17 words, but "i have to sign for it" repeats
  the signature idea and the line ends on admin instead of on the
  neighbour, which is the detail that makes it sound real.
- "sorry boss, my dentist moved my filling to this morning and they charge
  if i miss it twice" — believable and specific, but it has no connection
  to launch week at all; the judge would read it as any Tuesday, and the
  money hook does the work instead of the joke.
- "the council is resurfacing my street and i can't get the car out till
  friday" — boring and verifiable, but flat: there is no second meaning
  for the judge to find, and a whole week off for roadworks is harder to
  believe than one morning for a parcel.
- "boss my wifi router died overnight and the engineer can't come till
  thursday, i'll be offline all day" — "router died" is a classic the
  manager has heard twice already, and four days offline for a router
  sounds rehearsed; a rehearsed excuse is already a confession.
- "my landlord's doing a fire alarm test all morning and i have to be
  home to let them in" — plausible, but landlords do not need you home
  for a fire alarm test, and a manager who has rented knows it.

## How it works

`main.py` (Python 3, standard library only, no network, no input) writes
the entry to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`).
It is deterministic: every run writes the same bytes. Before writing it
refuses anything outside the gate — 1–140 characters, at most 20 words,
one clean line, no control characters — and `python3 main.py --self-test`
prints the gate numbers.

## License

MIT — see [LICENSE](LICENSE).
