dicionario = {
  "testando": 2,
  "nome": "Leandro",
  "idade": 32
}

print(dicionario)

print("nome" in dicionario)
print("sobrenome" in dicionario)

if "nome" in dicionario:
  print("O seu nome é %s" % dicionario["nome"])

if "sobrenome" in dicionario:
  print("O seu sobrenome é %s" % dicionario["sobrenome"])
