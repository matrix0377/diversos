"""
Vamos considerar um loop que conta de 1-20, mas ignora todos os números que são múltiplos de 5. 
Neste caso, NÃO poderíamos usar a palavra-chave "break", porque isso encerrará o loop. 
Queremos "continuar" o loop, exceto por alguns números. 

Vamos implementar isto tanto com um loop "while" quanto com um loop "for". 
"""

count = 1

# Implementação do loop WHILE
while count + 1 <= 20:
  if count % 5 == 0:
    print("SKIP")
    count += 1
    continue
  print(count)
  count += 1

  