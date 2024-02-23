import psycopg2

def openServer(host, user, password, database):
    try:
        #connecting to DB
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT version();"
            )
            print(cursor.fetchall())

    except Exception as _ex:
        print("[ERRORS] PostgreSQL connection error", _ex)

    finally:
        if connection:
            connection.close()
            print("[INFO] PostgreSQL connection closed")