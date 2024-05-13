import sqlite3


class DataBase:
    def __init__(self):
        self.database = sqlite3.connect('data.db', check_same_thread=False)
        # Чтобы база не задерживала очередь запросов

    def manager(self, sql, *args,
                fetchone: bool = False,
                fetchall: bool = False,
                commit: bool = False):
        with self.database as db:
            cursor = db.cursor()
            cursor.execute(sql, args)
            if commit:
                result = db.commit()
            if fetchone:
                result = cursor.fetchone()
            if fetchall:
                result = cursor.fetchall()
            return result

    def create_users_table(self):
        sql = '''
        CREATE TABLE IF NOT EXISTS users(
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            chat_id TEXT UNIQUE,
            language TEXT
        )
        '''
        self.manager(sql, commit=True)

    def get_user_by_chat_id(self, chat_id):
        sql = '''
                SELECT * FROM users WHERE chat_id = ?
                '''
        return self.manager(sql, chat_id, fetchone=True)

    def register_user(self, chat_id):
        sql = '''
        INSERT INTO users(chat_id) VALUES (?)
        '''
        return self.manager(sql, chat_id, commit=True)

    def set_lang(self, chat_id, lang):
        sql = '''
        UPDATE users
        SET language = ?
        WHERE chat_id = ?
        '''
        return self.manager(sql, lang, chat_id, commit=True)

    def get_lang(self, chat_id):
        sql = '''
        SELECT language FROM users WHERE chat_id = ? 
        '''
        return self.manager(sql, chat_id, fetchone=True)
