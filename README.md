# Report for Assignment 1

## Project chosen

Name: reader

URL: https://github.com/lemon24/reader

Number of lines of code and the tool used to count it: KLOC: 27.236 | tool: lizard

Programming language: python

## Coverage measurement

### Existing tool

<Inform the name of the existing tool that was executed and how it was executed>
Tool: tox + coverage.py <br />
Usage: The tool was used by following the guide on the contribute page of the project. We set up the development environment and run "tox" command, which run the full test suite using coverage.py. We found the result under "htmlcov/index.html" file name, which generated a file with the coverage (it can also be found in the terminal, however the html file is easier to read).

<Show the coverage results provided by the existing tool with a screenshot>
  <img src="readme_imgs/coverage_tool_run_1.png"
     alt="Coverage 1 before"
     style="float: left; margin-right: 10px;" />
  (tests in between that were skipped in the screenshots)
  <img src="readme_imgs/coverage_tool_run_2.png"
   alt="Coverage 2 before"
   style="float: left; margin-right: 10px;" />

### Your own coverage tool

<The following is supposed to be repeated for each group member>

<Group member name>
Group 69 - Sheng-Wen Chen<br>
Function 1 - _parse_poslist()<br><br>

My commitment can be found by clicking this link:
https://github.com/KubaDomagala/reader/commit/ed1d0cf4e1849477d5700d74490750b2d60dd15d

![_parse_poslist coverage tool](readme_imgs/_parse_poslist_COVERAGE_PRINT.png)

The coverage tool for _parse_poslist() is written under the file [src/reader/_vendor/feedparser/namespaces/georss.py](https://github.com/KubaDomagala/reader/blob/coverage-improv-1/src/reader/_vendor/feedparser/namespaces/georss.py), same location of where _parse_poslist() exists in. To run this, simply run the georss.py file from the terminal with the command <code>python3 ./src/reader/_vendor/feedparser/namespaces/georss.py</code>. As it can be seen with my own coverage tool, all of the branches in _parse_poslist() were hit, leading to a coverage percentage of 100%. 

Function 2 - _parse_date_nate()<br><br>

My commitment can be found by clicking this link:
https://github.com/KubaDomagala/reader/commit/a89c04e040ff6391efdc5a9db8f64e37fcaadd3e
![_parse_poslist coverage tool](readme_imgs/_parse_date_nate_COVERAGE_PRINT.png)

The coverage tool for _parse_date_nate() is written under the file [src/reader/_vendor/feedparser/datetimes/korean.py](https://github.com/KubaDomagala/reader/blob/coverage-improv-1/src/reader/_vendor/feedparser/datetimes/korean.py), same location of where _parse_date_nate() exists in. To run this, simply run the korean.py file from the terminal with the command <code>python3 src/reader/_vendor/feedparser/datetimes/korean.py</code>. As it can be seen with my own coverage tool, all of the branches in _parse_date_nate() were hit, leading to a coverage percentage of 100%. 


## Coverage improvement

### Individual tests
Group 69 - Sheng-Wen Chen<br>

Function 1 - _parse_poslist()<br><br>
<Test 1>georss.py
![_parse_poslist old coverage](readme_imgs/_parse_poslist_OLD_COVERAGE.png)
![_parse_poslist old coverage %](readme_imgs/_parse_poslist_OLD_COVERAGE_PERC.png)
![_parse_poslist new coverage](readme_imgs/_parse_poslist_NEW_COVERAGE.png)
![_parse_poslist new coverage %](readme_imgs/_parse_poslist_NEW_COVERAGE_PERC.png)

Overall the coverage percentage increased from 0% t0 100%.
The coverage percentage of _parse_poslist() was initially only 0%, meaing that it wasn't even tested in its original file. After building a tests for _parse_poslist(), all of the branches were hit, and the coverage percentage increased to 100%. 


<Test 2>korean.py
![_parse_poslist old coverage](readme_imgs/_parse_date_nate_OLD_COVERAGE.png)
![_parse_poslist old coverage %](readme_imgs/_parse_date_nate_OLD_COVERAGE_PERC.png)
![_parse_poslist new coverage](readme_imgs/_parse_date_nate_NEW_COVERAGE.png)
![_parse_poslist new coverage %](readme_imgs/_parse_date_nate_NEW_COVERAGE_PERC.png)

Overall the coverage percentage increased from 0% to 88%.
The coverage percentage of _parse_date_nate() was initially only 0%, meaing that it wasn't even tested in its original file. After building a tests for _parse_date_nate(), all of the branches were hit, and the coverage percentage increased to 88%.  

## Statement of individual contributions
Group 69 - Sheng-Wen Chen<br>

I worked on the functions _parse_poslist() and _parse_nate_date(). I made my own coverage tools where the branch coverage can be shown by running the commands <code>python3 ./src/reader/_vendor/feedparser/namespaces/georss.py</code> and <code>python3 src/reader/_vendor/feedparser/datetimes/korean.py</code>.

I increased the branch coverage of _parse_poslist() from 0% to 100%, and the branch coverage of _parse_nate_date() from 0% to 88% enhancing the overall coverage of the project. This was done by creating my own tests in test_parser.py, making sure that each branch is accessed and functions correctly by using assert statements inside of the tests. One of the branche wasn't able to reach after running <code>tox</code>.

Additionally, I was responsible for ensuring the group project was heading in the right direction. For instance, we didn't know that we needed to add an external "else" statement after an "if" statement that did not end with a return, while making the coverage tool. I managed to find this missing implementation and adjusted the working direction of the group.

