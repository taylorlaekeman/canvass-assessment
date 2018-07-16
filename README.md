# canvas-assessment

To run my solution to challenge #1, use the command `python all_even.py` from the project's root directory.

To run my solution to challenge #2, use the command `python3 sort.py` from the `sort` directory.  To test my solution to challenge #2, use the command `python3 test_sort.py` from the `sort` directory.

I'm particularly proud of my solution to challenge #2.  I believe that---in addition to writing a correct and functional implementation of Quicksort---I also wrote a clean, elegant, and easily-understood piece of software.  My implementation is split into three modules that meaningfully divide its functionality.  `filehandler.py` handles the file input and output, `compare.py` contains the comparators that are used by the algorithm, and `quicksort.py` contains the implementation of Quicksort itself.

I'm also proud of my minimal testing suite.  I decided not to test each method individually through unit tests because unit tests do not check that behaviour is correct and can themselves contain bugs.  They are a great tool to test small pieces of large applications, and become necessary when applications are so large that they cannot actually be *proven*.  Instead I chose to test the result of the algorithm.  I check the output lines to see if they are a permutation of the input lines, and that each item is 'larger' than the previous one.  If both of these things are true, than the output is correctly sorted.

If I were to continue working on my solution, I would look to update my algorithm so that it modified the list in place, and eliminated redundant memory usage.  If I were writing production code as opposed to a demo project, I would **always** look instead to an algorithm from a library that had been tested and scrutinized more rigorously.
