# Report for Assignment 1

## Project chosen

Name: reader

URL: https://github.com/lemon24/reader

Number of lines of code and the tool used to count it: KLOC: 27.236 | tool: lizard

Programming language: python

## Coverage measurement

### Existing tool

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

#### Yves Mangano <br />
##### Function 1 - _is_base64

https://github.com/KubaDomagala/reader/commit/92fcd2ff30c1292d1ed557ab4cf23a8ea9cd9fc6#diff-0b5c7ce5afcc43bab73a6f39f273da57a5f004f1a89da9c8361a84442ee0217d

And

https://github.com/KubaDomagala/reader/commit/d77e6039e13b0425a36f6e1117c047700779896d

<Provide a screenshot of the coverage results output by the instrumentation>

![is_base_64 on own coverage tool](readme_imgs/is_base_64_own_coverage_tool.png)

The coverage tool can be run by using pytest -s tests/test_parser.py
Please note that when the coverage tool is ran with print_coverage_map_content_type()
not being commented out, the results of the base_64 branch coverage tool will be displayed somewhere
in the middle so it might be a little bit hard to find. However, it will show the
exact same output.

---

##### Function 2 - map_content_type
https://github.com/KubaDomagala/reader/commit/92fcd2ff30c1292d1ed557ab4cf23a8ea9cd9fc6#diff-0b5c7ce5afcc43bab73a6f39f273da57a5f004f1a89da9c8361a84442ee0217d

And

https://github.com/KubaDomagala/reader/commit/d77e6039e13b0425a36f6e1117c047700779896d
  
![map_content_type on own coverage tool img1](readme_imgs/map_content_type_own_coverage_tool_1.png)

![map_content_type on own coverage tool img2](readme_imgs/map_content_type_own_coverage_tool_2.png)

The coverage tool can be run by using pytest -s tests/test_parser.py

---

#### Caio Miranda Haschelevici <br />
##### Function 1 - hungarian.py

   <Original cover results:>
   <img src="readme_imgs/header.png"
   alt="Coverage header"
   style="float: left; margin-right: 10px;" />
   <img src="readme_imgs/Hungarian&Greek.png"
   alt="Coverage hungarian and asctime before"
   style="float: left; margin-right: 10px;" />

   <Original code:>
   <img src="readme_imgs/hungarianOriginal1.png"
   alt="hungarian original code 1"
   style="float: left; margin-right: 10px;" />
   <img src="readme_imgs/hungarianOG2.png"
   alt= "hungarian original code 2"
   style="float: left; margin-right: 10px;" />
     
   <Changed code to make coverage tool>
   <img src="readme_imgs/correcthungarian1.png"
   alt="hungarian new code 1"
   style="float: left; margin-right: 10px;" />
   <img src="readme_imgs/newhungarian2.png"
   alt="hungarian new code 2"
   style="float: left; margin-right: 10px;" />
   <img src="readme_imgs/newhungarian3.png"
   alt="hungarian new code 3"
   style="float: left; margin-right: 10px;" />

   <Own coverage tool results with own tests:>
   <img src="readme_imgs/correcthungarianres.png"
   alt="hungarian own test results"
   style="float: left; margin-right: 10px;" />

--- 
##### Function 2 - asctime.py

   <Original cover results:>
   <img src="readme_imgs/header.png"
   alt="Coverage 2 before"
   style="float: left; margin-right: 10px;" />
   <img src="readme_imgs/Hungarian&Greek.png"
   alt="Coverage 2 before"
   style="float: left; margin-right: 10px;" />

   <Original code:>
   <img src="readme_imgs/AsctimeOG1.png"
   alt="asctime original code 1"
   style="float: left; margin-right: 10px;" />
   <img src="readme_imgs/AsctimeOG2.png"
   alt= "asctime original code 2"
   style="float: left; margin-right: 10px;" />

   <Changed code to make coverage tool>
   <img src="readme_imgs/correctAsc1.png"
   alt="asctime new code 1"
   style="float: left; margin-right: 10px;" />
   <img src="readme_imgs/correctAsc2.png"
   alt="asctime new code 2"
   style="float: left; margin-right: 10px;" />
   <img src="readme_imgs/correctAsc3.png"
   alt="asctime new code 3"
   style="float: left; margin-right: 10px;" />

   <Own coverage tool results with own tests:>
   <img src="readme_imgs/correctAscres.png"
   alt="asctime own test results"
   style="float: left; margin-right: 10px;" />

