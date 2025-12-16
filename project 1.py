import pandas as pd

# Custom exception for missing CSV or columns
class DataError(Exception):
    pass

class StudentAnalyzer:
    """
    A class to analyze student marks from a CSV file.
    It calculates averages, top performers, and subject-wise stats.
    """

    def __init__(self, csv_file):
        """
        Initialize the analyzer by loading data from the CSV file.

        Args:
            csv_file (str): Path to the CSV file containing student data.
        
        Raises:
            DataError: If the file is missing or lacks required columns.
        """
        try:
            # Attempt to read the CSV file
            self.data = pd.read_csv(csv_file)
        except FileNotFoundError:
            raise DataError(f"CSV file '{csv_file}' not found. Please check the file path.")
        
        # Check for required columns to ensure the data is usable
        required_columns = ["Name", "Subject", "Marks"]
        missing_columns = [col for col in required_columns if col not in self.data.columns]
        if missing_columns:
            raise DataError(f"CSV is missing required columns: {missing_columns}. Please ensure the file has 'Name', 'Subject', and 'Marks'.")
        
        # Validate that Marks are numeric
        if not pd.api.types.is_numeric_dtype(self.data["Marks"]):
            raise DataError("The 'Marks' column must contain numeric values.")

    def average_score_per_student(self):
        """
        Calculate the average marks for each student across all subjects.

        Returns:
            pandas.Series: A series with student names as index and their average marks as values.
        """
        # Group by student name and compute the mean of their marks
        return self.data.groupby("Name")["Marks"].mean()

    def top_performer(self):
        """
        Identify the student with the highest average score.

        Returns:
            tuple: A tuple containing the top student's name (str) and their average score (float).
        
        Note: This uses the precomputed averages from average_score_per_student().
        """
        # First, get the average scores
        avg_scores = self.average_score_per_student()
        
        # Find the student with the maximum average (handling ties by picking the first in alphabetical order, as idxmax() does)
        top_student = avg_scores.idxmax()
        top_score = avg_scores.max()
        
        return top_student, top_score

    def subject_wise_average(self):
        """
        Calculate the average marks for each subject across all students.

        Returns:
            pandas.Series: A series with subjects as index and their average marks as values.
        """
        # Group by subject and compute the mean marks
        return self.data.groupby("Subject")["Marks"].mean()

# Main execution block - like a friendly script that runs the analysis
if __name__ == "__main__":
    try:
        # Create an analyzer instance with the CSV file
        analyzer = StudentAnalyzer("student_marks.csv")
        
        # Display average score per student in a readable way
        print("Average Score Per Student:")
        avg_scores = analyzer.average_score_per_student()
        print(avg_scores.to_string(float_format="%.2f"))  # Format to 2 decimal places for clarity
        
        # Find and display the top performer nicely
        top_student, top_score = analyzer.top_performer()
        print(f"\nTop Performer: {top_student} with an average score of {top_score:.2f}")
        
        # Show subject-wise averages
        print("\nSubject-wise Average Marks:")
        subject_avgs = analyzer.subject_wise_average()
        print(subject_avgs.to_string(float_format="%.2f"))  # Again, nice formatting
    
    except DataError as e:
        # Handle any data-related errors gracefully
        print(f"Oops! A data error occurred: {e}")
    except Exception as e:
        # Catch any other unexpected errors
        print(f"Something unexpected happened: {e}")
