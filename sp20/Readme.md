# Notes on how to handle data

# Examples and lectures
## Retrieving data
### Sort
- Sort by student, with each student sorted by time:
  1. Sort by time accessed, increasing (earliest at top)
  2. Sort by student name

### Store
* Two columns
* Headers:
  * Header r1,c1: Module name
  * Header r1,c2: Brief description
  * Header r2,c1: 'Name'
  * Header r2,c2: 'Access time'
* Save as csv to be read by python

## Which data to exclude
* Remove Professor, CCN staff, etc.
* If timestamp is after quiz date, remove row
* Students who did not take a quiz are removed from the count

## How to count hits
* Each timestamp counts a hit
* If two hits are separated by 60 seconds or less, it counts as one hit

# Practice
## Retrieving data
1. Sort by questions correct
2. Sort by student name

## Store
- Four columns
- Headers:
  - Header r0,c0: Module name
  - Header r1,c0: Student name
  - Header r1,c1: SID
  - Header r1,c2: Questions correct
  - Header r1,c3: Questions total
 - Save as csv to be read by Python

## Exclude
- Remove if no finished timestamp