---

#### Kuba Domagala <br />
##### Function 1 - _build_urilib2_request
  
1. Link to the commit with the changed code of the function(_vendor/feedparser/http.py file) - https://github.com/KubaDomagala/reader/commit/108385f001ee1d6462d8b52357b04410e9d40a48#diff-c55ed7a611ef230781c2cab96ac3fb2fba6468e7b2e92d0a9abe2b49f6ebaf08
(The results can also be seen in the commit in the file "_build_urllib2_request_coverage.txt" )
2. Link to the update of the modification - https://github.com/KubaDomagala/reader/commit/ad3b7296bda99e7e16bd29c0651d3bcb7fd29aa7

CODE (BEFORE):
  <img src="readme_imgs/_build_before.png"
     alt="_build_uri before"
     style="float: left; margin-right: 10px;" />

CODE (AFTER): <br />
  <img src="readme_imgs/_build_after_1.png"
   alt="_build_uri after 1"
   style="float: left; margin-right: 10px;" />

  <img src="readme_imgs/_build_after_2.png"
   alt="_build_uri after 2"
   style="float: left; margin-right: 10px;" />

<Provide a screenshot of the coverage results output by the instrumentation>
RESULTS (BEFORE):
  <img src="readme_imgs/coverage_measure_before_tests__build.png"
     alt="_build_uri before"
     style="float: left; margin-right: 10px;" />

RESULTS (FINAL, full results can be seen in a file "_build_urllib2_request_coverage.txt") <br />
  <img src="readme_imgs/_build_urllib2_request_result_cov.png"
     alt="_build_uri final coverage results"
     style="float: left; margin-right: 10px;" />

---

##### Function 2 - setup_logging

1. Link to the 1st commit with the coverage changes - https://github.com/KubaDomagala/reader/commit/189b4a84e784f5feb72056ff9b0a6b2cace8c683 (in the file "src/reader_cli.py")
2. 2nd part of the coverage changes - https://github.com/KubaDomagala/reader/commit/108385f001ee1d6462d8b52357b04410e9d40a48#diff-ae4c294e1304214c4dc7860dfb07bbf702d59f952cf157ea705cf22b1e134244 (in the file in the file "src/reader_cli.py")

CODE (BEFORE):
  <img src="readme_imgs/setup_logging_before_1.png"
     alt="setup_logging code before 1"
     style="float: left; margin-right: 10px;" />

  <img src="readme_imgs/setup_logging_before_2.png"
     alt="setup_logging code before 2"
     style="float: left; margin-right: 10px;" />

CODE (AFTER):
  <img src="readme_imgs/setup_logging_after_1.png"
     alt="setup_logging code after 1"
     style="float: left; margin-right: 10px;" />

  <img src="readme_imgs/setup_logging_after_2.png"
     alt="setup_logging code after 2"
     style="float: left; margin-right: 10px;" />


RESULTS (BEFORE): <br />
  <img src="readme_imgs/coverage_measure_before_tests_logging.png"
     alt="setup_logging coverage before"
     style="float: left; margin-right: 10px;" />

