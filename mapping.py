from flask import Flask, request, render_template, redirect, url_for
import os
import csv
from collections import defaultdict
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'csv'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def parse_csv(filepath):
    with open(filepath, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

def build_mappings(students, faculties):
    sections = defaultdict(list) 
    faculty_to_sections = defaultdict(set)
    section_to_faculties = defaultdict(set)

    for s in students:
        key = (s['program'], s['department'], s['semester'], s['section'])
        sections[key].append(s)

    for f in faculties:
        key = (f['program'], f['department'], f['semester'], f['section'])
        faculty_key = (f['facultyID'], f['fullName'], f['email'])
        faculty_to_sections[faculty_key].add(key)
        section_to_faculties[key].add(faculty_key)

    return sections, faculty_to_sections, section_to_faculties

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        student_file = request.files['student_csv']
        faculty_file = request.files['faculty_csv']

        if student_file and allowed_file(student_file.filename) and \
           faculty_file and allowed_file(faculty_file.filename):

            student_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(student_file.filename))
            faculty_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(faculty_file.filename))

            student_file.save(student_path)
            faculty_file.save(faculty_path)

            students = parse_csv(student_path)
            faculties = parse_csv(faculty_path)

            sections, faculty_to_sections, section_to_faculties = build_mappings(students, faculties)

            return render_template(
                'results.html',
                faculty_to_sections=faculty_to_sections,
                section_to_faculties=section_to_faculties
            )

        else:
            return "Invalid file format", 400

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
