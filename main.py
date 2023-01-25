class Pessoa:
  def __init__(self,nome = 0,idade = 0):
    self.nome = nome
    self.idade = idade
    
  def get_nome(self):
   print(self.nome)

  def set_nome(self,v):
   if self.nome ==0:
    self.nome = v
   else:
     print('Ja foi colocado o nome')

  def get_idade(self):
    print(self.idade)

  def set_idade(self,v):
    if v  >=18:
      self.idade = v
    
    else:
      print('Deve ser adulto')


class ContaPoupança:
  def __init__(self,agência,número_da_conta,saldo,autentificação = False):
    self.agência = agência
    self.número_da_conta = número_da_conta
    self.saldo = saldo
    self.autentificação = autentificação

  def sacar(self,v):
   if self.agência in Banco1.contas:
     self.saldo+=v
   else:
     print('não foi autentificado')

  def mostrar_saldo(self):
    print(self.saldo)
  
class ContaCorrente(ContaPoupança):
  def __init__(agência,número_da_conta,saldo,autentificação = False):
   super().__init__(agência,número_da_conta,saldo,autentificação = False)
  
  def depositar(self,v,pessoa):
    if self.saldo >=0 and self.agência in Banco1.contas:
     self.saldo =-v
     self.saldo =+pessoa
    else:
     print('saldo indísponivel ou não autenficado')

  

class Banco:
  def __init__(self,clientes = [],contas =[]):
    self.clientes = clientes
    self.contas = contas 

  def autentificar(self,cliente,conta):
    self.clientes.append(cliente)
    self.contas.append(conta)
    
    
    

Cliente1 =Pessoa()
Cliente1.set_idade(18)
Cliente1.set_nome('João Antonio')
Conta1 = ContaCorrente(4534,54455,500)
Banco1 = Banco()
Banco1.autentificar(Cliente1.nome,Conta1.agência) 
Conta1.sacar(400)