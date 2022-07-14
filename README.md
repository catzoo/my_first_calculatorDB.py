# my_first_calculatorDB.py
I found [my_first_calculator.py](https://github.com/AceLewis/my_first_calculator.py) made by [AceLewis](https://github.com/AceLewis). The project is neat,
it can calculate any value between 0 and 50. But I didn't like that limit and if you go to larger numbers, it'll crash. I believe the highest the project went is 0-1000. I also wanted it to support decimals. So, I came up with an idea of about making a SQLite database to keep all those values.

This calculator is an improvement from `my_first_calculator.py`, it works in a similar way only it queries the database for an answer. Since its using a database it can expand to larger values without crashing. Only downside is its SQLite, if its too big then it'll take longer to query. 
Future plans are to move this towards PostgreSQL. 

The current `calc.db` file only accept values from -200 to 200, if you want to expand this you can regenerate the file.

## generate.py
This script generates the database and accept decimals as well. Just note, generating with decimals would make the file big. I generated the DB from `-250.0` to `250.9` and made a file that is over 3 GB big.

If you want to regenerate the DB, here are the current settings you can mess with.
| Setting | Description | Example |
| :---: | :--- | :---: |
| Min Value | The minimum value to support | -50 |
| Max Value | The maximum value to support. With decimals this would increase it by .9 | 50 |
| Step | For loop stepping value | 0.1 |

The example values would generate a DB from `-50.0` to `50.9`