RESULTS (FINAL, full results can be seen in a file "setup_logging_coverage.txt
" + the initial results differ from the screenshot as the tests have been rerun in the different order producing a different initial coverage, which was always < 80%) <br />
  <img src="readme_imgs/setup_logging_results_coverage.png"
     alt="setup_logging final coverage results"
     style="float: left; margin-right: 10px;" />

---

#### Sheng-Wen Chen<br>
##### Function 1 - _parse_poslist()<br><br>

My commitment can be found by clicking this link:
https://github.com/KubaDomagala/reader/commit/ed1d0cf4e1849477d5700d74490750b2d60dd15d

![_parse_poslist coverage tool](readme_imgs/_parse_poslist_COVERAGE_PRINT.png)

The coverage tool for _parse_poslist() is written under the file [src/reader/_vendor/feedparser/namespaces/georss.py](https://github.com/KubaDomagala/reader/blob/coverage-improv-1/src/reader/_vendor/feedparser/namespaces/georss.py), same location of where _parse_poslist() exists in. To run this, simply run the georss.py file from the terminal with the command <code>python3 ./src/reader/_vendor/feedparser/namespaces/georss.py</code>. As it can be seen with my own coverage tool, all of the branches in _parse_poslist() were hit, leading to a coverage percentage of 100%. 

---

##### Function 2 - _parse_date_nate()<br><br>

My commitment can be found by clicking this link:
https://github.com/KubaDomagala/reader/commit/a89c04e040ff6391efdc5a9db8f64e37fcaadd3e
![_parse_poslist coverage tool](readme_imgs/_parse_date_nate_COVERAGE_PRINT.png)

The coverage tool for _parse_date_nate() is written under the file [src/reader/_vendor/feedparser/datetimes/korean.py](https://github.com/KubaDomagala/reader/blob/coverage-improv-1/src/reader/_vendor/feedparser/datetimes/korean.py), same location of where _parse_date_nate() exists in. To run this, simply run the korean.py file from the terminal with the command <code>python3 src/reader/_vendor/feedparser/datetimes/korean.py</code>. As it can be seen with my own coverage tool, all of the branches in _parse_date_nate() were hit, leading to a coverage percentage of 100%. 

## Coverage improvement

### Individual tests

#### Yves Mangano <br />
##### Test 1
  
https://github.com/KubaDomagala/reader/commit/92fcd2ff30c1292d1ed557ab4cf23a8ea9cd9fc6#diff-237d6caeea59e3cf8f303958b4b29e752861048496a047a6af38a12915a02e32

![IMG1 old results](readme_imgs/_is_base64_old_coverage_results.png)

![IMG1 new results](readme_imgs/_is_base64_new_coverage_results_1.png)
![IMG2 new results](readme_imgs/_is_base64_new_coverage_results_2.png)

The coverage for function _is_base64 improved from 0% to 100%. This is because
there were simply no tests made for _is_base64, causing in a branch coverage of 0%.
However, since I have added tests to make sure each branch condition is tested
and accessed, the branch condition went up to 100%. 

---

##### Test 2
https://github.com/KubaDomagala/reader/commit/92fcd2ff30c1292d1ed557ab4cf23a8ea9cd9fc6#diff-237d6caeea59e3cf8f303958b4b29e752861048496a047a6af38a12915a02e32

![IMG1 old results](readme_imgs/map_content_type_old_coverage_results.png)
![IMG1 new results](readme_imgs/map_content_type_new_coverage_results_1.png)
![IMG2 new results](readme_imgs/map_content_type_new_coverage_results_2.png)

The coverage for function map_content_type improved from 0% to 100%. This is because
there were simply no tests made for map_content_type, causing in a branch coverage of 0%.
However, since I have added tests to make sure each branch condition is tested
and accessed, the branch condition went up to 100%. 

---

#### Caio Miranda Haschelevici <br />
##### Test 1 - hungarian.py

   <Original cover results:>
   <img src="readme_imgs/header.png"
   alt="Coverage 2 before"
   style="float: left; margin-right: 10px;" />
   <img src="readme_imgs/Hungarian&Greek.png"
   alt="Coverage 2 before"
   style="float: left; margin-right: 10px;" />

   <New tests:>
   <img src="readme_imgs/newtestshung.png"
   alt="new test for hungarian.py"
   style="float: left; margin-right: 10px;" />
   <New covarage results:>
   <img src="readme_imgs/header.png"
   alt="Coverage 2 before"
   style="float: left; margin-right: 10px;" />
   <img src="readme_imgs/correcthun&ascfinal.png"
   alt="Coverage 2 before"
   style="float: left; margin-right: 10px;" />

Overall we saw an improvement in coverage of 16% the main reason from this can be found when looking at the initial report generated by the coverage tool used. From what it shows the main reason for this low coverage where that the tests used always made the conditions on the if statement always true or false. Therefore, coverage wasnt very high due to the branch conditions not being checked by any individual test. My test checks each branch condition when its true or false thus determining if the branches would work properly during operation. Thus, increasing the coverage by 16%. It is also important to note that the functions coverage didnt increase further due to the inclusion of my own coverage tool into the function. The inclusion of this tool into the function itself caused alot of statements to go unused as they are exclusive statements to my own coverage tool. For example the area with tests for my own coverage tool.

---

##### Test 2 - asctime.py
   <Original cover results:>
   <img src="readme_imgs/header.png"
   alt="Coverage 2 before"
   style="float: left; margin-right: 10px;" />
   <img src="readme_imgs/Hungarian&Greek.png"
   alt="Coverage 2 before"
   style="float: left; margin-right: 10px;" />

   <New tests:>
   <img src="readme_imgs/newtestsasc.png"
   alt="new test for asctime.py"
   style="float: left; margin-right: 10px;" />

   <New covarage results:>
   <img src="readme_imgs/header.png"
   alt="Coverage 2 before"
   style="float: left; margin-right: 10px;" />
   <img src="readme_imgs/correcthun&ascfinal.png"
   alt="Coverage 2 before"
   style="float: left; margin-right: 10px;" />

   Overall we saw an improvement in coverage of 17%, we saw this improvements because of a similar reason as the previous test. Just like in the previous case we had a low initial coverage because certain branches where either always true or always false with the pre-exisiting tests. However, the tests I added ensure that either case of every branch is tested and therefore we had an increase in the overall coverage of this function by 17%. Just like in the rpevious test case, it is important to note that due to the inclusion of my own coverage tool into the function, the coverage wasnt able to be higher. This is due to the fact that certain areas of the code where exclusive to my coverage tool and therefore not tested. Thus, hampering the overall coverage

---

#### Kuba Domagala <br />
##### Test 1 - _build_urilib2_request
  
1. Link to the commit with added tests - https://github.com/KubaDomagala/reader/commit/108385f001ee1d6462d8b52357b04410e9d40a48#diff-371d71686903901ab120e582d2ca811179700201f7652353fdc03bc9f0fb9240 (in the file "tests/test_reader__vendor_feedparser_urls.py", function "test_build_urllib2_request()")
2.https://github.com/KubaDomagala/reader/commit/92fcd2ff30c1292d1ed557ab4cf23a8ea9cd9fc6#diff-237d6caeea59e3cf8f303958b4b29e752861048496a047a6af38a12915a02e32

BEFORE (function itself):
  <img src="readme_imgs/_build_coverage_before_official.png"
     alt="_build_uri coverage before official"
     style="float: left; margin-right: 10px;" />

(function coverage %)
  <img src="readme_imgs/_build_before_fun.png"
     alt="_build_uri coverage before official fun"
     style="float: left; margin-right: 10px;" />

(file coverage %) <br />
  <img src="readme_imgs/_build_before_file.png"
     alt="_build_uri coverage before official file"
     style="float: left; margin-right: 10px;" />

AFTER (function itself):
  <img src="readme_imgs/_build_coverage_after_official.png"
     alt="_build_uri coverage after official"
     style="float: left; margin-right: 10px;" />

(function coverage %)
  <img src="readme_imgs/_build_after_fun.png"
     alt="_build_uri coverage after official fun"
     style="float: left; margin-right: 10px;" />

(file coverage %)
  <img src="readme_imgs/_build_after_file.png"
     alt="_build_uri coverage after official file"
     style="float: left; margin-right: 10px;" />

The coverage of the function has improved from 0% to 100% in both code and branch coverage. This is because no tests have existed for that specific function and no already existing test used the functionality of that function. The coverage has improved as I added extensive tests that check every branch for that function that have not existed before.

---

##### Test 2 - setup_logging
1. Link to the commit with added tests https://github.com/KubaDomagala/reader/commit/189b4a84e784f5feb72056ff9b0a6b2cace8c683#diff-4e8715c7a425ee52e74b7df4d34efd32e8c92f3e60bd51bc2e1ad5943b82032e (in the file "tests/test_cli.py" function "test_cli_setup_logging")
2. modification here (same file and function) - https://github.com/KubaDomagala/reader/commit/108385f001ee1d6462d8b52357b04410e9d40a48#diff-4e8715c7a425ee52e74b7df4d34efd32e8c92f3e60bd51bc2e1ad5943b82032e

BEFORE (function ifself:)
  <img src="readme_imgs/setup_logging_before_official.png"
     alt="setup_logging before official"
     style="float: left; margin-right: 10px;" />

(function coverage %)
  <img src="readme_imgs/setup_before_fun.png"
     alt="setup_logging before official fun"
     style="float: left; margin-right: 10px;" />

(file coverage %) <br />
  <img src="readme_imgs/setup_before_file.png"
     alt="setup_logging before official file"
     style="float: left; margin-right: 10px;" />

<Provide a screenshot of the new coverage results>
  AFTER (function itself):
  <img src="readme_imgs/setup_logging_cov_after_official.png"
     alt="setup_logging coverage after official"
     style="float: left; margin-right: 10px;" />

(function coverage %)
  <img src="readme_imgs/setup_after_fun.png"
     alt="setup_logging after official fun"
     style="float: left; margin-right: 10px;" />

(file coverage %) <br />
  <img src="readme_imgs/setup_after_file.png"
     alt="setup_logging after official file"
     style="float: left; margin-right: 10px;" />

The coverage of the function has improved from 60% to 100% (branch coverage) and from 65% to 100% (code coverage)

---

#### Sheng-Wen Chen<br>
##### Test 1 georss.py
![_parse_poslist old coverage](readme_imgs/_parse_poslist_OLD_COVERAGE.png)
![_parse_poslist old coverage %](readme_imgs/_parse_poslist_OLD_COVERAGE_PERC.png)
![_parse_poslist new coverage](readme_imgs/_parse_poslist_NEW_COVERAGE.png)
![_parse_poslist new coverage %](readme_imgs/_parse_poslist_NEW_COVERAGE_PERC.png)

Overall the coverage percentage increased from 0% t0 100%.
The coverage percentage of _parse_poslist() was initially only 0%, meaing that it wasn't even tested in its original file. After building a tests for _parse_poslist(), all of the branches were hit, and the coverage percentage increased to 100%. 

---

##### Test 2 korean.py
![_parse_poslist old coverage](readme_imgs/_parse_date_nate_OLD_COVERAGE.png)
![_parse_poslist old coverage %](readme_imgs/_parse_date_nate_OLD_COVERAGE_PERC.png)
![_parse_poslist new coverage](readme_imgs/_parse_date_nate_NEW_COVERAGE.png)
![_parse_poslist new coverage %](readme_imgs/_parse_date_nate_NEW_COVERAGE_PERC.png)

Overall the coverage percentage increased from 0% to 88%.
The coverage percentage of _parse_date_nate() was initially only 0%, meaing that it wasn't even tested in its original file. After building a tests for _parse_date_nate(), all of the branches were hit, and the coverage percentage increased to 88%. 


### Overall

<Provide a screenshot of the old coverage results by running an existing tool (the same as you already showed above)>

<Provide a screenshot of the new coverage results by running the existing tool using all test modifications made by the group>

## Statement of individual contributions

### Yves Mangano

I worked on the functions _is_base64 and map_content_type. I made my own coverage
tool where the branch coverage can be shown by running pytest -s tests/test_parser.py

I increased the branch coverage from 0% to 100% in these functions, enhancing 
the overall coverage of the project, by creating my own tests in test_parser.py
making sure that each branch is accessed and functions correctly by using 
assert statements inside of the tests.

I've contributed also in our team by helping understand how the project works
and how we can run the inbuilt coverage (coverage.py) not only by using "tox" but
also "./run.sh coverage-all", and I've provided an example of the tests I've made 
for my teammates to help understand how they can test their functions.
Especially since _is_base64 function is a method from a class, it is harder to test, 
but I managed how to and set an example for the group doing this.

---

### Kuba Domagala
I worked on the functions _build_urilib2_request and setup_logging. I made my own coverage tool where the branch coverage can be shown by opening the respective files created in the main root of the project (first entry is the before the added tests, everything else is after).

I increased the coverage of these functions to 100% in their respective files, enhancing the coverage of the project and making sure that all of the branches are accessed and their results are as expected.

Additionally I was responsible for merging all of the pull requests and general organisation of the work. I was the one who found the repository that we are using in the assingment and made sure that everyone was able to run things correctly, so that we could start working.

---

### Sheng-Wen Chen

I worked on the functions _parse_poslist() and _parse_nate_date(). I made my own coverage tools where the branch coverage can be shown by running the commands <code>python3 ./src/reader/_vendor/feedparser/namespaces/georss.py</code> and <code>python3 src/reader/_vendor/feedparser/datetimes/korean.py</code>.

I increased the branch coverage of _parse_poslist() from 0% to 100%, and the branch coverage of _parse_nate_date() from 0% to 88% enhancing the overall coverage of the project. This was done by creating my own tests in test_parser.py, making sure that each branch is accessed and functions correctly by using assert statements inside of the tests. One of the branche wasn't able to reach after running <code>tox</code>.

Additionally, I was responsible for ensuring the group project was heading in the right direction. For instance, we didn't know that we needed to add an external "else" statement after an "if" statement that did not end with a return, while making the coverage tool. I managed to find this missing implementation and adjusted the working direction of the group.
