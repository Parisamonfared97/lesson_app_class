import sqlite3


connection = sqlite3.connect('database_dars.db')
# cursor = connection.cursor()
# cursor.execute()
# connection.commit()
# cursor.close()
# connection.close()

def create_database():
    my_connection = sqlite3.connect('repository/database_dars.db')
    cursor = my_connection.cursor()
    cursor.execute(
        """
        create table lessons (
        code integer primary key autoincrement ,
        title text not null ,
        teacher text not null ,
        class_number integer,
        unit integer
        )
        """
    )
    my_connection.commit()
    cursor.close()
    my_connection.close()

#اضافه کردن رکورد در جدول
# cursor = connection.cursor()
# cursor.execute('insert into lessons
# (title,teacher,class_number,unit)
# values
# (?,?,?,?)
# );
# connection.commit()
# cursor.close()
# connection.close()

#ویرایش رکورد در جدول
#cursor = connection.cursor()
#cursor.execute('update lessons
# set title=?,teacher=?,class_number=?,unit=?
#where ? =?
# );
# connection.commit()
# cursor.close()
# connection.close()


#حذف رکورد از جدول
#cursor = connection.cursor()
#cursor.execute('delete from lessons where ?  = ?;)
# connection.commit()
# cursor.close()
# connection.close()


#جستجو یا گزارش
##cursor = connection.cursor()
#cursor.execute('select * from lessons;
#select * from lessons where ?=?);
#cursor.fetchall()
#cursor.fetchone()



