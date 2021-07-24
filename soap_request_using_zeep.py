"""
Simples integração com requisição de serviço API SOAP utilizando o zeep

"""

from zeep import Client

client = Client('http://soapclient.com/xml/soapresponder.wsdl')

# Parâmetros do serviço (serviço Method1 especificado no arquivo wsdl)
bstrParam1 = '{Teste do Parametro 1}'
bstrParam2 = '{Teste do Parametro 2}'

# Chamada do serviço
result = client.service.Method1(bstrParam1,
                                bstrParam2)

print(result)

# Validação do resultado
if __name__ == '__main__':
    assert result == f'Your input parameters are {bstrParam1} and {bstrParam2}'
