f = open('text.txt', 'r', encoding='utf-8')
text = f.read()
print(text)
f.close()


f = open('text.txt', 'w', encoding='utf-8')
text = 'Новый текст'
f.write(text)
f.close()

with open('text.txt', 'r', encoding='utf-8') as f:
    print(f.read())