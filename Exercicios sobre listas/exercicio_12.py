# Exercício 12

# Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine 
# quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

alunos_dados = {
    "Ana Silva": {"idade": 15, "altura": 1.65},
    "Bruno Souza": {"idade": 16, "altura": 1.70},
    "Carlos Oliveira": {"idade": 15, "altura": 1.60},
    "Daniela Lima": {"idade": 17, "altura": 1.75},
    "Eduardo Santos": {"idade": 16, "altura": 1.68},
    "Fernanda Costa": {"idade": 14, "altura": 1.58},
    "Gabriel Rodrigues": {"idade": 18, "altura": 1.80},
    "Heloísa Gomes": {"idade": 15, "altura": 1.62},
    "Igor Martins": {"idade": 16, "altura": 1.72},
    "Julia Almeida": {"idade": 17, "altura": 1.77},
    "Kevin Ribeiro": {"idade": 15, "altura": 1.66},
    "Larissa Carvalho": {"idade": 14, "altura": 1.55},
    "Matheus Lopes": {"idade": 16, "altura": 1.71},
    "Natália Araujo": {"idade": 18, "altura": 1.82},
    "Otávio Barbosa": {"idade": 15, "altura": 1.64},
    "Patricia Melo": {"idade": 17, "altura": 1.76},
    "Quirino Teixeira": {"idade": 16, "altura": 1.69},
    "Rafaela Rocha": {"idade": 14, "altura": 1.57},
    "Samuel Cardoso": {"idade": 15, "altura": 1.63},
    "Thiago Nogueira": {"idade": 18, "altura": 1.85},
    "Ursula Mendes": {"idade": 16, "altura": 1.73},
    "Vinícius Freitas": {"idade": 17, "altura": 1.78},
    "Wanessa Vieira": {"idade": 15, "altura": 1.67},
    "Xavier Machado": {"idade": 14, "altura": 1.59},
    "Yasmim Ramos": {"idade": 16, "altura": 1.70},
    "Zeca Tavares": {"idade": 17, "altura": 1.79},
    "Amanda Pinheiro": {"idade": 15, "altura": 1.61},
    "Breno Guimarães": {"idade": 18, "altura": 1.81},
    "Camila Castro": {"idade": 16, "altura": 1.74},
    "Diego Fontes": {"idade": 17, "altura": 1.75}
}


total_altura = 0

for c,v in alunos_dados.items():
    total_altura += v["altura"]
    
media_altura = total_altura / len(alunos_dados)

alunos_maior_que_13_menor_que_media = []

for c,v in alunos_dados.items():
    if v['idade'] > 13 and v["altura"] < media_altura:
        alunos_maior_que_13_menor_que_media.append({"aluno": c, "dados": v})
            
print(f"\nQuantidade de alunos com mais de 13 anos que possuem altura inferior à média: {len(alunos_maior_que_13_menor_que_media)}\n")

for aluno_dict in alunos_maior_que_13_menor_que_media:
    nome = aluno_dict['aluno']
    idade = aluno_dict['dados']['idade']
    altura = aluno_dict['dados']['altura']
    
    print(f"{nome} tem {idade} anos e {altura}m de altura.")