# HTTP access log parse

The purpose of the project is to parse a NASA access log file in order to perform various analysis tasks, the tasks are the following:

1. Top 10 requested pages and the number of requests made for each
2. Percentage of successful requests (anything in the 200s and 300s range)
3. Percentage of unsuccessful requests (anything that is not in the 200s or 300s range)
4. Top 10 unsuccessful page requests
5. The top 10 hosts making the most requests, displaying the IP address and number of requests made.
6. Option parsing to produce only the report for one of the previous points (e.g. only the top 10 urls, only the percentage of successful requests and so on)
7. A README file explaining how to use the tool, what its dependencies and any assumptions you made while writing it

Extra points will be given for:

1. Tests
2. For each of the top 10 hosts, show the top 5 pages requested and the number of requests for each

Notes
    * You can use any programming language that you feel more comfortable with
    * The log file contains malformed entries; for each malformed line, display an error message and the line number.
    * You can use Algorithms and Data structures provided by the standard library of the programming language you use, or create your own

### Prerequisites

I choose to use Python as a programming language for this project which leverages use of Pandas library.

```
sudo apt install python3-pip
```

In my local machine the python version is Python 3.6.9

```
python3 --version
```

 Make sure that you have access to Pandas library.


### Running the tests

Some unit tests implemented, in order to assure the quality of the code. The tests use the unittest Python library.
In order to run the tests run the following statement:

```
python3 tests.py
```

Make sure that the tests ran successfully.

### Running the code

In order to run the actual analysis code, run the following statement in console:

```
python3 exercise.py
```

### Critical points for consideration

1) What is a web page and what is a simple request. From our email communication, I made an assumption on what is a web page and what is not.
   Web page is a request that include either .html or no dot(.) at all.

   E.g. The following examples are all defined as page requests:

   ```
   GET /ksc.html
   GET /shuttle/missions/sts-69/news
   GET /
   ```

   On the contrary, the below examples are defined as requests:

   ```
   GET /history/apollo/images/footprint-small.gif
   GET /htbin/cdt_main.pl
   ```


2) Another assumption is that the string "HTTP/1.0" removed from the request column, to simplify the process on how we decide a web page or a simple request.

3) Remove the columns date, size (4th and 8th column) from the initial data set which were not mandatory for my analysis (as described in the requirements).

4) When we have less than 10 results in the final data frame/table, then I assume that we want to show all the rows that have actual values.
   E.g.
   0           /page1      3
   1  /dashboard.html      2
   2           /login      1
   3       /login/gfd      1
   4          /logout      1

   And not fill the remaining columns with NaN and None respectively until we reach 10 results.
