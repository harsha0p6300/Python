list=['Harsha','Anudeep','Rakesh']
list.append("Reventh")# ['Harsha', 'Anudeep', 'Rakesh']
list.extend(["Srinath, veda vyas"])# Better than multiple appends
list.insert(2,"op rah")# Insert at index 1
list.remove("Harsha")# Removes the item itself, not index
list.pop(0)  # Removes first item
print(list)
