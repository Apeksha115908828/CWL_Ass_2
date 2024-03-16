import subprocess
from datetime import datetime
import matplotlib.pyplot as plt
import random
import os
import signal

def executeAndGetPlotPoints(file_name, testcase, input, plotNumNodes, plotTimeTaken):
    start_time = datetime.now()
    command = ["/opt/homebrew/bin/clingo", testcase, file_name]

    # Run the command with a timeout of 10 seconds
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

def generate_test_case(num_tasks, m, d):
    tasks = []
    for i in range(1, num_tasks + 1):
        length = random.randint(1, d)
        tasks.append(f"task({i}, {length}).")
    params = f"#const m = {m}.\n#const d = {d}.\n"
    return params + "\n".join(tasks)

def has_solution(tasks, m, d):
    total_length = sum(tasks.values())
    return total_length <= m * d
num_test_cases = 5

def generateTestcasesMPS():    
    min_num_tasks = 3
    max_num_tasks = 15
    m_values = [2, 5, 8]
    d_values = [5, 12, 17]
    num_tasks_values = []
    task_counts = set()

    for i in range(num_test_cases):
        m = random.choice(m_values)
        d = random.choice(d_values)
        num_tasks = random.randint(min_num_tasks, max_num_tasks)
        while num_tasks in task_counts:
            num_tasks = random.randint(min_num_tasks, max_num_tasks)
        task_counts.add(num_tasks)
        num_tasks_values.append(num_tasks)
        test_case = generate_test_case(num_tasks, m, d)
        tasks = {i: random.randint(1, d) for i in range(1, num_tasks + 1)}
        if has_solution(tasks, m, d):
            solution = "Solution exists."
        else:
            solution = "No solution."
        file_name = f"mps_input_{i}.lp"
        with open(file_name, "w") as file:
            file.write(f"% Test Case {i + 1} (m={m}, d={d}): {solution}\n{test_case}\n")
        print(f"Test case {i + 1} written to {file_name}")
    return num_tasks_values


def generateTestcaseAndExecuteMPS():
    plt.clf()
    file_name = "mps.lp"
    plotNumNodes_v1 = []
    plotTimeTaken_v1 = []
    num_tasks_values = generateTestcasesMPS()
    for i in range(0, 5):
        print(i)
        input = num_tasks_values
        executeAndGetPlotPoints(file_name, "mps_input_" + str(i) + ".lp", input[i], plotNumNodes_v1, plotTimeTaken_v1)
    plotNumNodes_v1, plotTimeTaken_v1 = zip(*sorted(zip(plotNumNodes_v1, plotTimeTaken_v1)))
    plt.plot(plotNumNodes_v1, plotTimeTaken_v1, label = "mps with clingo")
    plt.xlabel('Num of tasks to be scheduled')
    plt.ylabel('Time taken to execute')
    plt.title('Scheduling on m processors')
    plt.legend()
    plt.savefig('mps.png')

# clear the files
def clear_file(file_path):
    with open(file_path, 'w') as file:
        pass

if __name__ == "__main__":
    file_paths = ['output_mps.lp.txt', "mps_input_0.lp", "mps_input_1.lp", "mps_input_2.lp", "mps_input_3.lp", "mps_input_4.lp"]
    for file_path in file_paths:
        clear_file(file_path)
    generateTestcaseAndExecuteMPS()