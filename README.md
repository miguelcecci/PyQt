# PyQt

## Requisitos
>python 2.7.12
>mongodb 3.6.6

## Bibliotecas
>PyQt4
>pymongo
>datetime
>hashlib

## Banco
>Collection users
--> user - contem o nome de login dos usuarios
--> pass - contem a chave de verificaçao da senha do usuario, criptografado usando sha224

>Collection compras
--> operador - contem o nome do usuario que cadastrou a compra
--> data - contem a data em que a compra foi cadastrada, formato ISO
--> cpf - cpf do cliente que realizou a compra
--> valor - o valor da compra
