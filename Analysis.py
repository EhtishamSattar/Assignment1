from radon.cli import Config
from radon.cli.harvest import CCHarvester, RawHarvester
from pathlib import Path

def analyze_cyclomatic_complexity(file_path):
    config = Config(exclude="")  # You can customize the exclude pattern if needed
    cc_harvester = CCHarvester([str(file_path)], config)
    cc_results = cc_harvester.harvest()
    print(f"Cyclomatic Complexity for {file_path.name}: {cc_results.total_complexity}")

def analyze_halstead_metrics(file_path):
    config = Config(exclude="")
    hal_harvester = RawHarvester([str(file_path)], config)
    hal_results = hal_harvester.get_metrics()
    print(f"Halstead Metrics for {file_path.name}:")
    for key, value in hal_results._asdict().items():
        print(f"{key}: {value}")

def analyze_file(file_path):
    print(f"Analyzing {file_path.name}:")
    analyze_cyclomatic_complexity(file_path)
    analyze_halstead_metrics(file_path)
    print("\n" + "=" * 50 + "\n")

if __name__ == "__main__":
    files = [
        Path(r"D:\Sem 8\SQA\Assignments\Assignment1\CaterpilerGame.py"),
        Path(r"D:\Sem 8\SQA\Assignments\Assignment1\Translator\translator.py"),
        Path(r"D:\Sem 8\SQA\Assignments\Assignment1\RockPaperScissors.py"),
    ]

    for file_path in files:
        if file_path.exists() and file_path.is_file():
            analyze_file(file_path)
        else:
            print(f"File not found: {file_path}")
