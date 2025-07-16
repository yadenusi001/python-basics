#create an empty list

todo_list = [] 
print("Your to-do list:", todo_list) 

todo_list.append("Buy groceries") 
todo_list.append("Finish homework") 
todo_list.append("Call mom") 

print("Updated list:", todo_list)

todo_list.insert(1, "Pay bills") 
print("After inserting a task:", todo_list) 

print("First task:", todo_list[0]) 
print("Last two tasks:", todo_list[-2:]) 

done_task = todo_list.pop(2) 
print("You completed:", done_task) 
print("To-do list after removal:", todo_list) 

todo_list[0] = "Buy groceries and snacks" 
print("After modifying a task:", todo_list) 

print("Here’s what you still need to do:") 

