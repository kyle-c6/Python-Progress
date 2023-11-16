import os, time

taskList = []

def pPrint():
  os.system("clear")
  for i in range(len(taskList)):
    print(f"{i+1}: {taskList[i]}")
  top = input("Press enter to return to the Main Menu: ") # Return to menu prompt rather than sleep and clear. User has as much time as needed to view their list
  top == True
  
while True:
  os.system("clear")
  print("Task Manger")
  time.sleep(1)
  menu = input("1: Add\n2: Remove\n3: Edit\n4: View List\n5: CLear List\n")
  os.system("clear")
  if menu.strip() == "1" or menu.strip().lower() == "add": # ADD TASK
    task = input("What would you like add? ").strip().title()
    if task in taskList:
      print("That is already on your Task List.")
      time.sleep(2)
    else:
      taskList.append(task)
      time.sleep(1)
  elif menu.strip() == "2" or menu.strip().lower() == "remove": # REMOVE TASK
    task = input("What would you like to remove? ").strip().title()
    if task in taskList:
      confirm = input(f"Are you sure you would like to remove {task}?\nEnter 1 to Confirm: ")
      if confirm == "1":
        taskList.remove(task)
      else:
        print(f"Okay, we won't remove {task}.")
        time.sleep(2)
    else:
      print("That task isn't on your Task List.")
  elif menu.strip() == "3" or menu.strip().lower() == "edit": # EDIT TASK
    task = input("Which task whould you like to edit? ").strip().title()
    if task in taskList:
      newTask = input("What would you like to change this to? ").strip().title()
      if newTask in taskList:
        print("This new task is already in your Task List. Let's try again.")
        time.sleep(2)
      else:
        confirm = input(f"Are you sure you want to replace {task} with {newTask}?\nEnter 1 to Confirm: ")
        if confirm.strip() == "1":
          taskList.remove(task)
          taskList.append(newTask)
        else:
          print("Alright, let's try again.")
          time.sleep(2)
    else:
      print("That task isn't in your Task List. Let's try again.")
      time.sleep(2)
  elif menu.strip() == "4" or menu.strip().lower() == "view" or menu.replace(" ", "").lower() == "viewlist": # VIEW TASK LIST
    pPrint()
  elif menu.strip() == "5" or menu.strip().lower() == "clear" or menu.replace(" ", "").lower() == "clearlist": # CLEAR TASK LIST
    confirm = input("Enter 1 to confirm you would like to clear your Task List, or enter any other key to return to the Main Menu: ")
    if confirm.strip() == "1":
      taskList = []
    else:
      print("That was almost a huge mistake! Returning to the Main Menu.")
      time.sleep(2)
