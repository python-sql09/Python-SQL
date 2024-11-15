Why Python for Data Analysis?
-----------------------------
For many people, the Python programming language has strong appeal. 
Since its first appearance in 1991, Python has become one of 
the most popular interpreted programming languages, along with Perl, 
Ruby, and others. Python and Ruby have become especially popular since 
2005 or so for building websites using their numerous web frameworks, 
like Rails (Ruby) and Django (Python). Such languages are often called 
scripting languages, as they can be used to quickly write small programs,
or scripts to automate other tasks. I don’t like the term “scripting 
language, ” as it carries a connotation that they cannot be used for
building serious software. Among interpreted languages, for various 
historical and cultural reasons, Python has developed a large and active 
scientific computing and data analysis community. NumPy NumPy, short for 
Numerical Python, has long been a cornerstone of numerical computing in 
Python.  It provides the data structures, algorithms, and library glue 
needed for most scientific applications involving numerical data in 
Python. NumPy contains, among other things: 
A fast and efficient multidimensional array object ndarray Functions 
for performing element-wise computations with arrays or mathematical 
operations between arrays Tools for reading and writing array-based 
datasets to disk Linear algebra operations, Fourier transform, and 
random number generation A mature C API to enable Python extensions 
and native C or C++ code to access NumPy’s data structures and 
computational facilities. 
In the last 10 years, Python has gone from a bleeding-edge 
or “at your own risk” scientific computing language to one of the most 
important languages for data science, machine learning, and general 
software development in academia and industry. 
For data analysis and interactive computing and data visualization, 
Python will inevitably draw comparisons with other open source and 
commercial programming languages and tools in wide use, such as R, 
MATLAB, SAS, Stata, and others. 
In recent years, Python’s improved support for libraries 
(such as pandas and scikit-learn) has made it a popular choice for
data analysis tasks. Combined with Python’s overall strength for 
general-purpose software engineering, it is an excellent option as 
a primary language for building data applications.

Python as Glue:
---------------
Part of Python’s success in scientific computing is the ease of 
integrating C, C++, and FORTRAN code. Most modern computing environments
share a similar set of legacy FORTRAN and C libraries for doing linear 
algebra, optimization, integration, fast Fourier transforms, and other 
such algorithms. The same story has held true for many companies and 
national labs that have used Python to glue together decades’ worth of 
legacy software.

Solving the “Two-Language” Problem:
-----------------------------------
In many organizations, it is common to research, prototype, and test new
ideas using a more specialized computing language like SAS or R and then
later port those ideas to be part of a larger production system written 
in, say,Java, C#, or C++. What people are increasingly finding is that 
Python is a suitable language not only for doing research and 
prototyping but also for building the production systems.

Why maintain two development environments when one will suffice? 
I believe that more and more companies will go down this path, as 
there are often significant organizational benefits to having both 
researchers and software engineers using the same set of programming 
tools.

NumPy:
-----
NumPy, short for Numerical Python, has long been a cornerstone of
numerical computing in Python. It provides the data structures, 
algorithms, and library glue needed for most scientific applications 
involving numerical data in Python. NumPy contains, among other things:
* A fast and efficient multidimensional array object ndarray
* Functions for performing element-wise computations with arrays or
  mathematical operations between arrays
* Tools for reading and writing array-based datasets to disk
* Linear algebra operations, Fourier transform, and random number
  generation
* A mature C API to enable Python extensions and native C or C++ code
  to access NumPy’s data structures and computational facilities

pandas:
-------
pandas provides high-level data structures and functions designed to 
make working with structured or tabular data fast, easy, and expressive. 
Since its emergence in 2010, it has helped enable Python to be a 
powerful and productive data analysis environment. The primary objects 
in pandas that will be used in this book are the DataFrame, a tabular, 
column-oriented data structure with both row and column labels, and the 
Series, a one-dimensional labeled array object.

As a bit of background, I started building pandas in early 2008 during 
my tenure at AQR Capital Management, a quantitative investment 
management firm. At the time, I had a distinct set of requirements that 
were not well addressed by any single tool at my disposal:
* Data structures with labeled axes supporting automatic or explicit 
  data alignment — this prevents common errors resulting from misaligned
  data and working with differently indexed data coming from different
  sources
* Integrated time series functionality
* The same data structures handle both time series data and non–time
  series data
* Arithmetic operations and reductions that preserve metadata
* Flexible handling of missing 
* Merge and other relational operations found in popular databases 
  (SQL-based, for example)

matplotlib
----------
matplotlib is the most popular Python library for producing plots and 
other two-dimensional data visualizations. It was originally created by 
John D.Hunter and is now maintained by a large team of developers. It is 
designed for creating plots suitable for publication. While there are 
other visualization libraries available to Python programmers, 
matplotlib is the most widely used and as such has generally good 
integration with the rest of the ecosystem. I think it is a safe choice 
as a default visualization tool.

