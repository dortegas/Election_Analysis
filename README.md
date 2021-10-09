# Election Analysis

## Project Overview
We worked together with Tom on the auditory and analysis of elections results for the US Congressional precinct in Colorado. Tom is an employee of the Colorado Board of Elections. Our tasks were following to complete the analysis:

1. Calculate the total numbers of votes cast.
2. The voter turnout for each county.
3. The percentage of votes from each county out of the total count.
4. The county with the highest turnout.
5. Get a complete list of candidates who received votes.
6. Calculate the total number of votes each candidate received.
7. Calculate the percentage of votes each candidate won.
8. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.9.7 and Visual Studio Code 1.61.0 for Windows

## Election-Audit Results
The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The counties were:
    - Jefferson
    - Denver
    - Arapahoe  
- The votes by counties were:
    - In Jefferson, the turnout was 38,855 votes which represent 10.5%
    - In Denver, the turnout was 306,055 votes which represent 82.8%
    - In Arapahoe, the turnout was 24,801 votes which represent 6.7%
- The county with the highest turnout was **Denver**
 - The candidates were:
    - Diana DeGette
    - Charles Casper Stockham
    - Raymon Anthony Doane
- The candidate results were:
    - Diana DeGette received 73.8% of the vote and 272,892 number of votes
    - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes
- The winner of the election was:
    - **Diana DeGette**, who received 73.8% of the vote and 272,892 number of votes

## Summary
The audit automated with code Python was successful for the US Congressional precinct in Colorado. We could establish that the solution could work in other congressional district elections, also in senatorial local and district elections.

To this solution works, we must consider the following:

1.	The voting methods (mail-in ballots, punch cards, and DRE) should concentrate the results in a tabular model into a CSV format file.
2.	The CSV files must follow the format of columns: Ballot ID, County, and Candidate.
3.  Adjust the path according to the local file system where the CSV file with the election results is. (line 9 in the code block Python).
4.	Adjust the path according to the local file system where the audit results will save in a text file (line 12 in the code block Python).
