# Skills Resolução de problemas usando Python

Este é um teste para verificar suas habilidades em resolução de problemas, conhecimento matemático básico e linguagem de programação Python

# Problema a resolver.

Você tem a oportunidade de fazer um investimento comprando alguns ativos financeiros com desconto.
Você pagará por esses ativos R $ 300.000,00 (trezentos mil reais) no dia D.
Esse investimento contém muitos ativos e você deseja saber qual é a taxa interna do investimento.

Além de calcular a taxa interna de investimento, você deseja comparar se esse investimento é melhor que uma taxa Selic.

# Voce tem que:
Compreender o arquivo CSV e como ele está relacionado aos conceitos de taxa interna de investimento no fluxo de caixa irregular;

# Exercício proposto
Crie um aplicativo Python que execute as seguintes tarefas:

- Leia um arquivo CSV com os ativos;

- Calcule a TIR (você deve criar seu próprio algoritmo (não use nenhuma função matemática python para isso), queremos testar seu pensamento lógico aqui

- consumir um serviço público da web que retorne a taxa Selic do dia;

- Mostra a TIR calculada e a taxa Selic no console;

- Armazene as informações do arquivo CSV, a taxa de IRR e Selic calculada em um banco de dados na memória - Sinta-se à vontade para usar a estrutura ou o quadro que desejar.

- Crie uma imagem do Docker com o aplicativo pronto para uso;

# Testes unitários
- Crie testes de unidade com 50% de cobertura de código





# TIR - 
# http://prorum.com/?qa=4563/matematica-financeira-com-python
# https://medium.com/@alegeorgelustosa/introdu%C3%A7%C3%A3o-ao-mercado-financeiro-com-python-3383ebecddf7


Vamos agora calcular a taxa interna de retorno. Lembre-se que a TIR é a taxa de juros que zera o valor presente de um fluxo de caixa. No exemplo a seguir, o autor utiliza uma função do Excel para fazer esse cálculo. Por isso, vamos utilizar a função irr() do módulo numpy, que também calcula a taxa interna de retorno.