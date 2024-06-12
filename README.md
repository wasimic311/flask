# Report for Assignment 1

## Project chosen

Name: Flask

URL: https://github.com/pallets/flask

Number of lines of code and the tool used to count it: 782430 counted using Lizard

Programming language: Python

## Coverage measurement

### Existing tool

The existing tool used for measuring coverage is coverage.py. It was executed using the following command: coverage run -m pytest


<Show the coverage results provided by the existing tool with a screenshot>

![Coverage.py tool](./images/Coverage.PNG)

### Your own coverage tool

<The following is supposed to be repeated for each group member>

Group member name: Wasim Albarazi

Function 1: 'show_server_banner'

<Show a patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements>
Commit made: https://github.com/pallets/flask/commit/f7549030d395a498cd3e5a9756647d0994f73cfd

<Provide a screenshot of the coverage results output by the instrumentation>

![JSON Dumb file for the results](./images/jsonDumbShow.PNG)
![The coverage before writing a test](./images/showBefore.PNG)



Function 2: 'make_config'

Commit made: https://github.com/pallets/flask/commit/d498fae3aaac40c0b050ae7c1fcda63351977bb9

<Provide a screenshot of the coverage results output by the instrumentation>

![JSON Dumb file for the results](./images/jsonDumbMake.PNG)
![The coverage before writing a test](./images/makeBefore.PNG)

## Coverage improvement

### Individual tests

<The following is supposed to be repeated for each group member>

<Group member name>

<Test 1>

<Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test>

<Provide a screenshot of the old coverage results (the same as you already showed above)>

<Provide a screenshot of the new coverage results>

<State the coverage improvement with a number and elaborate on why the coverage is improved>

<Test 2>

<Provide the same kind of information provided for Test 1>

### Overall

<Provide a screenshot of the old coverage results by running an existing tool (the same as you already showed above)>

<Provide a screenshot of the new coverage results by running the existing tool using all test modifications made by the group>

## Statement of individual contributions

<Write what each group member did>
