# CWL-Ass2

Modeling and solving with rules and constraints

A. Traveling salesperson
Testcases are generated using randomization, the code to generate testcases can be found in A_travelling_salesman/script.py

Clingo implementation: File: tsp.lp
generateTestcase() generates testcases for the clingo implementation, generateTestcaseAndExecuteTSP() has implementation to execute the testcases.
generateTestcase() generates testcases for number of nodes ranging from 4 nodes to 8 nodes and cost/3 predicates using randomized function.
To execute: uncomment generateTestcaseAndExecuteTSP(num_tasks_values) line in the main function and run python script.py on the terminal.

tsp_input_[i].lp : The input testcases will be stored in these files.
output_tsp.lp.txt: the output for all the testcases executed will be stored in this file.
tsp_clingo.png: The performance graph will be in this file.
As the graph suggests, we are getting polynomial complexity in the execution in clingo.

Correctness testing: The files tsp_no_models.lp and tsp_has_cycle.lp have testcases to perform correctness testing on traveling salesman implementation in clingo:
tsp_no_models.lp: This file has a disconnected graph so there shouldn't be a solution to this testcase, on executing tsp.lp file with this testcase, the output shows UNSATISFIABLE which means there is no solution, this proves the correctness in case of a disconnected graph.
tsp_has_cycle.lp has a testcase where there is a cycle and the implementation should be able to find the hamilton cycle with lowest cost, on executing tsp.lp with this testcase, the output shows that there is a cycle.
To execute on terminal run:
$clingo tsp_no_models.lp tsp.lp
$clingo tsp_has_cycle.lp tsp.lp


SCASP Implementation: File: tsp.pl
The testcases are generated in common for clingo and SCASP implementation, and testcases are placed in the files tsp_input_[i].lp files.
generateTestcaseAndExecuteSCASP() has implementation to execute the testcases for implementation in s(CASP).
tsp.pl: This file has the Ciao-Prolog implementation with s(CASP) for traveling salesman problem.
output_tsp.pl.txt: the output for all the testcases executed will be stored in this file.
tsp_scasp.png: The performance graph can be found in this file.
The performance is comparable to the clingo implementation.
To execute: uncomment generateTestcaseAndExecuteSCASP(num_tasks_values) line in the main function and run python script.py on the terminal.

Correctness testing: The files tsp_no_models.lp and tsp_has_cycle.lp have testcases to perform correctness testing on traveling salesman implementation in SCASP:
tsp_no_models.lp: This file has a disconnected graph so there shouldn't be a solution to this testcase, on executing tsp.pl file with this testcase, the output shows UNSATISFIABLE which means there is no solution, this proves the correctness in case of a disconnected graph.
tsp_has_cycle.lp has a testcase where there is a cycle and the implementation should be able to find the hamilton cycle with lowest cost, on executing tsp.pl with this testcase, the output shows that there is a cycle.
To execute on terminal run:
$scasp tsp_no_models.lp tsp.pl
$scasp tsp_has_cycle.lp tsp.pl

AMPL implementation: 
Files:
tsp.dat: This file has the testcases used for the performance testing(This file is replaced for every testcase).
tsp.run: This file has the logic to execute the code using the input from tsp.dat abnd the implementation in tsp.mod
tsp.mod: has the AMPL implementation for the traveling salesman problem
generateTestcaseAndExecuteAMPL() has implementation to execute the testcases for the implementation in AMPL.
output_tsp.run.txt: The output for all the testcases executed will be stored in this file.
tsp_ampl.png: The performance graph can be found in this file.
The performance graph is linear, the performance is way better with AMPL programming as compared to clingo and SCASP implementation.
To execute: uncomment generateTestcaseAndExecuteAMPL(num_tasks_values) line in the main function and run python script.py on the terminal.

