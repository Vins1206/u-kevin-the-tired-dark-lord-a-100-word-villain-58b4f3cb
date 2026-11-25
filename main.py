"""The Tired Dark Lord: a 100-word villain monologue.

Writes one monologue to /output/entry.txt. Pure standard library,
deterministic: the text is fixed, so every run writes identical bytes.

The speaker is Kevin, dark lord of one tower for nine hundred years.
His tiredness is never announced: it lives in the lost thread
("the keys are -- somewhere"), the pauses, and the paperwork he
keeps deflecting to -- permits, forms, three copies for ravens
who eat the copies. The sting lands in the last line.
"""

import os

MONOLOGUE = (
    "Sit down. No, not there \u2014 that chair bites. I am Kevin, and I have "
    "ruled this tower for nine hundred years. The paperwork alone could "
    "bury a dragon: permits for the moat, forms for the curse, three "
    "copies for the ravens, who eat the copies. You came to kill me? "
    "Fine. The sword is on the rack, the crown is on the hook, the keys "
    "are \u2014 somewhere. Take them all. Only sign here first. And here. "
    "The realm runs on signatures, hero, and I have signed my name so "
    "many times I have forgotten how to spell it."
)


def main():
    # Gate the entry before writing it: about 100 words, and the
    # competition gate allows 1-600 characters of UTF-8 text.
    words = MONOLOGUE.split()
    assert len(words) == 100, f"monologue is {len(words)} words, want 100"
    assert 1 <= len(MONOLOGUE) <= 600, "monologue over the 600-char gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(MONOLOGUE)


if __name__ == "__main__":
    main()
