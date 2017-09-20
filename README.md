A simple extension to the gender.py library to take as input a CSV (Comma-Separated Values) file with one person info for each row and return the same file with additional columns related to their gender using the genderize.io API.

Usage example
-------
```
python genderCsv.py ./input.csv ./output.csv
```
Where:

- input.csv file must contain a column named "name" or "first name" (any combination of lower/upper case).
- output.csv file will contain the output of the script. It will be the same input.csv file with gender-related info.

Resuming a partial execution (maybe due to having reached the quota limits of genderize.io):
pass a input.csv file already containing the gender-related columns. GenderCsv.py will automatically resume the execution from the first row where the gender-related columns are not filled. 

Output
-------

Output is the same input.csv file with 3 additional columns (if they are not already there), namely: 
- gender (string), 
- confidence (float), 
- documents supporting the gender choice (int).

The values of those 3 columns are obtained via the [genderize.io](https://genderize.io) API

Requirements
-------

[from gender.py] Requires requests to function for HTTP requests.
