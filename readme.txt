This program is designed to play the game wordle, and guess the word in as few guesses as possible
This document details how it works

How it works:
    I started by giving each letter in the english alphabet a score, where the
    score is equivalent to how often it shows up compared to the least common letter "q".
    For example, "e" gets a score of 56 because it occurs 56 times more frequently than
    "q". "q" being the least frequent gets a score of 1.

    I then got a list of all possible words wordle could use and gave each of them a score.
    In this case the score was equivalent to the sum of the score of each of its letters,
    with the exception that if a letter appeared twice it was only given a score of 1 for its 
    second appearance. With all that done I sorted the list by scores from highest to lowest
    and used the highest scoring word as my first guess. In this case it was "irate"

    After this its just a simple process of elimination. You guess irate first, and then
    tell the program which letters dont appear, which letters appear but in the wrong place,
    and which letters appear in the right place. It then eliminates any words that wouldn't
    work. Then from the remaining words it makes its next guess the word with the highest score.

How it performs:
    At the time of uploading, I have yet to do a performance analysis, so if you're seeing this
    and want the results check later. I will update this document with my findings.
