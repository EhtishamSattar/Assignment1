import subprocess
import matplotlib.pyplot as plt
import re


def parse_output(output):
    # Extract function/method names and average complexities using regular expression
    pattern = r"\s*F\s+(\d+:\d+)\s+(\w+)\s+-\s+(\w+)"
    matches = re.findall(pattern, output)

    # Mapping from letter representations to numerical values
    complexity_mapping = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6}

    # Convert the matched values to a dictionary
    complexity_data = {name: complexity_mapping[avg_complexity] for _, name, avg_complexity in matches}
    
    return complexity_data

def plot_cc_results(complexity_data):
    # Create a bar chart using Matplotlib
    names = list(complexity_data.keys())
    values = list(complexity_data.values())

    plt.bar(names, values)
    plt.xlabel('Function/Method')
    plt.ylabel('Cyclomatic Complexity')
    plt.title('Cyclomatic Complexity Analysis')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    plt.show()


def showgraph(file):
    file_path = file  # Replace with the actual path to your Python file

    try:
        result = subprocess.run(["radon", "cc", file_path], capture_output=True, text=True, check=True)
        cc_output = result.stdout
        print("Radon CC output:")
        print(cc_output)
        data = parse_output(cc_output)
        #print(data)
        plot_cc_results(data)
    except subprocess.CalledProcessError as e:
        print(f"Error running radon cc: {e}")