SciPy:
------
SciPy is a collection of packages addressing a number of different 
standard problem domains in scientific computing. Here is a sampling 
of the packages included:
scipy.integrate:
----------------
Numerical integration routines and differential equation solvers
scipy.linalg
------------
Linear algebra routines and matrix decompositions extending beyond
those provided in numpy.linalg
scipy.optimize:
--------------
Function optimizers (minimizers) and root finding algorithms
scipy.signal:
-------------
Signal processing tools
scipy.sparse:
-------------
Sparse matrices and sparse linear system solvers
scipy.special:
--------------
Wrapper around SPECFUN, a Fortran library implementing many
common mathematical functions, such as the gamma function
scipy.stats:
------------
Standard continuous and discrete probability distributions (density
functions, samplers, continuous distribution functions), various
statistical tests, and more descriptive statistics.
Together NumPy and SciPy form a reasonably complete and mature
computational foundation for many traditional scientific computing
applications.

scikit-learn:
-------------
Since the project’s inception in 2010, scikit-learn has become the 
premier general-purpose machine learning toolkit for Python programmers. 
In just seven years, it has had over 1,500 contributors from around the 
world. It includes submodules for such models as:
* Classification: SVM, nearest neighbors, random forest, logistic
  regression, etc.
* Regression: Lasso, ridge regression, etc.
* Clustering: k-means, spectral clustering, etc.
* Dimensionality reduction: PCA, feature selection, matrix factorization,
  etc.
* Model selection: Grid search, cross-validation, metrics
* Preprocessing: Feature extraction, normalization

statsmodels:
------------
statsmodels is a statistical analysis package that was seeded by work 
from Stanford University statistics professor Jonathan Taylor, who 
implemented a number of regression analysis models popular in the R 
programming language.
Compared with scikit-learn, statsmodels contains algorithms for classical
(primarily frequentist) statistics and econometrics. This includes such
submodules as:
* Regression models: Linear regression, generalized linear models, robust
  linear models, linear mixed effects models, etc.
* Analysis of variance (ANOVA)
* Time series analysis: AR, ARMA, ARIMA, VAR, and other models
* Nonparametric methods: Kernel density estimation, kernel regression
  Visualization of statistical model results

Installing or Updating Python Packages:
* conda install package_name
* pip install package_name
* conda update package_name
* pip install --upgrade package_name

Standard IPython keyboard shortcuts-Keyboard shortcutDescription:
-----------------------------------------------------------------
Ctrl-P or up-
arrowSearch backward in command history for commands starting with
currently entered text
Ctrl-N or down-
arrowSearch forward in command history for commands starting with
currently entered text
Ctrl-RReadline-style reverse history search (partial matching)
Ctrl-Shift-VPaste text from clipboard
Ctrl-CInterrupt currently executing code
Ctrl-AMove cursor to beginning of line
Ctrl-EMove cursor to end of line
Ctrl-KDelete text from cursor until end of line
Ctrl-UDiscard all text on current line
Ctrl-FMove cursor forward one characterCtrl-BMove cursor back one character
Ctrl-LClear screen

Magic:
------
A magic command is any command prefixed by the percent symbol %. 
For example, you can check the execution time of any Python statement, 
such as a matrix multiplication, using the %timeit magic function

Some frequently used IPython magic commands - Command Description:
------------------------------------------------------------------
%quickref - Display the IPython Quick Reference Card
%magic - Display detailed documentation for all of the available magic commands
%debug - Enter the interactive debugger at the bottom of the last exception traceback
%hist - Print command input (and optionally output) history
%pdb - Automatically enter debugger after any exception
%paste - Execute preformatted Python code from clipboard
%cpaste - Open a special prompt for manually pasting Python code to be executed
%reset - Delete all variables/names defined in interactive namespace
%page OBJECT - Pretty-print the object and display it through a pager
%run script.py - Run a Python script inside IPython
%prun statement - Execute statement with cProfile and report the profiler output
%time statement - Report the execution time of a single statement
%timeit statement - Run a statement multiple times to compute an ensemble average execution
time; useful for timing code with very short execution time
%who, %who_ls, %whos - Display variables defined in interactive namespace, with varying levels of
information/verbosity
%xdel variable - Delete a variable and attempt to clear any references to the object in the
IPython internals

Binary operators - Operation Description:
-----------------------------------------
a + b - Add a and b
a - b - Subtract b from a
a * b - Multiply a by b
a / b - Divide a by b
a // b - Floor-divide a by b, dropping any fractional remainder
a ** b - Raise a to the b power
a & b - True if both a and b are True; for integers, take the bitwise AND
a | b - True if either a or b is True; for integers, take the bitwise OR
a ^ b - For booleans, True if a or b is True, but not both; for integers, take the bitwise
EXCLUSIVE-OR
a == b - True if a equals b
a != b - True if a is not equal to b
a <= b, a < b - True if a is less than (less than or equal) to b
a > b, a >= b - True if a is greater than (greater than or equal) to b
a is b - True if a and b reference the same Python object
a is not b - True if a and b reference different Python objects

