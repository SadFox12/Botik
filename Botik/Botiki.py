import datetime
import random
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Загрузка необходимых данных
#nltk.download('punkt')
#nltk.download('stopwords')
#nltk.download('punkt_tab')

stop_words = set(stopwords.words('russian'))

# Функция для обработки текста
def preprocess_text(text):
    # Токенизация с универсальным токенизатором punkt
    tokens = word_tokenize(text.lower())  # Не указываем язык для предотвращения ошибок
    # Удаление стоп-слов и не буквенных символов
    filtered_tokens = [word for word in tokens if word.isalpha() and word not in stop_words]
    return filtered_tokens

# Функция для определения ответа
def get_bot_response(user_input):
    user_input = preprocess_text(user_input)

    # Ответы на стандартные вопросы
    if 'время' in user_input:
        return "Текущее время: " + datetime.datetime.now().strftime("%H:%M:%S")

    elif 'дата' in user_input:
        return "Сегодняшняя дата: " + datetime.datetime.now().strftime("%Y-%m-%d")

    elif 'погода' in user_input:
        return "Извините, я не могу предоставить информацию о погоде."

    elif 'поиграем' in user_input:
        return start_game()

    # Если вопрос не распознан
    return "Извините, я не понял ваш запрос."

# Функция для старта игры
def start_game():
    number_to_guess = random.randint(1, 10)  # Загадать число от 1 до 10
    print("Я загадал число от 1 до 10. Попробуй его угадать!")

    while True:
        user_guess = input("Введи свой вариант: ")
        if user_guess.isdigit():
            user_guess = int(user_guess)
            if user_guess < number_to_guess:
                print("Мое число больше. Попробуй снова.")
            elif user_guess > number_to_guess:
                print("Мое число меньше. Попробуй снова.")
            else:
                return "Поздравляю! Ты угадал число."
        else:
            print("Пожалуйста, вводи только числа.")

# Главный цикл чат-бота
def chat():
    print("Привет! Я чат-бот. Спроси меня что-нибудь.")

    while True:
        user_input = input("Вы: ")
        if user_input.lower() == 'выход':
            print("До свидания!")
            break

        response = get_bot_response(user_input)
        print("Бот: " + response)

# Запуск бота
chat()
