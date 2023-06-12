

with open(r"D:\Mine\Programming\Python\CourseUdemy\projects\Mail Merge Project Start\Input\Letters\starting_letter.txt", 'r') as letter:
    letter = letter.read()

with open(r'D:\Mine\Programming\Python\CourseUdemy\projects\Mail Merge Project Start\Input\imena\invited_names.txt', 'r') as names:
    names = names.readlines()

for name in names:
    name = name.strip()
    personalize_letter = letter.replace('[name]', name)
    with open(f"D:\Mine\Programming\Python\CourseUdemy\projects\Mail Merge Project Start\Output\ReadyToSend\letter_for_{name}.txt", 'w') as done:
        done.write(personalize_letter)


