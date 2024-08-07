import pandas as pd

dados = open('logs.csv', mode='r', encoding='utf-8').read()
teste = dados.split('\n')

mestre = 0
emp_semente = 0
emp_fertilizante = 0
emp_agrotoxico = 0
emp_maquinas = 0
prefeito_at = 0
prefeito_cid = 0
fiscal_at = 0
fiscal_cid = 0
vereador_at = 0
vereador_cid = 0
agricultor_at = 0
agricultor_cid = 0
# print(teste)
for i in range(len(teste)):
    if 'EmpSem' in teste[i]:
        emp_semente+=1
    if 'EmpFer' in teste[i]:
        emp_fertilizante+=1
    if 'EmpMaq' in teste[i]:
        emp_maquinas+=1
    if 'EmpAgr' in teste[i]:
        emp_agrotoxico+=1
    if 'PrefAT' in teste[i]:
        prefeito_at+=1
    if 'PrefCD' in teste[i]:
        prefeito_cid+=1
    if 'FisAT' in teste[i]:
        fiscal_at+=1
    if 'FisCD' in teste[i]:
        fiscal_cid+=1
    if 'VerAT' in teste[i]:
        vereador_at+=1
    if 'VerCD' in teste[i]:
        vereador_cid+=1
    if 'AT1' in teste[i]:
        agricultor_at+=1
    if 'CD1' in teste[i]:
        agricultor_cid+=1
    if 'Mestre' in teste[i]:
        mestre+=1

print(f'emp semente:',emp_semente,'emp fertilizantes:',emp_fertilizante,'emp agrotoxicos:',emp_agrotoxico,'emp maquinas:',emp_maquinas)
print(f'prefeito atlantis:',prefeito_at,'prefeito cidadela:',prefeito_cid,'vereador atlantis:',vereador_at,'vereador cidadela:',vereador_cid)
print(f'fiscal atlantis:',fiscal_at,'fiscal cidadela:',fiscal_cid,'agricultor atlantis:',agricultor_at,'agricultor cidadela:',agricultor_cid,'mestre:',mestre)