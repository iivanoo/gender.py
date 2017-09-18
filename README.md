A simple extension to the gender.py library to take first names as a single .csv file and return the same file with additional columns related to their gender using the genderize.io API.

Usage example
-------
```
python genderCsv.py ./names.csv
```
Where the names.csv file should contain a column named "name" or "first name" (any combination of lower/upper case).

Resuming a partial execution (maybe due to having reached the quota limits of genderize.io):
pass a names.csv file already containing the gender-related columns. GenderCsv.py will automatically resume the execution from the first row where the gender-related columns are not filled. 

Output
-------

Output is the same names.csv file with 3 additional columns (if they are not already there), namely: name (string), confidence (float), documents supporting the gender choice (int).

Requirements
-------

[from gender.py] Requires requests to function for HTTP requests.
