from datetime import datetime
import re

# Задача 1. Создайте список. Запишите в него N первых элементов последовательности Фибоначчи.
# 6 –> 1 1 2 3 5 8
def Task1():
    print("Задача 1")
    number = abs(int(input("Введите число N: ")))
    if number > 1:
        fib_sequence = [1, 1]
        for _ in range(2, number):
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    else:
        fib_sequence = [1]
    print(*fib_sequence)

# Задача 2. В списке находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву.
# а –> абрикос, авокадо, апельсин, айва.
def Task2():
    print("\nЗадача 2")
    fruits = [
    "абрикос", "авокадо", "арбуз", "апельсин", "айва", "ананас",
    "банан", "барбарис", "боярышник",
    "груша", "гранат", "гуава",
    "дыня",
    "ежевика",
    "жимолость",
    "земляника",
    "изюм",
    "каламондин", "киви", "красноплодная рябина",
    "лайм", "лимон", "личи",
    "мандарин", "манго", "малина",
    "нектарин",
    "облепиха",
    "папайя", "персик", "помело",
    "рамбутан",
    "слива", "смородина",
    "тамарилло", "тыква",
    "фейхоа", "финик", "физалис",
    "хурма",
    "цитрон",
    "черешня", "черная смородина", "чайот",
    "шелковица", "шиповник",
    "яблоко",]
    letter = input("Введите букву: ").lower()[0]
    for i in fruits:
        if i[0] == letter:
            print(i)

# Задача 3. Создайте скрипт бота, который находит ответы на фразы по ключу в словаре. 
# Бот должен, как минимум, отвечать на фразы «привет», «как тебя зовут». 
# Если фраза ему неизвестна, он выводит соответствующую фразу.

# Функция загрузки данных из файла
def load_responses(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            return dict(line.split('\t') for line in content.split('\n') if line)
    except FileNotFoundError:
        return {
            "привет|здравствуй|здравствуйте": "Привет! Как могу помочь?",
            "как тебя зовут|твоё имя|твое имя": "Я чатбот.",
            "как дела|как жизнь|что нового|как ты": "Спасибо, что спросили! Я всего лишь искусственный интеллект, но моя задача – помогать вам. Чем могу быть полезен?",
            "какая погода|погода сегодня": "Извините, но я не могу предоставить вам актуальную информацию о погоде. Попробуйте использовать сервисы, предназначенные для этого.",
            "какой сегодня день|какое число": "Сегодня " + datetime.now().strftime("%d-%m-%Y"),
            "что такое (.*?)\?": "Определение для {0} можно найти на Википедии или других источниках знаний.",
            "как доехать|как пройти|как попасть": "Мне жаль, но я не могу предоставить маршрут. Рекомендую использовать карты Google или Яндекс.Карты для определения маршрута.",
            "default": "Извините, я не понимаю эту фразу. Пожалуйста, попробуйте сформулировать по-другому."
            }

# Функция сохранения данных в файл
def save_responses(responses, filename):
    with open(filename, "w") as file:
        for key, value in responses.items():
            file.write(f"{key}\t{value}\n")

# Функция поиска ответа на фразу
def find_response(phrase, responses):
    for key, value in responses.items():
        match = re.search(key, phrase, re.IGNORECASE)
        if match:
            return value.format(*match.groups())
    return responses["default"]

# Функция обучения бота
def teach_bot(phrase, response, responses):
    responses[phrase.lower()] = response
    print("Чатбот: Спасибо, я запомню это!")

# Функция взаимодействия с ботом
def interact_with_bot(responses, filename):
    while True:
        user_input = input("Пользователь: ")
        if user_input.lower() == "выход":
            print("Чатбот: Всего доброго!")
            break
        response = find_response(user_input, responses)

        if response == responses["default"]:
            print("Чатбот:", response)
            teach = input("Пользователь: Как мне на это ответить? ")
            teach_bot(user_input, teach, responses)
            save_responses(responses, filename)
        else:
            print("Чатбот:", response)

# Запуск бота
print("\nЗадача 3")
filename = "chatbot_data.txt"
responses = load_responses(filename)
interact_with_bot(responses, filename)


#Task1()
#Task2()