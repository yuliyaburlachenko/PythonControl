#Необходимо написать проект, содержащий функционал работы с заметками.
#Программа должна уметь создавать заметку, сохранять её, 
#читать список заметок, редактировать заметку, удалять заметку.
import json
import os
import uuid
from datetime import datetime

# Путь к файлу для хранения заметок
FILE_PATH = 'notes.json'

def load_notes():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as file:
            return json.load(file)
    return {}

def save_notes(notes):
    with open(FILE_PATH, 'w') as file:
        json.dump(notes, file, indent=4)

def create_note(title, body):
    note_id = str(uuid.uuid4())
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return {'id': note_id, 'title': title, 'body': body, 'timestamp': timestamp}

def list_notes():
    notes = load_notes()
    for note in notes.values():
        print(f"{note['id']} - {note['title']} - {note['timestamp']}")

def view_note(note_id):
    notes = load_notes()
    if note_id in notes:
        note = notes[note_id]
        print(f"{note['id']} - {note['title']} - {note['timestamp']}")
        print(note['body'])
    else:
        print("Заметка не найдена.")

def add_note(title, body):
    notes = load_notes()
    note = create_note(title, body)
    notes[note['id']] = note
    save_notes(notes)
    print("Заметка добавлена.")

def edit_note(note_id, title, body):
    notes = load_notes()
    if note_id in notes:
        notes[note_id]['title'] = title
        notes[note_id]['body'] = body
        notes[note_id]['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        save_notes(notes)
        print("Заметка изменена.")
    else:
        print("Заметка не найдена.")

def delete_note(note_id):
    notes = load_notes()
    if note_id in notes:
        del notes[note_id]
        save_notes(notes)
        print("Заметка удалена.")
    else:
        print("Заметка не найдена.")

# Пример использования функций
while True:
    print("\nВыберите действие:")
    print("1. Создать заметку")
    print("2. Показать список заметок")
    print("3. Просмотреть заметку")
    print("4. Редактировать заметку")
    print("5. Удалить заметку")
    print("6. Выйти")

    choice = input("Ваш выбор: ")

    if choice == '1':
        title = input("Введите заголовок заметки: ")
        body = input("Введите текст заметки: ")
        add_note(title, body)
    elif choice == '2':
        list_notes()
    elif choice == '3':
        note_id = input("Введите ID заметки: ")
        view_note(note_id)
    elif choice == '4':
        note_id = input("Введите ID заметки для редактирования: ")
        title = input("Введите новый заголовок: ")
        body = input("Введите новый текст: ")
        edit_note(note_id, title, body)
    elif choice == '5':
        note_id = input("Введите ID заметки для удаления: ")
        delete_note(note_id)
    elif choice == '6':
        break
    else:
        print("Неверный выбор. Попробуйте еще раз.")

