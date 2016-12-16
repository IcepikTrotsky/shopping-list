shopping_list = []

print("Enter you shopping list items one at a time")
print("Enter 'DONE' to exit and display your list")

while True:
	
	new_item = input("> ")

	if new_item == 'DONE':
		for item in shopping_list:
			print(item)
		break
	else:
		shopping_list.append(new_item)
