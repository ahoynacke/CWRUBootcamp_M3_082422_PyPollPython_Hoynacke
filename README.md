# CWRUBootcamp_M3_082422_PyPollPython_Hoynacke
# Election Analysis

## Project Overview 
I have been given the task of completing an election audit of a recant local congressional election. 

I was asked to do the following:
1. Get a complete list of candidates who received votes.
2. Calculate the following:
  a. total number of votes cast
  b. total number of votes each candidate received 
  c. percent of votes each candidate won 
3. Determine who won.

## Resources 

Data Source: election_results.csv
Software: Python, Visual Studio Code

## Summary 
The analysis of the election shows that:
- There were 369,711 votes cast in total.
- The candidates who ran were: 
  1. Charles Casper Stockham
  2. Diana DeGette
  3. Raymon Anthony Doane
- The results were: 
  - Charles Casper Stockham received 23.0% of the votes (85,213)
  - Diana DeGette received 73.8% of the votes (272,892)
  - Raymon Anthony Doane received 3.1% of the votes (11,606)
- The winner was Diana Degette with 272,892 votes.

## Software output: 

<img width="330" alt="Screen Shot 2022-08-29 at 4 09 24 PM" src="https://user-images.githubusercontent.com/111096384/187289184-49ee6144-6fa6-4d62-8851-0824adc17d85.png">

## Written Analysis of the Election Audit
### Overview of Election Audit 
I have been given the task by a Board of Elections employee to complete an election audit of a recent local congressional election. 

I was asked to do the following:
1. Get a complete list of candidates who received votes.
2. Calculate the following:
  a. total number of votes cast
  b. total number of votes each candidate received 
  c. percent of votes each candidate won 
3. Determine who won.

In order to correctly execute the above tasks, I used a technique called pseudocode. This breaks down the information needed in an easily digestible way. 
For this project my final python script will include: 
1. Total number of votes cast. 
2. Total number of votes and percentage of votes by county.
3. County with the largest turnout of voters. 
4. Percentage of votes each candidate won. 
5. The winner of the election, their vote count and winning percentage

### Election Audit Results 
- How many votes were cast in this congressional election?

    Total Votes: 369,711
  
- Provide a breakdown of the number of votes and the percentage of total votes for   each county in the precinct.

    County Votes:
      Jefferson: 10.5% (38,855) 
      Denver: 82.8% (306,055)
      Arapahoe: 6.7% (24,801)

- Which county had the largest number of votes?

    County with largest turnout: Denver
  
- Provide a breakdown of the number of votes and the percentage of the total votes   each candidate received.

    Percentage of votes each candidate won:
      Charles Casper Stockham: 23.0% (85,213)
      Diana DeGette: 73.8% (272,892)
      Raymon Anthony Doane: 3.1% (11,606)
    
- Which candidate won the election, what was their vote count, and what was their     percentage of the total votes?
 
    Winner: Diana DeGette
    Winning Vote Count: 272,892
    Winning Percentage: 73.8%
    
<img width="587" alt="Screen Shot 2022-08-31 at 11 35 23 AM" src="https://user-images.githubusercontent.com/111096384/187721968-cd444f77-cbfc-442d-b5f1-eda7266624a4.png">

  
### Election-Audit Summary: In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. Give at least two examples of how this script can be modified to be used for other elections.

Moving forward this script can be utilized to provide a clean report of election data. The report can be editing and customized for all elections moving forward. The script can be adjusted for locations and number of candidates. This script provides a template that will give the user the following: 
  1. Total number of votes cast. 
  2. Total number of votes and percentage of votes by county or your locations of choice 
  3. County (Locations) with the largest turnout of voters. 
  4. Percentage of votes each candidate won. 
  5. The winner of the election, their vote count and winning percentage