Standard Python scalar types - Type Description:
------------------------------------------------
None - The Python “null” value (only one instance of the None object exists)
str - String type; holds Unicode (UTF-8 encoded) strings
bytes - Raw ASCII bytes (or Unicode encoded as bytes)
float - Double-precision (64-bit) floating-point number (note there is no separate double
type)
boolA -  True or False value
int - Arbitrary precision signed integer

Datetime format specification (ISO C89 compatible) - Type Description
----------------------------------------------------------------------
%Y - Four-digit year
%y - Two-digit year
%m - Two-digit month [01, 12]
%d - Two-digit day [01, 31]
%H - Hour (24-hour clock) [00, 23]
%I - Hour (12-hour clock) [01, 12]
%M - Two-digit minute [00, 59]
%S - Second [00, 61] (seconds 60, 61 account for leap seconds)
%w - Weekday as integer [0 (Sunday), 6]
%U - Week number of the year [00, 53]; Sunday is considered the first day of the week, and days before the first Sunday of the year are “week 0”
%W - Week number of the year [00, 53]; Monday is considered the first day of the week, and days before the first Monday of the year are “week 0”
%z - UTC time zone offset as +HHMM or -HHMM; empty if time zone naive
%F - Shortcut for %Y-%m-%d (e.g., 2012-4-18)
%D - Shortcut for %m/%d/%y (e.g., 04/18/12)

list of commonly used set methods - Python set operations:
-----------------------------------------------------------
Function      Alternative syntax           Description
a.add(x)            N/A           Add element x to the set a
a.clear()           N/A           Reset the set a to an empty state,
                                  discarding all of its elements
a.remove(x)         N/A           Remove element x from the set a
a.pop()             N/A           Remove an arbitrary element from the set
                                  a, raising KeyError if the set is empty
a.union(b)        a | b           All of the unique elements in a and b
a.update(b)       a |= b          Set the contents of a to be the union of
                                  the elements in a and b
a.intersection(b) a & b           All of the elements in both a and b
a.intersection_update(b)  a &= b  Set the contents of a to be the       
                                  intersection of the elements in a and b
a.difference(b)   a - bT          he elements in a that are not in b
a.difference_update(b)  a -= b Set a to the elements in a that are not in b
a.symmetric_difference(b) a ^ b   All of the elements in either a or b but 
                                  not both
a.symmetric_difference_update(b) a ^= b   Set a to contain the elements in 
                                          either a or b but not both
a.issubset(b)       N/A           True if the elements of a are all       
                                  contained in b
a.issuperset(b)     N/A           True if the elements of b are all 
                                  contained in a
a.isdisjoint(b)     N/A          True if a and b have no elements in common

Python file modes - Mode Description:
-------------------------------------
r   - Read-only mode
w   - Write-only mode; creates a new file (erasing the data for any file  
      with the same name)
x   - Write-only mode; creates a new file, but fails if the file path 
      already exists
a  - Append to existing file (create the file if it does not already exist)
r+  -  Read and write
b   -   Add to mode for binary files (i.e., 'rb' or 'wb')
t   - Text mode for files (automatically decoding bytes to Unicode). This 
      is the default if not specified. Add t to other modes to use this (i.e., 'rt' or 'xt')

list of commonly used set methods. Python set operations:
---------------------------------------------------------
Function      Alternative       Description
                syntax
a.add(x)            N/A     Add element x to the set a
a.clear()           N/A     Reset the set a to an empty state,
                            discarding all of its elements
a.remove(x)         N/A     Remove element x from the set a
a.pop()             N/A     Remove an arbitrary element from the set
                            a, raising KeyError if the set is empty
a.union(b)          a | b   All of the unique elements in a and b
a.update(b)         a |= b  Set the contents of a to be the union of
                            the elements in a and b
a.intersection(b)   a & b   All of the elements in both a and b
a.intersection_update(b)  a &= b  Set the contents of a to be the      
                                  intersection of the elements in a and b
a.difference(b)     a - b   The elements in a that are not in b
a.difference_update(b)  a -= b Set a to the elements in a that are not in b
a.symmetric_difference(b)   a ^ b     All of the elements in either a or b                                     but not both
a.symmetric_difference_update(b)  a ^= b    Set a to contain the elements
                                            in either a or b but not both
a.issubset(b)     N/A     True if the elements of a are all contained in b
a.issuperset(b)   N/A     True if the elements of b are all contained in a
a.isdisjoint(b)   N/A     True if a and b have no elements in common