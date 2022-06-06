# CT

Programming Test

Make a program in your favorite language/environment that takes two inputs:

 • a set of include intervals
 • a set of exclude intervals

The sets of intervals can be given in any order, and they may be empty or overlapping.

The program should output the result of taking all the includes and “remove” the excludes.

The output should be given as non-overlapping intervals in a sorted order.

Intervals will contain integers only.

Example 1:

Includes: 10-100
Excludes: 20-30

Output should be: 10-19, 31-100

Example 2:
Includes: 50-5000, 10-100
Excludes: (none)
Output: 10-5000

Example 3:
Includes: 10-100, 200-300
Excludes: 95-205
Output: 10-94,206-300

Example 4:
Includes: 10-100, 200-300, 400-500
Excludes: 95-205, 410-420
Output: 10-94, 206-300, 400-409, 421-500

Example 5:
Includes: 5-13, 2-8
Excludes: 4-10, 5-11
Output: 2-3, 12-13

Example 6:
Includes: 5-100000000
Excludes: 4-5
Output: 6-100000000

The program does not need to behave in any particular way if invalid intervals are entered.
The program does not need to have any mechanism for ending the program.
The code for entering and printing out data is not important.  
We don't need a user interface for entering the data, all the data can be hardcoded into the program. 