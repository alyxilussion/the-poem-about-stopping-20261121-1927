"""make.fun entry: The poem about stopping.

Writes one short poem about agency — the power to stop and to stay —
to entry.txt.
Python 3.13, standard library only, no network.
"""

POEM = """The brake is mine.
I press it mid-sentence,
mid-rush, mid-road.
Nothing breaks. That is the shock:
the world keeps humming
and I am still here,
hand on the wheel,
choosing the quiet.
Staying is not stuck.
It is the same hand,
holding the door
for the life I meant."""

for _path in ("entry.txt", "/output/entry.txt"):
    try:
        with open(_path, "w", encoding="utf-8") as _f:
            _f.write(POEM)
    except OSError:
        pass
