from mysql.connector import connect,Error


class WordnetData:
    def __init__(self):
        try:
            self.conn = connect(host="127.0.0.1",user="root",password="root",port=3306)
        except Error as e:
            self.conn = None
            print(e)