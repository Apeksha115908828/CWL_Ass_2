import random
import subprocess
from datetime import datetime
import matplotlib.pyplot as plt
import os
import signal

def generate_testcase(n):
    nodes = list(range(1, n+1))
    edges = {i: random.sample(nodes, random.randint(1, min(3, n-1))) for i in nodes}
    costs = {(i, j): random.randint(1, 10) for i in nodes for j in edges[i]}
    
    testcase = []
    testcase.append(f"% Nodes\n")
    for i in range(n):
        testcase.append(f"\nnode({i}).\n")
    testcase.append("% (Directed) Edges")
    
    testcase.append("\n% Edge Costs")
    for (i, j), cost in costs.items():
        if(i!=j):
            testcase.append(f"cost({i},{j},{cost}).")
    
    return '\n'.join(testcase)

def save_testcases(num_testcases, start_n, end_n):
    num_nodes = []
    for i in range(num_testcases):
        n = random.randint(start_n, end_n)
        num_nodes.append(n)
        testcase = generate_testcase(n)
        filename = f"tsp_input_{i+1}.lp"
        with open(filename, 'w') as f:
            f.write(testcase)
    return num_nodes

def executeAndGetPlotPoints(file_name, testcase, input, plotNumNodes, plotTimeTaken):
    start_time = datetime.now()
    command = ["/opt/homebrew/bin/clingo", testcase, file_name]

    timeout_seconds = 30
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    try:
        stdout, _ = process.communicate(timeout=timeout_seconds)
    except subprocess.TimeoutExpired:
        os.kill(process.pid, signal.SIGINT)
        stdout, _ = process.communicate()

    with open('output_'+ file_name + '.txt', 'a') as output_file:
        output_file.write(stdout.decode("utf-8"))

    end_time = datetime.now()
    time_diff_milli_seconds = (end_time - start_time).total_seconds() * 1000
    # Add points for number of nodes against time
    plotNumNodes.append(input)
    plotTimeTaken.append(time_diff_milli_seconds)

def executeAndGetPlotPoints_SCASP(file_name, testcase, input, plotNumNodes, plotTimeTaken):
    start_time = datetime.now()
    command = ["scasp", testcase, file_name]

    timeout_seconds = 30
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    try:
        stdout, _ = process.communicate(timeout=timeout_seconds)
    except subprocess.TimeoutExpired:
        os.kill(process.pid, signal.SIGINT)
        stdout, _ = process.communicate()

    with open('output_'+ file_name + '.txt', 'a') as output_file:
        output_file.write(stdout.decode("utf-8"))

    end_time = datetime.now()
    time_diff_milli_seconds = (end_time - start_time).total_seconds() * 1000
    # Add points for number of nodes against time
    plotNumNodes.append(input)
    plotTimeTaken.append(time_diff_milli_seconds)

def executeAndGetPlotPoints_AMPL(file_name, input, plotNumNodes, plotTimeTaken):
    start_time = datetime.now()
    command = ["./ampl", file_name]

    timeout_seconds = 30
    process = subprocess.Popen("C:\\Users\\Utkarsha\\Downloads\\ampl.mswin64\\ampl.mswin64\\ampl.exe tsp.run", stdout=subprocess.PIPE)
    try:
        stdout, _ = process.communicate(timeout=timeout_seconds)
    except subprocess.TimeoutExpired:
        os.kill(process.pid, signal.SIGINT)
        stdout, _ = process.communicate()

    with open('output_'+ file_name + '.txt', 'a') as output_file:
        output_file.write(stdout.decode("utf-8"))

    end_time = datetime.now()
    time_diff_milli_seconds = (end_time - start_time).total_seconds() * 1000
    # Add points for number of nodes against time
    plotNumNodes.append(input)
    plotTimeTaken.append(time_diff_milli_seconds)


