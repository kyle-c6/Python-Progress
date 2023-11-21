import os, time

taskList = []

while True:
  os.system("clear")
  
  row = []
  
  print("Task Manager")
  menu = input("1 - Add\n2 - View\n3 - Edit\n4 - Remove\n").strip()
  
  if menu == "1": #ADD
    
    os.system("clear")
    task = input("Task: ").strip().title()
    if task in taskList:
      print("Task already exists.")
      time.sleep(2)
    else:
      due = input("Due Date: ").strip()
      priority = input("Priority: ").strip().title()
      row = [task, due, priority]
      taskList.append(row)
      print("Task Added")
      time.sleep(2)
      
  elif menu == "2": #VIEW
    
    os.system("clear")
    view = input("1 - All\n2 - Priority\n").strip()
    if view == "1": # View All
      os.system("clear")
      for row in taskList:
        for value in row:
          print(value, end=" | ")
        print()
        time.sleep(2)
    elif view == "2": # View by Priority
      os.system("clear")
      i = input("1 - High\n2 - Medium\n3 - Low\n").strip()
      if i == "1": # View High Priority Tasks
        os.system("clear")
        for row in taskList:
          if row[2] == "High":
            for value in row:
              print(value, end=" | ")
          print()
        time.sleep(2)
      elif i == "2": # View Medium Priority Tasks
        os.system("clear")
        for row in taskList:
          if row[2] == "Medium":
            for value in row:
              print(value, end=" | ")
          print()
        time.sleep(2)
      elif i == "3": # View Low Priority Tasks
        os.system("clear")
        for row in taskList:
          if row[2] == "Low":
            for value in row:
              print(value, end=" | ")
          print()
        time.sleep(2)
  
  elif menu == "3": #EDIT

    os.system("clear")
    edit = input("1 - Task\n2 - Due Date\n3 - Priority\n").strip()
    if edit == "1": # Edit Task
      os.system("clear")
      task = input("Task: ").strip().title()
      os.system("clear")
      for row in taskList:
        if row[0] == task:
          task = input("New Task: ").strip().title()
          row[0] = task
          print("Task Updated")
          time.sleep(2)
    elif edit == "2": # Edit Due Date
      os.system("clear")
      task = input("Task: ").strip().title()
      os.system("clear")
      for row in taskList:
        if row[0] == task:
          due = input("New Due Date: ").strip()
          row[1] = due
          print("Due Date Updated")
          time.sleep(2)
    elif edit == "3": # Edit Priority
      os.system("clear")
      task = input("Task: ").strip().title()
      os.system("clear")
      for row in taskList:
        if row[0] == task:
          priority = input("New Priority: ").strip().title()
          row[2] = priority
          print("Priority Updated")
          time.sleep(2)

  elif menu == "4":
    os.system("clear")
    remove = input("What task would you like to remove? ").strip().title()
    os.system("clear")
    for row in taskList:
      if row[0] == remove:
        taskList.remove(row)
        print("Task Removed")
        time.sleep(2)
      else:
        print("That task is not on your task list.")
        time.sleep(2)
