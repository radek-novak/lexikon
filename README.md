# Lexikon

<img width="263" src="https://cloud.githubusercontent.com/assets/381895/20901807/8d964852-bb34-11e6-9150-245bdaadb35a.png">

Outputs word counts in a text file, while transforming words to their base forms e.g.:

`teilgenommen` -> `teilnehmen`

`seiner` -> `sein`

`Schüle` -> `Schule`

Output example:
```
1420 sein
1348 und
921 er
707 der
705 ein
612 die
546 zu
```

Uses [http://www.clips.ua.ac.be/pages/pattern-de](http://www.clips.ua.ac.be/pages/pattern-de)

### Install:
```
pip install pattern
```

### Run
```
PYTHONIOENCODING=utf-8 ./words.py your-book-name.txt > words-from-the-book.txt
```
