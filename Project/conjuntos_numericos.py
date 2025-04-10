# Importação de bibliotecas
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

#Definindo os conjuntos numéricos 
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

#Operações utilizando os conjuntos

uniao = A.union(B)          # A ∪ B
intersecao = A.intersection(B)  # A ∩ B
diferenca_AB = A.difference(B)  # A - B
diferenca_BA = B.difference(A)  # B - A
simetrica = A.symmetric_difference(B)  # A Δ B (diferença simétrica)

#Exibindo os resultados

print(f"Conjunto A: {A}")
print(f"Conjunto B: {B}")
print(f"A união B: {uniao}")
print(f"A interseção B: {intersecao}")
print(f"A - B: {diferenca_AB}")
print(f"B - A: {diferenca_BA}")
print(f"A Δ B (diferença simétrica): {simetrica}")

#Criando diagrama de Venn

plt.figure(figsize=(8, 6))
venn = venn2(subsets=(len(A - B), len(B - A), len(intersecao)),
             set_labels=('Conjunto A', 'Conjunto B'))
venn.get_label_by_id('10').set_text('\n'.join(map(str, A - B)))
venn.get_label_by_id('01').set_text('\n'.join(map(str, B - A)))
venn.get_label_by_id('11').set_text('\n'.join(map(str, intersecao)))

plt.title('Diagrama de Venn: Conjuntos A e B')
plt.show()