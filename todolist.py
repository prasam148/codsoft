Task_list=[]

def add_task():
   task_add=input("enter task to add in list:")
   Task_list.append(task_add)
   print(f"task {task_add} successfully added in list")

def update_task():
    task_index=int(input("enter task index to update from list:"))-1
    new_task=input("Enter new task for updating old task:")
    if len(Task_list) > task_index >= 0:
       Task_list[task_index] = new_task
       print(f" task updated Sucessfully ")
    else:
       print("No tasks in the list")

def remove_task():
    display_task()
    task_index=int(input("enter task index to update from list:"))-1
    if len(Task_list) > task_index >= 0:
      task_remove = Task_list.pop(task_index)
      print(f" task {task_remove} removed Sucessfully ")
    else:
       print("No tasks in the list")
 

def display_task():
    if Task_list:
      print("Task list: ")
      for i, task_view in enumerate(Task_list):
        print(f"{i+1}.{task_view}")
    else:
      print("No tasks in the list")



def main():
  
  while True:
    print("*****List application*****")
    print("1. Add task")
    print("2. Update task")
    print("3. Remove task")
    print("4. Display task")
    print("5. Exit from List application")

    choose=int(input("choose options (1 to 5):" ))

    if choose == 1:
       add_task()
    elif choose == 2:
       update_task()
    elif choose == 3:
       remove_task()
    elif choose == 4 :
       display_task()
    elif choose == 5:
       print("Exit from list, bye")
       break
    else:
       print("Invalid choose, please enter valid option")

if __name__=="__main__":
     main()