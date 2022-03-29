'''
 Descobrindo tudo sobre o telefone
''' 

from phonenumbers import carrier
from phonenumbers import geocoder
import phonenumbers

#Ajuste do telefone para usar o phonenumbers
telefone = "+5521999999999"
telefone_ajustado = phonenumbers.parse(telefone)
print(telefone_ajustado)

#Descobrir a localização do telefone
local = geocoder.description_for_number(telefone_ajustado, 'pt-br')
print(local)

#Formatando um telefone que foi inserido em um formulário
telefone_formulario = "21999999999"
telefone_formulario_ajustado = phonenumbers.parse(telefone_formulario, "BR")

telefone_formatado = phonenumbers.format_number(
    telefone_formulario_ajustado, phonenumbers.PhoneNumberFormat.NATIONAL)

telefone_internacional = phonenumbers.format_number(
    telefone_formulario_ajustado, phonenumbers.PhoneNumberFormat.INTERNATIONAL)

print(telefone_formatado)

print(telefone_internacional)

#Descobrir a operadora do telefone
operadora = carrier.name_for_number(telefone_ajustado, 'pt-br')

print(operadora)

