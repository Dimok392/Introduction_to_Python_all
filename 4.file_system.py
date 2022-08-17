
with open ('test.txt', 'w', encoding='utf-8') as file:
    file.writelines(['hello world!\n', 'how are you?\n', 'i am fine\n'])

file= open ('test.txt', 'a', encoding='utf-8')
file.writelines('2\n')
file.write('4')
file.close()