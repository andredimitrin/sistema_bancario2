# Sistema Bancário Simples 2.0
Este é um projeto de um Sistema de Banco Simples, implementado em Python, que permite criar usuários, criar contas correntes vinculadas aos usuários, realizar saques, depósitos e consultar extratos.

### Funcionalidades
O Sistema de Banco Simples possui as seguintes funcionalidades:

1. Criar Usuário: Permite cadastrar um novo usuário no sistema, fornecendo informações como nome, data de nascimento, CPF e endereço.

2. Criar Conta Corrente: Permite criar uma nova conta corrente vinculada a um usuário existente. O usuário deve fornecer o número da conta corrente para realizar transações.

3. Realizar Saque: Permite realizar saques de uma conta corrente, desde que o valor não exceda o saldo disponível, o limite de saques ou o limite de saldo.

4. Realizar Depósito: Permite realizar depósitos em uma conta corrente, atualizando o saldo disponível e o extrato da conta.

5. Consultar Extrato: Permite verificar o extrato completo de uma conta corrente, mostrando as transações realizadas e o saldo atual.

6. Listar Contas: Exibe todas as contas correntes cadastradas no sistema, junto com as informações dos titulares.

7. Listar Usuários: Exibe todos os usuários cadastrados no sistema, com suas respectivas informações pessoais.

### Como Executar
1. Certifique-se de que você tenha o Python instalado em seu sistema.

2. Baixe ou clone este repositório em sua máquina local.

3. Navegue até o diretório do projeto.

4. Execute o arquivo index.py para iniciar o Sistema de Banco Simples.

5. Siga as instruções exibidas no menu para realizar as operações desejadas.

### Requisitos
O projeto foi implementado em Python 3.x e não possui requisitos adicionais. Todo o código necessário está contido no próprio arquivo index.py.

### Sair do Programa
Ao selecionar a opção "Sair", o sistema bancário será encerrado, e o programa será finalizado.

## Detalhes de Implementação
O sistema bancário é implementado em Python e utiliza um loop simples while True para apresentar o menu principal repetidamente até que o usuário escolha sair. O saldo da conta (saldo), limite de saque (limite) e histórico de transações (extrato) são armazenados em variáveis.

O sistema impõe regras específicas para transações de depósito e saque, incluindo a validação dos valores informados e a verificação se a conta possui saldo suficiente e se o usuário não excedeu o limite de saque. Se uma transação falhar, uma mensagem de erro apropriada é exibida ao usuário.

## Vídeo de Demonstração
Você pode assistir a um vídeo de demonstração do sistema bancário simples no seguinte link: [Inserir Link do Vídeo Aqui]
