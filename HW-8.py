import sqlite3

connect = sqlite3.connect('your_database.db')
cursor = connect.cursor()

# 1) Создание таблицы 1
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")
# 2) Создание таблицы 2
cursor.execute("""
CREATE TABLE IF NOT EXISTS grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    userid INTEGER,
    subject TEXT,
    grade INTEGER,
    FOREIGN KEY(userid) REFERENCES users(user_id)
)
""")
connect.commit()

# 3) Создание VIEW
cursor.execute("""
CREATE VIEW IF NOT EXISTS user_grades_view AS
SELECT
    users.user_id,
    users.name AS user_name,
    users.age,
    grades.subject,
    grades.grade
FROM users
LEFT JOIN grades ON users.user_id = grades.userid
""")
connect.commit()

# 5) Выборка и фильтры
def get_from_view(min_age=None, subject=None, min_grade=None):
    query = "SELECT user_id, user_name, age, subject, grade FROM user_grades_view"
    conditions = []
    params = []

    if min_age is not None:
        conditions.append("age >= ?")
        params.append(min_age)

    if subject is not None:
        conditions.append("subject = ?")
        params.append(subject)

    if min_grade is not None:
        conditions.append("grade >= ?")
        params.append(min_grade)

    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    cursor.execute(query, params)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Вызов
print("Выполнен вызов get_from_view() без фильтров:")
get_from_view()

print("\nС фильтром: возраст >18")
get_from_view(min_age=18)

print("\nС фильтром: предмет = Backend, минимальная оценка 3")
get_from_view(subject="BackendCourse", min_grade=3)

