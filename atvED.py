#!/usr/bin/env python
# coding: utf-8

# In[11]:


import random

class HashDupla:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.primeiro_nivel = [None] * 10
        self.segundo_nivel = [None] * (tamanho // 10)

    def Hash1(self, chave):
        return hash(chave) % 10

    def Hash2(self, chave):
        return hash(chave) % (self.tamanho // 10)

    def Inserir(self, chave, dados):
        hash1 = self.funcao_hash_primerio_nivel(chave)
        hash2 = self.funcao_hash_segundo_nivel(chave)
        
        if self.primeiro_nivel[hash1] is None:
            self.primeiro_nivel[hash1] = [None] * (self.tamanho // 10)
        
        if self.segundo_nivel[hash2] is None:
            self.segundo_nivel[hash2] = []

        self.segundo_nivel[hash2].append((chave, dados))

    def Recuperar(self, chave):
        hash1 = self.funcao_hash_primerio_nivel(chave)
        hash2 = self.funcao_hash_segundo_nivel(chave)

        if self.primeiro_nivel[hash1] is not None and self.segundo_nivel[hash2] is not None:
            for c, dados in self.segundo_nivel[hash2]:
                if c == chave:
                    return dados
        return None


# In[51]:


tabela = TabelaHashDupla(100)
tabela.inserir(144522314, {"Nome": "Esdras","Idade": 25, "Cidade": "Recife"})      
tabela.inserir(123456789, {"Nome": "Maria", "Idade": 25, "Cidade": "Rio de Janeiro"})
tabela.inserir(555555555, {"Nome": "Carlos", "Idade": 40, "Cidade": "Belo Horizonte"})
cpf = int(input("Digite um cpf para procurar: "))
informacoes = tabela.recuperar(cpf)

if informacoes:
    print(f"Informações da pessoa com CPF {cpf}: {informacoes}")
else:
    print(f"Pessoa com CPF {cpf} não encontrada.")


# In[ ]:




