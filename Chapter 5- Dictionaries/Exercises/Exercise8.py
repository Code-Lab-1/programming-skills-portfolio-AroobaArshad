Marks = {'Milo Murphy':250, 'Melissa Chase':230, 'Zach Underwood':220,
         'Amanda Lopez':195, 'Sara Murphy':150}

print("Original dictionary:")
print(Marks)

print("Marks greater than 200:")
Result = {key:value for (key, value) in Marks.items() if value >= 200}
print(Result)
