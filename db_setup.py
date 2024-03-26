from data import questions, questions_uz, questions_uz_latin
from db import insert_to_question, insert_to_option, create_tables_if_not_exists, select_question


def insert_data(questions, language):
    order_num = 0
    for q in questions:
        is_single_option = True
        if q["question"] != "Перейти на следующий вопрос" and q["question"] != "Кейинги саволга ўтиш" and q["question"] != "Keyingi savolga o'tish":
            insert_to_question(q['question'], is_single_option, order_num, language)
            inserted_question = select_question(order_num, language)
            print(f"q={order_num}")
            question_id = inserted_question[0][0]
            for o in q["answers"]:
                print(f"0={o}")
                insert_to_option(question_id, o, language, order_num)
            order_num +=1

def db_setup():
    # creating tables
    create_tables_if_not_exists()

    # inserting data
    # insert_data(questions, 'ru')
    # insert_data(questions_uz, 'uz_kiril')
    # insert_data(questions_uz_latin, 'uz_latin')

    