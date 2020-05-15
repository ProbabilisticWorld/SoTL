# Notes on how to handle data

## Retrieving data
### Sort
Sort by student, with each student sorted by time:
1. Sort by time accessed, increasing (earliest at top)
2. Sort by student name

### Store
* Two columns
* Headers:
  * Header r1,c1: Module name
  * Header r1,c2: Brief description
  * Header r2,c1: Name
  * Header r2,c2: Access time
* Save as csv to be read by python

## Which data to exclude
* If timestamp is after quiz date, exclude

## How to count hits
* Each timestamp counts a hit
* If two hits are separated by 60 seconds or less, it counts as one hit
