# ENPM661 - Project1

#### Project 1 for ENPM661: Planning for Autonomous Robots by Vivek Sood(UID:117504279)
### Description

##### 1. This python script is used to solve any n x n sliding number puzzle(Only tested for 3x3, 4x4, 5x5).
##### 2. The algorithm I have implemented uses a priority queue that optimizes the brute force Breadth First Search (BFS) approach.
##### 3. For example: For testcase5 the code is 25.2 times faster with around 15.3 times fewer iterations when comparing my algorithm with the suggested approach.

### Packages Used
```python
import numpy as np
import time
import copy
import argparse
```
##### Note: Apart from numpy everything else is an inbuilt package
### Usage
##### To run the program
```bash
python3 project1.py --testCase {enter the number of the testcase you need to run}
```
##### For Example: Run the command below to tun testcase number 4

```bash
python3 project1.py --testCase 4
```
##### Note: The code has 8 testcases 5 are the default testcases and I have defined 3 custom testcases
##### To see the generated output file
```bash
cat ./nodePath.txt
```
##### Note!! The output file overwrites the previously present file