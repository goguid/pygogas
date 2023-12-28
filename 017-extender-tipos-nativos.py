class Lista(list):
    def prepend(self,item):
        self.insert(0,item)

lista=Lista([18,2,13])
lista.append(74)
lista.prepend(76)
print(lista)
lista.sort()
print(lista)