class Section:
    def __init__(self, section_code, subject_code, course_code, num_credits, start_date, end_date):
        self.section_code = section_code
        self.subject_code = subject_code
        self.course_code = course_code
        self.num_credits = num_credits
        self.start_date = start_date
        self.end_date = end_date

    def __str__(self):
        return f"[Section] SectionCode: {self.section_code}, SubjectCode: {self.subject_code}, " \
               f"CourseCode: {self.course_code}, Credits: {self.num_credits}, " \
               f"Start: {self.start_date}, End: {self.end_date}"