Correctness testing: The files tsp_1.dat has testcase for correctness testing.
tsp_1.dat has a testcase where there is a cycle and the implementation should be able to find the hamilton cycle with lowest cost, on executing tsp.lp with this testcase, the output shows that there is a cycle.
To execute on terminal run:
$ ./ampl tsp_1.run


B. Multiprocessor scheduling
Testcases are generated using randomization, the code to generate testcases can be found in B_Multiprocessor_scheduling/script.py

Clingo implementation: File: mps.lp
generateTestcasesMPS(): This function has the implementation to generate the testcases for the multi process scheduling. The testcases are generated for values for number of tasks ranging from 3 to 15. 
generateTestcaseAndExecuteMPS() has implementation to execute the testcases on clingo implementation for performance testing.
mps_input_[i].lp has the testcases for clingo implementation.
task/2 predicate has task(taskid, length) has the taskid and its length.
output_mps.lp.txt: This file has output for all the executed testcases.
mps.png: The performance graph can be found in this file.
The performance graph is quadratic as can be observed from the graph.
To execute: uncomment generateTestcaseAndExecuteMPS() line in the main function and run python script.py on the terminal.
Predicates: 
start/4 : start(T, P, S, L) : this predicate is to store the task(T: taskId) to processor(P: processorId) mapping along with the start time(S) and its length(L: task length).
task/2 : task(T, L) : this predicate is to store the task length where T(T: taskId) and length(L: length of the task).

Correctness Testing:
The files mps_solvable.lp and mps_unsolvable.lp have testcases to perform correctness testing on multi process scheduling implementation in Clingo:
mps_solvable.lp: This file has tasks that can be scheduled with the given processors and time limit so there should be a solution to this testcase, on executing mps.lp file with this testcase, the output gives a SATISFIABLE with the mapping.
mps_unsolvable.lp has a testcase where there is no scheduling possible, on running this testcase, it shows UNSATISFIABLE as expected.
To execute on terminal run:
$clingo mps_solvable.lp mps.pl
$clingo mps_unsolvable.lp mps.pl

SCASP Implementation: File: mps.pl
The SCASP implementation for the multi process scheduling can be found in mps.pl file. I have implemented the code in s(CASP) but as it not passing the correctness test, I have not done the performance testing.

IDP-Z3 Implementation: mps_final.idp
The IDP-Z3 implementation for multi process scheduling in IDP-Z3, file test_idp_z3.py has implementation for generating testcases and executing them for performance testing. 

DLV Implementation: mps.query.1
This file has multi process scheduling implementation in DLV, but DLV has a limitation that doesn't allow us to define variable intervals that we need to use to define the range of values allowed for start of any task.

C. Roll Cutting:
Testcases are generated using randomization, the code to generate testcases can be found in C_Roll_cutting/script.py

AMPL Implementation:
Files:
cut.dat: This file has the testcases used for the performance testing(This file is replaced for every testcase).
cut.run: This file has the logic to execute the code using the input from cut.dat abnd the implementation in cut.mod
cut.mod: has the AMPL implementation for the roll cutting problem
generateTestcaseAndExecuteAMPL() has the implementation to generate and execute the testcases and do the performance testing.
output_cut.run.txt: The output for all the testcases executed will be stored in this file.
cut_ampl.png: The performance graph can be found in this file.
The performance graph is not linear, the complexity is kind of polynomial as can be observed from the graph.
To execute: uncomment generateTestcaseAndExecuteAMPL(num_tasks_values) line in the main function and run python script.py on the terminal.

CorrectNess Testing: This implementation gives a possible solution with optimal values.
cut_1.dat has the testcase for correctness testing, we can execute this testcase using following command:
$ ./ampl cut_1.run
This file takes cut_1.dat as input while executing and gives the optimal solution by minimizing the number of rolls used.

Clingo Implementation:
Files: roll_cutting.lp: I have attempted to implement the roll cutting problem in clingo in this file, but I could not get the correctness testing done as t.

