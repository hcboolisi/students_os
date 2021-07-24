import pymysql

userName = ""


def open():
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="1234",
        db="db_students",
        charset="utf8")
    return db


def exec(sql, values):
    db = open()
    print(db)
    cursor = db.cursor()
    print(cursor)
    try:
        cursor.execute(sql, values)
        db.commit()
        return 1
    except:
        db.rollback()
        return 0
    finally:
        cursor.close()
        db.close()


def query(sql, *keys):
    db = open()
    cursor = db.cursor()
    cursor.execute(sql, keys)
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return result


def query2(sql):
    db = open()
    print(db)
    cursor = db.cursor()
    print(cursor)
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return result
