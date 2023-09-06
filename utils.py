from dispatcher import db


def lessons_to_text(lessons):
    result = ""
    for i in lessons:
        name = db.get_subject(i[1])[1]
        result += f"{i[4]}. {name}\n"
    return result
