# Internship Finder

## Overview

Internship Finder is a Python-based web scraping tool that searches for internships on Internshala based on a user-provided skill keyword. The script extracts internship details and stores them in a CSV file. It also supports automatic daily scraping at a specified time.

---

# Features

* Search internships by skill keyword.
* Extracts:

  * Internship Title
  * Company Name
  * Location
  * Internship Link
  * Date Posted
* Saves results in a CSV file.
* Removes duplicate entries.
* Supports daily automated scraping using a scheduler.

---

# Requirements

* Python 3.9 or later

Install the required Python libraries using:

```bash
pip install requests beautifulsoup4 pandas schedule
```

---

# Project Structure

```text
project-folder/
│
├── internship_finder.py
├── internship_results.csv   (generated automatically)
└── README.md
```

---

# How to Run

Open a terminal in the project folder and execute:

```bash
python internship_finder.py
```

If your system uses `python3`:

```bash
python3 internship_finder.py
```

---

# Menu Options

When the program starts, it displays:

```text
1. Run Once
2. Daily Automation
```

## Option 1 – Run Once

Choose:

```text
1
```

You will be prompted for a skill keyword.

Example:

```text
Enter skill keyword: python
```

The program immediately scrapes available internships and saves them into:

```text
internship_results.csv
```

---

## Option 2 – Daily Automation

Choose:

```text
2
```

Enter the desired skill keyword.

Example:

```text
Enter skill keyword: machine-learning
```

The scraper will:

* Run immediately once.
* Schedule itself to run every day at **10:00 AM**.
* Continue running until stopped manually.

Stop automation using:

```text
CTRL + C
```

---

# Command-Line Arguments

This script does **not** require any command-line arguments.

Instead, it interacts with the user through terminal prompts.

| Prompt        | Description                                                     |
| ------------- | --------------------------------------------------------------- |
| Menu Option   | Select whether to run once or enable automation                 |
| Skill Keyword | Internship keyword to search (e.g., python, java, data-science) |

---

# Output

The script generates a CSV file named:

```text
internship_results.csv
```

Each row contains:

| Column      | Description                       |
| ----------- | --------------------------------- |
| Title       | Internship title                  |
| Company     | Company offering the internship   |
| Location    | Internship location               |
| Link        | Direct internship URL             |
| Date Posted | Posting date shown on Internshala |

Duplicate internships are automatically removed before saving.

---

# Example Run

```text
===== MENU =====
1. Run Once
2. Daily Automation

Choose an option: 1

Enter skill keyword: python

Fetching internships...

Found 24 internships.

Saved Successfully!
Records in file : 24
Output file     : internship_results.csv
```

---

# Screenshot

## Replace with Screenshot of Program Execution

<img width="402" height="272" alt="image" src="https://github.com/user-attachments/assets/b437844c-ead0-4dfe-ae19-4cbdcacd58c6" />

---

## Replace with Screenshot of Generated CSV File

<img width="1258" height="657" alt="image" src="https://github.com/user-attachments/assets/c9a608ff-073c-40fe-a49b-5ecd0d738787" />

---

# Notes

* An active internet connection is required.
* If the CSV file already exists, newly scraped internships are appended.
* Duplicate internship entries are automatically removed.
* If no internships match the provided keyword, the script will notify the user without creating duplicate records.
