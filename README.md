# ENPM661 - Project1

Project 1 for ENPM661: Planning for Autonomous Robots by Vivek Sood(UID:117504279)
### Description

1. This python script is used to solve a n x n
sliding number puzzle.
1. The algorithm I have implemented uses a priority
queue that optimizes the brute force BFS approach.
1. For example: For testcase5 the code is 25.2 times
faster with around 15.3 times fewer iterations.
1. Additional testcases are present in the file to test the efficiency of the implemented solution

### Packages Used
```python
import numpy as np
import time
import copy
```
##### Note: Apart from numpy everything else is an inbuilt package
### Usage
##### To run the program
```bash
python3 project1.py
```
##### To see the generated output file
```bash
cat ./nodePath.txt
```
##### To change the test-case
```bash
1. Go to the main() block (line no. 234 onwards)
2. Un-comment the code block of the testcase you want to run.
3. Comment the code block of the testcase that was Un-commented before. 