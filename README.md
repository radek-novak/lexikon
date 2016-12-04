Outputs word counts in a text file, while transforming words to their base forms e.g.:  
`teilgenommen` -> `teilnehmen`  
`seiner` -> `sein`  
`Schüle` -> `Schule`

output example:
```
1420 sein
1348 und
921 er
707 der
705 ein
612 die
546 zu```


uses: http://www.clips.ua.ac.be/pages/pattern-de

install:
`pip install pattern`

run:  
`PYTHONIOENCODING=utf-8 words.py your-book-name.txt > words-from-the-book.txt`
