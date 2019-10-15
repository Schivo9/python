import csv

n = raw_input("Digite seu nome")
e = raw_input("Digite seu endereco")
c = raw_input("Digite sua cidade")
est = raw_input("Digite seu estado")
cep = raw_input("Digite seu cep")

print(n)
print(e)
print(c)
print(est)
print(cep)

 
filename = 'test.csv'
with open('test.csv','wb') as f:
    f.write('%s;%s;%s;%s;%s;\n'%(n,e,c,est,cep))
