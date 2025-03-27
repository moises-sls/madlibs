with open("historia.txt", "r") as f:
    story = f.read()


words = set() # criando um conjunto para armazenar as variáveis
# isso vai servir para que o usuário não precise repetir
# palavras que ja foram selecionadas anteriormente
start_of_word = -1

target_start = "<"
target_end = ">"

for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i   # se torna o índice correspondente ao começo da palavra
    
    if char == target_end and start_of_word != -1:
        word = story[start_of_word : i+1] #pega as letras do começo até o final da palavra, o ultimo indice é exclusivo, por isso o +1
        words.add(word)
        start_of_word = -1



answers = {}

for word in words:
    answer = input("Digite uma palavra para " + word + ": ")
    answers[word] = answer



for word in words:
    story = story.replace(word, answers[word])


print(story)