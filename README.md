
#  LeetCode-Sync

`LeetCode-Sync` is a lightweight, terminal-based CLI utility designed to automate the process of organizing, formatting, and syncing coding solutions directly to a GitHub repository.

---

##  Why LeetCode-Sync?
I primarily solve LeetCode problems using my **Android tablet** . Because browser extensions like *LeetHub* are entirely unavailable in this environment, I built this lightweight CLI tool to bridge the gap. It eliminates manual file shifting and git pushing, allowing a seamless, keyboard-driven backup process right inside your terminal (like Termux).

---

##  Features

*   **Interactive CLI Work Flow :** Dynamic terminal prompts with input loops validate problem names, algorithmic topics, and language configurations on the fly.
*   **Structured Organization :** Automatically classifies solutions into cleanly separated folders based on code topics (e.g., `ARRAY/`, `STRINGS/`).
*   **Automatic File Formatting :** Automatically handles title string conversions into standard, lowercase, underscore-separated file names (e.g., `two_sum.py`).
*   **End-to-End Git Automation :** Automatically stages, commits with a tailored message prefix (`SOLVED : Problem Name`), and pushes the updates directly to GitHub while handling sub-process exceptions.

## Demo

![LeetCode Sync Demo](assets/demo.gif)

---

## Project Structure

```text
leetcode-sync/
├── main.py            # Main script running the interactive CLI loop
├── input_handler.py   # Manages terminal prompts, code collection, and validations
├── file_handler.py    # Maps file extensions and writes scripts to local paths
├── git_handler.py     # Automates system git subprocess workflows (add, commit, push)
├── solutions/         # Directory containing organized topic sub-folders
├── assets/            # Project documentation images or design assets
└── README.md          # Project documentation
```

## Requirements

Before running the project, ensure that the following are installed on your system:

- Python 3.10 or later
- Git
- A GitHub account

> **Platform Support**
>
> This project has been developed and tested on **Termux (Android)** and is expected to work on Linux systems with Python and Git installed.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/aalwinrajesh001-a11y/leetcode-sync.git
cd leetcode-sync
```

---

## Dependencies

No external Python packages are required.

LeetCode Sync relies entirely on Python's standard library.

---

## Running the Tool

Start the application using:

```bash
python main.py
```

The tool will guide you through the following steps:

- Enter the LeetCode problem name.
- Select the problem topic.
- Choose the programming language.
- Paste the accepted solution.
- Automatically create the required folder structure.
- Save the solution file.
- Commit the changes.
- Push the solution to GitHub.

> **Important**
>
> Before using the tool, make sure:
>
> - Git is installed on your system.
> - The repository is connected to a valid GitHub remote.
> - Git authentication (SSH or Personal Access Token) has already been configured.
>
> Otherwise, the automated Git push operation will fail.

---

## Example

```text
PROBLEM NAME : Two Sum
PROBLEM TOPIC : ARRAY
LANGUAGE : cpp

Enter the copied code below.
Type 'END' on a new line when finished.

class Solution {
    ...
}

END
```

After completion, the generated directory structure will look similar to:

```text
leetcode-sync/
└── solutions/
    └── ARRAY/
        └── two_sum.cpp
```
---

##  Future Plans (Version 2)

I am activPlanned improvements include : 

*   **Automatic Metadata Extraction:** Automatically pull problem titles and categories directly from the LeetCode platform to eliminate manual typing.
*   **URL Support:** Simply pass a LeetCode problem URL to initialize the configuration workspace and fetch context instantly.
*   **Better Language Detection:** Intelligently parse and detect the source programming language automatically based on code boilerplate or keywords.
*   **Configuration File:** Support for a local config file (e.g., `.env` or `config.json`) to store customized directory paths, target repository configurations, and default languages.
*   **Statistics Module:** Track your daily solving streaks, difficulty counts, and total categorized metrics directly from your terminal dashboard.
*   **Better CLI Experience:** Improve user interaction designs using richer text rendering frameworks (like `rich` or `curses`) for cleaner prompts and loading indicators.

## License

This project is licensed under the MIT License.

See the [LICENSE](LICENSE) file for more information.

## Author

**Aalwin Rajesh**

- GitHub Profile: https://github.com/aalwinrajesh001-a11y
