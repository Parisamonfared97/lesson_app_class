import sqlite3
#connection = sqlite3.connect('database_dars.db')
# cursor = connection.cursor()
# cursor.execute()
# connection.commit()
# cursor.close()
# connection.close()





def save(title,teacher,class_number,unit):
    connection = sqlite3.connect(r'E:\python\dars_app\repository\database_dars.db')
    cursor = connection.cursor()
    cursor.execute('insert into lessons (title,teacher,class_number,unit) values (?,?,?,?)',
    [title,teacher,class_number,unit])
    connection.commit()
    cursor.close()
    connection.close()


def edit(code,title,teacher,class_number,unit):
    connection = sqlite3.connect(r'E:\python\dars_app\repository\database_dars.db')
    cursor = connection.cursor()
    cursor.execute('update lessons set title=?,teacher=?,class_number=?,unit=? where code =?',
                   [title, teacher, class_number, unit,code])
    connection.commit()
    cursor.close()
    connection.close()



def remove(code):
    connection = sqlite3.connect(r'E:\python\dars_app\repository\database_dars.db')
    cursor = connection.cursor()
    cursor.execute('delete from lessons where code  = ?',
                   [code])
    connection.commit()
    cursor.close()
    connection.close()



def find_all():
    connection = sqlite3.connect(r'E:\python\dars_app\repository\database_dars.db')
    cursor = connection.cursor()
    cursor.execute('select * from lessons')
    lessons_list = cursor.fetchall()
    cursor.close()
    connection.close()
    return lessons_list




def find_by_code(code):
    connection = sqlite3.connect(r'E:\python\dars_app\repository\database_dars.db')
    cursor = connection.cursor()
    cursor.execute('select * from lessons where code = ?',[code])
    lesson = cursor.fetchone()
    cursor.close()
    connection.close()
    return lesson


def find_by_teacher(teacher):
    connection = sqlite3.connect(r'E:\python\dars_app\repository\database_dars.db')
    cursor = connection.cursor()
    cursor.execute('select * from lessons where teacher like ?', [teacher+"%"])
    lesson = cursor.fetchone()
    cursor.close()
    connection.close()
    return lesson


def find_by_class_title(title):
    connection = sqlite3.connect(r'E:\python\dars_app\repository\database_dars.db')
    cursor = connection.cursor()
    cursor.execute('select * from lessons where title like ?', [title + "%"])
    lesson = cursor.fetchone()
    cursor.close()
    connection.close()
    return lesson
