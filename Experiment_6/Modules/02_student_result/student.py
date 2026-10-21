def total_marks(marks): return sum(marks)
def percentage(marks): return sum(marks) / len(marks)
def grade(p):
    if p >= 90: return "A"
    elif p >= 75: return "B"
    elif p >= 60: return "C"
    elif p >= 40: return "D"
    return "F"
