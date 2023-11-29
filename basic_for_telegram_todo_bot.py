import random 

HELP = """
help - наечатать справку по программе
add - добавить задачу в список (название задачи запрашиваем у пользователя)
show - напечатать все добавленные задачи
random - добавлять случайную задачу на дату Сегодня"""

RANDOM_TASKS = ["Записаться на курс в Нетологию", "Написать Гвидо письмо", "Покормить кошку", "Помыть машину"]

tasks = {
  
}

run = True

def add_todo(date, task):
  if date in tasks:
    tasks[date].append(task)
    print(f'Задача {task} добавлена на дату {date}')
  else:
    tasks[date] = []
    tasks[date].append(task)
    print(f'Задача {task} добавлена на дату {date}')

while run:
  command = input('Введите команду: ')
  
  if command == 'help':
    print(HELP)
    
  elif command == 'show':
    date = input('Введите дату для отображения списка задач: ')
    if date in tasks:
      for task in tasks[date]:
        print('- ', task)
    else:
      print('Такой даты нет')
  
  elif command == 'add':
    date = input('Введите дату: ')
    task = input('Введите название задачи: ')
    add_todo(date, task)
      
  elif command == 'exit':
    print('Спасибо за использование!')
    break

  elif command == 'random':
    task = random.choice(RANDOM_TASKS)
    add_todo("Сегодня", task)
    
  else:
    print('Неизвестная команда')
    break
print('До свидания!')