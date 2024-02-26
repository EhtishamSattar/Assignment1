import subprocess
import matplotlib.pyplot as plt
import re

def run_radon_halstead(file_path):
    try:
        result = subprocess.run(["radon", "hal", file_path], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running radon hal: {e}")
        return None

def parse_radon_halstead_output(output):
    # Extract Halstead metrics values using regular expression
    pattern = r"^\s*(\w+):\s+([\d.]+)"
    matches = re.findall(pattern, output, re.MULTILINE)
    
    # Convert the matched values to a dictionary
    #halstead_data = {name: float(value) for name, value in matches}
    halstead_data = {name: float(value) for name, value in matches if name.lower() != "effort"}
    
    return halstead_data

def plot_halstead_results(halstead_data):
    # Create a bar chart using Matplotlib
    
    names = list(halstead_data.keys())
    values = list(halstead_data.values())

    plt.bar(names, values)
    plt.xlabel('Halstead Metric Factors')
    plt.ylabel('Value')
    plt.title('Halstead Metrics Analysis')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    plt.show()

def showHalsteadGraph(file):
    file_path = file  # Replace with the actual path to your Python file

    hal_output = run_radon_halstead(file_path)

    if hal_output:
        halstead_data = parse_radon_halstead_output(hal_output)
        print("Halstead Metrics Data:")
        print(halstead_data)

        plot_halstead_results(halstead_data)
    else:
        print("Failed to run radon hal.")
