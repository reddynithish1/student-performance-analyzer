# 📊 Student Performance Analyzer

A simple and robust **Python-based data analysis project** that analyzes student marks from a CSV file. This project was created using the **Windsurf tool** and focuses on clean design, proper error handling, and readable output.

The analyzer computes:

* Average score per student
* Top-performing student
* Subject-wise average marks

---

## 🚀 Features

* 📂 Reads student data from a CSV file
* 📈 Calculates average marks per student
* 🏆 Identifies the top performer based on average score
* 📚 Computes subject-wise average marks
* ⚠️ Custom exception handling for missing files and invalid data
* 🧼 Clean, readable console output

---

## 🗂️ Project Structure

```text
student-performance-analyzer/
│
├── student_marks.csv        # Input dataset
├── student_analyzer.py      # Main Python script
└── README.md                # Project documentation
```

---

## 📄 CSV File Format

The input CSV file **must** contain the following columns:

| Column Name | Description            |
| ----------- | ---------------------- |
| Name        | Student name           |
| Subject     | Subject name           |
| Marks       | Marks scored (numeric) |

### ✅ Example (`student_marks.csv`)

```csv
Name,Subject,Marks
Alice,Math,85
Alice,Science,90
Bob,Math,78
Bob,Science,82
```

---

## 🛠️ Requirements

* Python **3.8+**
* pandas

Install dependencies using:

```bash
pip install pandas
```

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone <your-repo-url>
cd student-performance-analyzer
```

2. Ensure `student_marks.csv` is present in the project directory.

3. Run the script:

```bash
python student_analyzer.py
```

---

## 📤 Sample Output

```text
Average Score Per Student:
Alice    87.50
Bob      80.00

Top Performer: Alice with an average score of 87.50

Subject-wise Average Marks:
Math       81.50
Science    86.00
```

---

## ⚠️ Error Handling

The project uses a **custom exception (`DataError`)** to handle:

* Missing CSV file
* Missing required columns (`Name`, `Subject`, `Marks`)
* Non-numeric values in the `Marks` column

Errors are displayed in a user-friendly way without crashing the program.

---

## 🌱 Branch Information

This README was created in the branch:

```
feature-readme
```

---

## 🤝 Contribution

* Creating feature branches
* Submitting pull requests
* Improving documentation or adding new analytics features

---

## 📌 Future Enhancements

* Add visualization (charts/graphs)
* Export results to a report file
* Add grading (A/B/C) logic
* CLI arguments for custom CSV input

---

## 🧑‍💻 Author

Forked and enhanced by **charitha(github.com/cha861)**
Original project created using **Windsurf Tool**

---

⭐ If you find this project useful, feel free to star the repository!
