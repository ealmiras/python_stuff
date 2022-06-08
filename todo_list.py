todo_list = []
completed = []

while True:
    for i in range(len(todo_list)):
        print(f"{i + 1}) {todo_list[i]}")
    print("*" * 20)
    print("Enter a command. Type 'h' for help: ")
    todo = input("> ")
    if todo == "h":
        print("TODO LIST HELP")
        print("Type 'q' to quit")
        print("To add a todo to the list, type it and hit enter")
        print("To complete a todo enter its number")   
    elif todo == "q":
        break
    elif todo.isnumeric():
        idx = int(todo) - 1
        if idx >= len(todo_list):
            print("THERE IS NO TODO WITH THAT NUMBER!")
        else:
            completed.append(todo_list.pop(idx))
    else:
        todo_list.append(todo)

print(f"Today you completed {len(completed)} todos:")
for i in range(len(completed)):
    print(f"* {completed[i]}")