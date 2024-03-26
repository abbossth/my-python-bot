from config import DATABASE_URL
import psycopg2

# create table if not exists
def create_tables_if_not_exists():    
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()
        
            # SQL statements to create tables
        create_users_table = """
        CREATE TABLE IF NOT EXISTS Users (
            id SERIAL PRIMARY KEY,
            user_id INTEGER,
            chosen_language VARCHAR(128),
            current_question_order INTEGER,
            is_survey_finished BOOLEAN,
            join_date TIMESTAMP
        );
        """

        create_questions_table = """
        CREATE TABLE IF NOT EXISTS questions (
            id SERIAL PRIMARY KEY,
            question_text VARCHAR(256),
            is_single_option BOOLEAN,
            order_num INTEGER,
            language VARCHAR(128)
        );
        """

        create_options_table = """
        CREATE TABLE IF NOT EXISTS options (
            id SERIAL PRIMARY KEY,
            question_id INTEGER REFERENCES questions(id),
            option_text VARCHAR(256),
            language VARCHAR(128),
            order_num INTEGER
        );
        """

        create_question_responses_table = """
        CREATE TABLE IF NOT EXISTS question_responses (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES Users(user_id),
            question_id INTEGER REFERENCES questions(id),
            option_id INTEGER REFERENCES options(id)
        );
        """

        cursor.execute(create_users_table)
        cursor.execute(create_questions_table)
        cursor.execute(create_options_table)
        cursor.execute(create_question_responses_table)
        conn.commit()
        print("Tables created successfully!")
        # Close the database connection
        cursor.close()
        conn.close()
    except Exception as _ex:
        print(f"Error in creating tables {_ex}")

# create new user
def new_user(user_id):
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()
        insert_query = f"""
        INSERT INTO users (user_id, current_question_order, is_survey_finished, join_date)
        VALUES ({user_id}, 0, False, NOW());
        """
        cursor.execute(insert_query)
        conn.commit()
        print("User created successfully!")
        cursor.close()
        conn.close()
    except Exception as _ex:
        print(f"Error in creating new user. {_ex}")
        conn.rollback()

# choose language
def set_language(user_id, language):
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()
        insert_query = f"""
        UPDATE users SET 
        chosen_language = '{language}'
        WHERE user_id = {user_id};
        """
        cursor.execute(insert_query)
        conn.commit()
        print("Language set successfully!")
    except Exception as _ex:
        print(f"Error in setting language to user {user_id}. {_ex}")
        conn.rollback()

# increment order num
def increment_order_num(user_id, num):
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()
        insert_query = f"""
        UPDATE users SET 
        current_question_order = {num}
        WHERE user_id = {user_id};
        """
        cursor.execute(insert_query)
        conn.commit()
        print("Incremented successfully!")
    except Exception as _ex:
        print(f"Error in incrementing order num to user {user_id}. {_ex}")
        conn.rollback()

# select all users
def select_users():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM USERS")
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result
    except Exception as _ex:
        print(f"Error in fetching users. {_ex}")
        return _ex

# select one user with id
def select_user(user_id):
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM USERS WHERE user_id = {user_id}")
        user_exists = cursor.fetchall()
        cursor.close()
        conn.close()
        return user_exists
    except Exception as _ex:
        print(f"Error in fetching user with id: {user_id}. {_ex}")
        return _ex


# QUESTIONS
# insert questions
def insert_to_question(question_text, is_single_option, order_num, language):
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()

        # Insert statement for the first question
        insert_question_query = f"""
        INSERT INTO questions (question_text, is_single_option, order_num, language) 
        VALUES ('{question_text}', {is_single_option}, {order_num}, '{language}');
        """
        cursor.execute(insert_question_query)
        conn.commit()
        # Close the cursor and connection
        cursor.close()
        conn.close()
    except Exception as ex:
        print(f"Error in inserting questions in insert_to_question function. {ex}")

# get question
# select one question with id
def select_question(order_num, language):
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM QUESTIONS WHERE order_num = {order_num} AND language = '{language}'")
        q_exists = cursor.fetchall()
        cursor.close()
        conn.close()
        return q_exists
    except Exception as _ex:
        print(f"Error in fetching question with id: {q_exists}. {_ex}")
        return _ex

# OPTIONS
# insert options
def insert_to_option(question_id, option_text, language, order_num):
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()

        # Insert statement for the first question
        insert_option_query = f"""
        INSERT INTO options (question_id, option_text, language, order_num) 
        VALUES ({question_id}, '{option_text}', '{language}', {order_num});
        """
        cursor.execute(insert_option_query)
        conn.commit()
        # Close the cursor and connection
        cursor.close()
        conn.close()
    except Exception as ex:
        print(f"Error in inserting options in insert_to_option function. {ex}")


# get options
# select options with question id
def select_options(order_num, language):
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM OPTIONS WHERE order_num = {order_num} AND language = '{language}'")
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result
    except Exception as _ex:
        print(f"Error in fetching options of question with id: {order_num, language}. {_ex}")
        return _ex

