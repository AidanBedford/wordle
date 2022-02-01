This program is a tool to beat the game wordle. The game itself is simple, but playing it perfectly
is harder to guage. My goal is to create a program that gets the lowest average guesses required
accross all possible words in the wordle word bank.

How it works:
    The most important aspect of playing wordle is what to do on your first guess. To determine
    what to use as my first guess, I scored each word based on how many other words they share 
    at least one letter with. Using this method, I came up "arise" as my first guess. I can
    improve this ranking, perhaps by also giving factoring in how many letters in
    the correct position this word shares with another, but for now this is my method.

    Using this method I collect results from the guess: Letters that arent in the correct word,
    letters that are in the word but currently arent in the right place, and letters in the right
    place. Using this information, I filter out all words that are no longer possible to be the word.
    I rescore each word using the same method as before, except now the score is based on only the remaining 
    words. I continue this process until the correct guess is given.


How it performs:
    At the time of uploading, I have yet to do a performance analysis, so if you're seeing this
    and want the results check later. I will update this document with my findings.

