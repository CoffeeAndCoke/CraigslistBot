## Synopsis

This script takes a craigslist URL as a command line parameter and emails the top 5 most recent posts. It’s a the beginning of a bot with smarter features being added.

## Example

The script will read in the austin.craigslist.org/search/sof URL and output the following:

```
	Time Posted: 2017-01-05 09:30:00
	Title: Tech Startup Looking for Veterans: Up to $300 for 3-5 hours of work

	Time Posted: 2017-01-04 15:34:00
	Title: 100% remote Node.js developer - full time with benefits

	Time Posted: 2017-01-03 18:50:00
	Title: Job Opening: Hiring a Senior Physical Design Engineer

	Time Posted: 2017-01-03 18:11:00
	Title: Web and Mobile Software Developer

	Time Posted: 2017-01-03 12:11:00
	Title: Data Analyst - Sales Operations Analyst, Global Org
```

## Compile and Run 

Version: Python 2.7.10

EXAMPLE:
```
	python craigslistbot.py http://austin.craigslist.org/search/sof
```
## Author

Edgar Jaimes
