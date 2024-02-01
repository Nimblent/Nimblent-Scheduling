import pulp

def h(hours, minutes=0):
    return hours*60 + minutes

def convert_min_hrs(course_minutes):
    hours = course_minutes // 60
    minutes = course_minutes % 60
    return (hours, minutes)

def format_mins(course_minutes):
    hours, minutes = convert_min_hrs(course_minutes)
    return f"{hours:02}h{minutes:02}"

def show_day_courses(courses):
    for start, end in courses:
        print("---------")
        print(f"Start: {format_mins(start)}")
        print(f"End: {format_mins(end)}")

def generate_course(start_end_hour, lunch_breaks, breaks, breaks_duration, course_duration=h(0,55)):
    '''
    Generate all available courses in the week considering all the breaks including lunch breaks.
    You can edit settings such as course_duration and breaks_duration
    '''
    courses = []
    
    for i, (start, end) in enumerate(start_end_hour):
        current_hour = start
        day_courses = []
        
        while current_hour < end:
            if current_hour in breaks[i]:
                current_hour += breaks_duration
            if current_hour == lunch_breaks[i][0]:
                current_hour = lunch_breaks[i][1]
            if current_hour + course_duration > end:
                break
            
            day_courses.append((current_hour, current_hour+course_duration))
            
            current_hour += course_duration
        
        if end - current_hour > 0:
            day_courses.append((current_hour, end))
        
        courses.append(day_courses)
    show_day_courses(courses[0])
    return courses


# Données de contraintes
start_end_hour = [
    (h(9, 25), h(17, 25)), 
    (h(8, 15), h(17, 25)), 
    (h(8, 15), h(17, 25)), 
    (h(8, 15), h(17, 25)), 
    (h(8, 15), h(17, 25))
]

breaks = [
    (h(15, 20),),
    (h(10, 5), h(15, 45)),
    (h(10, 5), h(15, 20)),
    (h(10, 5), h(15, 20)),
    (h(10, 5), h(15, 20)),
]

lunch_breaks = [
    (h(12, 10), h(13, 30)),
    (h(12, 10), h(13, 55)),
    (h(12, 10), h(13, 30)),
    (h(12, 10), h(13, 30)),
    (h(12, 10), h(13, 30)),
]

breaks_duration = h(0, 15)

generate_course(start_end_hour, lunch_breaks, breaks, breaks_duration)

subjects = [
    (("Maths", "Physiques", "SVT"), h(6)),
    (("NSI", "HDA", "HGGSP"), h(6)),
    (("Allemand", "Espagnol"), h(2)),
    (("Philosophie"), h(4)),
    (("Histoire Géographie"), h(4)),
    (("Anglais"), h(2)), 
    ((None, "Maths expertes", "Maths complémentaires"), h(2)),   
    ((None, "Cinéma Audiovisuel", "Art plastique"), h(2)), 
]

teachers = [
    ("Prof A", ("Maths", "NSI")),
    ("Prof B", ("Histoire Géographie", "HGGSP")),
    ("Prof C", ("Physiques")),
    ("Prof D", ("SVT")),
    ("Prof E", ("Histoire-Géographie", "Cinéma Audiovisuel")),
    ("Prof F", ("HDA", "Art plastique")),
    ("Prof G", ("Allemand")),
    ("Prof H", ("Espagnol")),
    ("Prof I", ("Philosophie")),
    ("Prof J", ("Anglais"))
]
