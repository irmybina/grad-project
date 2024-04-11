import pymysql
from config_test import *
import psycopg2

# try:
#     connection = psycopg2.connect(database=db_name, user=user, password=password, host=host)
#
#     with connection.cursor() as cursor:
#         create_table_query = "CREATE TABLE public.users(id serial PRIMARY KEY, username VARCHAR(255), password VARCHAR(255))"
#         cursor.execute(create_table_query)
#         connection.commit()
#         # print(cursor.fetchone())
#
# except Exception as e:
#     print(e)
#     print("Something went wrong")
# finally:
#     if connection:
#         connection.close()
#         print("PostgreSQL connection is closed")

# try:
#     connection = pymysql.connect(host=host,
#                              port=3306,
#                              user=user,
#                              password=password,
#                              database=db_name,
#                              cursorclass=pymysql.cursors.DictCursor)
#     print("Connection successful")
#     print("--------------------")

    # try:
        # with connection.cursor() as cursor:
        #     create_table_query = "CREATE TABLE `users`(id int AUTO_INCREMENT," \
        #                                  " name varchar(32)," \
        #                              " password varchar(32)," \
        #                              " email varchar(32), PRIMARY KEY (id));"
        #     cursor.execute(create_table_query)
        #     print("Table created successfully")


        # with connection.cursor() as cursor:
        #     insert_query = "INSERT INTO `users` (name, password, email) VALUES ('Anna', 'qwerty', 'pochta@abc.de');"
        #     cursor.execute(insert_query)
        #     connection.commit()

        # with connection.cursor() as cursor:
        #     select_all_rows = "SELECT * FROM `users`"
        #     cursor.execute(select_all_rows)
        #     rows = cursor.fetchall()
        #     for row in rows:
        #         print(row)

        # with connection.cursor() as cursor:
        #     update_query = 'UPDATE `users` SET `password` = %s WHERE `id` = 1'
        #     cursor.execute(update_query, ("password"))
        #     connection.commit()

        # with connection.cursor() as cursor:
        #     delete_query = "DELETE FROM users WHERE id = %s"
        #     cursor.execute(delete_query, 1)
        #     connection.commit()

        # with connection.cursor() as cursor:
        #     drop_table = "DROP TABLE IF EXISTS `users`"
#
#     finally:
#         connection.close()
# except Exception as e:
#     print(e)
#     print("Connection failed")

