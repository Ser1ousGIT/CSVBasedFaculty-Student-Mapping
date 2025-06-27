# Faculty–Student Mapper

This is a web-based utility that maps faculty members to the student sections they are assigned to teach and vice versa. Upload two CSV files (one for students, one for faculty), and the application generates detailed tables of:

- Sections each faculty member teaches
- Faculty assigned to each student section


# Features

- Upload **Student** and **Faculty** CSV files.
- Automatically parse and group students by their:
  - Program
  - Department
  - Semester
  - Section
- Create two-way mappings:
  - **Faculty → Sections they teach**
  - **Section → Assigned faculties**
- Displays results in a clean, readable HTML table format.
- Handles multiple faculty–section assignments.
- Modular, lightweight, and easy to deploy.


# Important

- Use the headers from the **faculty.csv** and **student.csv** to avoid errors or change the code to match your needs. For our code these headers are the ones that are the most relevant and allow us to make unique pairings precisely.
- Install Flask

'''
pip install Flask
'''

- Run python on whatever host you'd like to use, easiest would be:

  pyton mapping.py
  localhost:5000

