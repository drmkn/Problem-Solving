from pathlib import Path
from datetime import datetime

def create_solution():
    # Get inputs
    date = input("Date (DD-MM-YYYY): ").strip()
    problem_name = input("Problem name: ").strip()
    link = input("LeetCode link: ").strip()

    print("\nPaste your Python solution.")
    print("Type END on a new line when finished:\n")

    lines = []

    while True:
        line = input()
        if line == "END":
            break
        lines.append(line)

    solution = "\n".join(lines)
    print(solution)
    # Validate date
    try:
        datetime.strptime(date, "%d-%m-%Y")
    except ValueError:
        print("Invalid date. Use DD-MM-YYYY format.")
        return

    # Create date folder
    folder = Path(date)
    folder.mkdir(parents=True, exist_ok=True)

    # Create Markdown content
    content = f"""# {problem_name}\n\n**LeetCode:** [{problem_name}]({link})
    \n\n## Solution
    \n```python
    {solution.rstrip()}
    """

    # Create Solution.md

    file_path = folder / "Solution.md"
    file_path.write_text(content, encoding="utf-8")

    print(f"\nCreated: {file_path}")

if __name__ == "__main__":
    create_solution()