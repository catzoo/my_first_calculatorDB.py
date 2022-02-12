# my_first_calculatorDB.py
I found [my_first_calculator.py](https://github.com/AceLewis/my_first_calculator.py) made by [AceLewis](https://github.com/AceLewis). The project is neat,
it can calculate any value between 0 and 50. But I didn't like that limit and if you attempt to expand to 1000, it would crash. So, I came up with an idea of about making a SQLite database to keep all those values.

This calculator is an improvement from `my_first_calculator.py` to where it accepts negatives and decimals to find the answer. The current `calc.db` file only accept values from -200 to 200 (no decimal), if you want to expand this you can regenerate the file.

## generate.py
This script generates the database and accept decimals as well. Just note, generating with decimals would make the file big. I generated the DB from `-250.0` to `250.9` and made a file that is over 3 GB big.

If you want to regenerate the DB, here are the current settings you can mess with.
| Setting | Description | Example |
| :---: | :--- | :---: |
| Min Value | The minimum value to support | -50 |
| Max Value | The maximum value to support. With decimals this would increase it by .9 | 50 |
| Step | For loop stepping value | 0.1 |

The example values would generate a DB from `-50.0` to `-50.9`

------------------------
###### Note: this project works, but its made as a Joke.