def generateTestcaseAndExecuteSCASP(num_tasks_values):
    file_name = "tsp.pl"
    plotNumNodes_v1 = []
    plotTimeTaken_v1 = []
    for i in range(1, 6):
        print(i)
        input = num_tasks_values
        executeAndGetPlotPoints_SCASP(file_name, "tsp_input_" + str(i) + ".lp", input[i-1], plotNumNodes_v1, plotTimeTaken_v1)
    plotNumNodes_v1, plotTimeTaken_v1 = zip(*sorted(zip(plotNumNodes_v1, plotTimeTaken_v1)))
    plt.plot(plotNumNodes_v1, plotTimeTaken_v1, label = "tsp with SCASP")
    plt.xlabel('Num of tasks to be scheduled')
    plt.ylabel('Time taken to execute')
    plt.title('Scheduling on m processors')
    plt.legend()
    plt.savefig('tsp_scasp.png')

def generateTestcaseAndExecuteAMPL(num_tasks_values):
    file_name = "tsp.run"
    plotNumNodes_v1 = []
    plotTimeTaken_v1 = []
    for i in range(0, len(num_tasks_values)):
        print(i)
        input = num_tasks_values[i]
        testcase = []
        testcase.append(f"data;\n")
        testcase.append(f"param: NODES: hpos vpos :=")
        for i in range(num_tasks_values[i]):
            hpos = random.randint(0, 100)
            vpos = random.randint(0, 100)
            testcase.append(f"{i} {hpos} {vpos}\n")
        filename = f"tsp.dat"
        with open(filename, 'w') as f:
            f.write('\n'.join(testcase))
        executeAndGetPlotPoints_AMPL(file_name, input, plotNumNodes_v1, plotTimeTaken_v1)
    plotNumNodes_v1, plotTimeTaken_v1 = zip(*sorted(zip(plotNumNodes_v1, plotTimeTaken_v1)))
    plt.plot(plotNumNodes_v1, plotTimeTaken_v1, label = "tsp with ampl")
    plt.xlabel('Num of nodes in the graph')
    plt.ylabel('Time taken to execute')
    plt.title('Travelling Salesman Problem in AMPL')
    plt.legend()
    plt.savefig('tsp_ampl.png')

def generateTestcase():
    plt.clf()
    # Parameters
    num_testcases = 5
    start_n = 4
    end_n = 18

    # Generate and save testcases
    num_tasks_values = save_testcases(num_testcases, start_n, end_n)
    return num_tasks_values

def generateTestcaseAndExecuteTSP(num_tasks_values):
    file_name = "tsp.lp"
    plotNumNodes_v1 = []
    plotTimeTaken_v1 = []
    for i in range(1, 6):
        print(i)
        input = num_tasks_values
        executeAndGetPlotPoints(file_name, "tsp_input_" + str(i) + ".lp", input[i-1], plotNumNodes_v1, plotTimeTaken_v1)
    plotNumNodes_v1, plotTimeTaken_v1 = zip(*sorted(zip(plotNumNodes_v1, plotTimeTaken_v1)))
    plt.plot(plotNumNodes_v1, plotTimeTaken_v1, label = "tsp with clingo")
    plt.xlabel('Num of tasks to be scheduled')
    plt.ylabel('Time taken to execute')
    plt.title('Scheduling on m processors')
    plt.legend()
    plt.savefig('tsp_clingo.png')

# clear the files
def clear_file(file_path):
    with open(file_path, 'w') as file:
        pass

if __name__ == "__main__":
    # file_paths = ['output_tsp.lp.txt', "tsp_input_1.lp", "tsp_input_2.lp", "tsp_input_3.lp", "tsp_input_4.lp", "tsp_input_5.lp"]
    # file_paths1 = ['output_tsp.pl.txt', "tsp_input_1.dat", "tsp_input_2.dat", "tsp_input_3.dat", "tsp_input_4.dat", "tsp_input_5.dat"]
    
    # for file_path in file_paths:
    #     clear_file(file_path)
    num_tasks_values = generateTestcase()
    # generateTestcaseAndExecuteTSP(num_tasks_values)
    # plt.clf()
    generateTestcaseAndExecuteSCASP(num_tasks_values)
    # generateTestcaseAndExecuteAMPL(num_tasks_values)

