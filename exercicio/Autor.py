class Autor:

    def __innit__(self, nome, ano):     #atributo privado mas método público pois permite verificação 
        self._nome = nome               # _ fracamente privado
        self.__ano = ano                # __ fortemente privado

    def setNome(self, valor):
        if valor != "" and valor != "Adalto":
            set._nome = valor

    def getNome(self):
        return self._nome
    
    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, valor):
        if valor < 2026: 
            self.__ano = valor
    
    def __str__(self):
        #return super().__str__() - polimorfismo 
        txt - "Autor: " + self._nome
        txt += " - Ano: " + self.__ano
        return txt