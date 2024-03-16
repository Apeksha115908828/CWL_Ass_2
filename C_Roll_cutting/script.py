import random
import subprocess
from datetime import datetime
import matplotlib.pyplot as plt
import os
import signal

def executeAndGetPlotPoints_AMPL(file_name, input, plotNumNodes, plotTimeTaken):
    start_time = datetime.now()

    timeout_seconds = 30
    process = subprocess.Popen("C:\\Users\\Apeksha\\Downloads\\ampl.mswin64\\ampl.mswin64\\ampl.exe cut.run", stdout=subprocess.PIPE)
    try:
        stdout, _ = process.communicate(timeout=timeout_seconds)
    except subprocess.TimeoutExpired:
        os.kill(process.pid, signal.SIGINT)
        stdout, _ = process.communicate()

    with open('output_'+ file_name + '.txt', 'a') as output_file:
        output_file.write(stdout.decode("utf-8"))

    end_time = datetime.now()
    time_diff_milli_seconds = (end_time - start_time).total_seconds() * 1000
    plotNumNodes.append(input)
    plotTimeTaken.append(time_diff_milli_seconds)

def generateTestcaseAndExecuteAMPL():
    i1 = 0
    file_name = "cut.run"
    plotNumNodes_v1 = []
    plotTimeTaken_v1 = []
    for i in range(1, 6):
        num_tasks_values = random.randint(0, 30)
        plotNumNodes_v1.append(num_tasks_values)
        print(i)
        testcase = []
        testcase.append(f"data;\n")
        roll_width = random.randint(70, 150)
        testcase.append(f"param roll_width := {roll_width} ;\n")
        testcase.append(f"param: WIDTHS: orders :=\n")
        widths = set()
        while len(widths) < num_tasks_values:
            width = random.randint(1, roll_width)
            if width in widths:
                print("..")
            else:
                orders = random.randint(1, 30)
                widths.add(width)
                if i < num_tasks_values :
                    testcase.append(f"\t\t {width} \t {orders}\n")
                else :
                    testcase.append(f"\t\t {width} \t {orders} ;\n")

        filename = "cut.dat"
        with open(filename, 'w') as f:
            f.write('\n'.join(testcase))
        executeAndGetPlotPoints_AMPL(file_name, num_tasks_values, plotNumNodes_v1, plotTimeTaken_v1)
    plotNumNodes_v1, plotTimeTaken_v1 = zip(*sorted(zip(plotNumNodes_v1, plotTimeTaken_v1)))
    plt.plot(plotNumNodes_v1, plotTimeTaken_v1, label = "cut with ampl")
    plt.xlabel('Num of tasks to be scheduled')
    plt.ylabel('Time taken to execute')
    plt.title('Scheduling on m processors')
    plt.legend()
    plt.savefig('cut_ampl.png')

def clear_file(file_path):
    with open(file_path, 'w') as file:
        pass

if __name__ == "__main__":
    generateTestcaseAndExecuteAMPL()

