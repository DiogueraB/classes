from girafa import Girafa # Do arquivo girafa importa Girafa

girafa = Girafa("Melman", 4.15, "Amarela e Marrom", 32, "Nova York") 
girafa2 = Girafa("Gloria", 5, "Amarela e Marrom", 30, "Africa Central")

print(girafa.nome)
girafa2.comer('folhas')
girafa2.comer('folhas')

girafa2.fome()
girafa2.andar()
girafa2.respirar()

filhote = girafa2.reproduzir(girafa)

print(filhote.nome)
filhote.fome()
filhote.andar()
filhote.respirar()