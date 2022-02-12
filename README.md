# my_first_calculatorDB.py
I found [my_first_calculator.py](https://github.com/AceLewis/my_first_calculator.py) made by [AceLewis](https://github.com/AceLewis). The project is neat,
it can calculate any value between 0 and 50. But I didn't like that limit and if you attempt to expand to 1000, it would crash. So, I came up with an idea of about making a SQLite database to keep all those values.

This calculator is an improvement from `my_first_calculator.py` to where it accepts negatives and decimals to find the answer. The current `calc.db` file only accept values from -200 to 200 (no decimal), if you want to expand this you can regenerate the file.

## generate.py
This script generates the DB and accept decimals as well. Just note, generating with decimals would make the file big. Generating a db with the range -250.0 to -250.9 will make over 100,000,000 rows with a 3.8 GB file.

You can generate this file with the settings:
- Min Value: -250
- Max Value: 250
- Step: 0.1

------------------------
###### Note: this project works, but its made as a Joke.
