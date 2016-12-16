running = True
shopping_list = []

print("Enter you shopping list items one at a time")
print("Enter 'DONE' to exit and display your list")

while running:
	
	new_item = input("> ")

	if new_item == 'DONE':
		running = False

		for item in shopping_list:
			print(item)
	else:
		shopping_list.append(new_item)