# Log Analysis

## Description
This Project consists code for running log analysis for Udacity Project.

It analyses large data from the tables. It gives output according to given question through proper formulation of query. All the computation is done by Database through single query using join.

newdata.sql consists all the required data to be analysed.

The database consist of three table
* authors
* articles
* log

##Running
#### Step 1
* make sure you have ```newsdata.sql``` in the same folder
#### Step 2
* Add data to database, you must create news database name 'news' before executing command

Run
```Shell
psql -d news -f newsdata.sql
```
#### Step 3
Run the script
```Shell
python main.py
```

You will get result on your terminal
