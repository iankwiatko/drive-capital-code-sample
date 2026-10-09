# Drive Capital Network Analyzer

Network analyzer written for the Drive Capital coding interview!

## Table of Contents

1. Build, Run, and Test

2. Approach and Design Decisions

3. Assumptions

## 1. Build, Run, and Test

### Requirements

- Python `3.14.8+`

### Cloning/Setup

To be able to run the repo, you need to clone the GitHub repository onto your local machine. The project should only use built-in tools, so no proprietary installs are necessary.

### Running the program

To run the program, simply navigate to the parent/top-level directory and input `py analyze_network.py input.txt` into the command line. The analyze_network.py serves as a entry point so that the program is executable from the top-level directory. Please note, the input file needs to be located in the same parent folder as the analyze_network.py file; otherwise, the path to the file needs to be specified.

### Running the tests

The tests are written using Python's built-in test suite`unittest`. To run the test suite, simply input `py -m unittest -v`. This will execute all the tests. Additional documentation on how to run unittest is provided [here](https://docs.python.org/3/library/unittest.html#command-line-interface)

## 2. Approach and Design Decisions

### Approach

My goal with this sample program was to provide a real-life example of the engineering fundamentals I use to develop applications. Engineering to me is a delicate balance of designing the most efficient solution while also keeping things like maintainability, scalability, readability, time complexity, along with other principles, in mind. While developing this application, many of the design choices I made were impacted by these ideas.

To approach this problem, I initially created a diagram that helped me understand how the mock network should look and how commands interact with each other. This was followed by creating a class structure to help represent the network. This class structure helps enforce organization of data and creates reusable classes to help easily represent our commands. From here, I dissected the larger problem into smaller bits that would later become my functions. I iterated through developing each of these functions, writing unit tests along the way to make sure each one functioned properly. The most complex part of this problem for me was the relationship algorithm. It took a bit of brainstorming, but eventually I found something that I was comfortable with, and that felt balanced. To round the project out, I simply connected all the parts together, ran some end-to-end tests, and had my complete result!

### Design Decisions

For this section, I will list a few engineering principles and how they impacted my design decisions.

Readability, Scalability, and Maintainability:

One of the bigger decisions I made with regard to this project was to make build_network a function. I initially thought about including build_network.py as a class method for the network. After teetering back and forth a little bit, I ended up settling for an individual function that was similar to how the remainder of my project functions. This decision improves readability and maintainability, as I feel that having each step of the network building process as a function creates a more uniform feel across the repo. It makes things easier to find. This decision also allowed unit tests to be easily created for the function. In the long term, it also helps with scalability. What if the project starts to pull from a database or API calls? A new function can be easily configured to solve this rather than rewriting the class method implementation.

The design of the class structure was also heavily influenced by these principles. I kept maintainability in mind, as I wanted each function to be easily unit tested and isolated rather than one big mushy main file.

Reusability:

The design decision to have individual functions was impacted by wanting them to be more reusable. If another portion of the program has repeatable logic, it can be easily reused!

Separation of Concerns:

Separation of concerns impacted an initial implementation of the parser that has a list of tuples as the final output. I chose to return a list of command types instead, as this helped keep the validation in the parser. With the original tuple implementation, command validity checks were done when building a network, which muddled the lines between the functions of each. Now the parser is strictly dedicated to parsing and validating inputs, and build_network is responsible for creating the network we use.

Time Complexity:

I considered time complexity when designing any of the iterations, especially the strongest_partners function. Nearly all of the functions have a maximum runtime of O(N), with N being the length of the data structure. The worst case stems from the strongest partners, which is O(NLogN), as the sort functions add complexity. The separation of concerns helps with minimizing the average runtime, as usually each function iterates through one data structure.

### Use of LLM Tools

I used LLM tools in a variety of ways for this project. Copilot was my main tool, and I utilized it to help me write boilerplate code, aid with debugging, and help simplify expressions using some syntax sugar. I also used Copilot to help me identify where errors were necessary and, most importantly, to help me write test cases. However, all the main design decisions involving logic, structure, and trade-offs were made by me. Copilot is a tool, not a solution! (at least to me)

## 3. Assumptions

### Assumptions About the Input

- A command consists of only the characters A-Z, in upper or lower case. _(from requirements)_

  To expand this, I assumed all commands and args have the same casing as in the example. Each command or arg is led by a capital letter aside from the contact types. _(my assumption)_
- The company an employee works at is declared before the employee. _(from requirements)_

  To expand this, I assumed employees and partners also have to be declared before a contact command**(my assumption)**
- Input is well formed, with no incorrectly formatted lines. _(from requirements)_
- I assumed there is only one input file. _(my assumption)_
- Each interaction has the same weight, regardless of contact type. Meeting for coffee holds the same weight as an email _(my assumption)_
- I resolved ties for the strongest partner by alphabetical order. _(my assumption)_
