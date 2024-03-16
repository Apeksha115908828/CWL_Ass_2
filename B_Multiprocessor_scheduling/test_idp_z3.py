import random
import shutil

def generate_testcase(num_tasks, max_duration, num_processors):
    T = set(range(1, num_tasks + 1))
    T1 = set(random.randint(1, max_duration) for _ in range(num_tasks))
    Task = [(task_id, duration) for task_id, duration in zip(T, T1)]
    m = random.randint(1, num_processors)
    d = sum(T1)

    testcase = f"structure S : V {{\n"
    testcase += f"\tT ≜ {T}.\n"
    testcase += f"\tT1 ≜ {T1}.\n"
    testcase += f"\tTask ≜ {Task}.\n"
    testcase += f"\tm ≜ {m}.\n"
    testcase += f"\td ≜ {d}.\n"
    testcase += f"\tn ≜ {{0..{m-1}}}.\n"
    testcase += f"\td1 ≜ {{0..{d}}}.\n"
    testcase += "}"
    
    return testcase

def insert_structure_to_file(file_path, structure):
    with open(file_path, 'a') as file:
        file.write('\n')
        file.write(structure)

def copy_file(file_path, new_file_path):
    shutil.copyfile(file_path, new_file_path)

file_path = 'mps_final.idp'
new_file_path = 'mps_final_temp.idp'

num_tasks = 3
max_duration = 5
num_processors = 2
testcase = generate_testcase(num_tasks, max_duration, num_processors)

copy_file(file_path, new_file_path)

insert_structure_to_file(new_file_path, testcase)


