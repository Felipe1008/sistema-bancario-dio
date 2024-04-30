# Sistema Bancário
Repositório para armazenar o código do desafio DIO de implementar um sistema bancário simples com o objetivo de implementar as operações de Depositar, Sacar e Consultar Extrato.

Para cada operação temos uma série de requisitos a serem respeitados, vejamos:

## Versão 1

### Depositar
- Deve ser possível depositar somente valores positivos;
- A versão 1 do projeto trabalha com apenas 1 usuário;
- Todos depósitos devem constar no Extrato.
### Sacar
- O sistema deve permitir no máximo 3 saques diários;
- O sistema tem um limite máximo de saque de R$500,00;
- Caso o usuário não tenha saldo em conta o sistema deverá informá-lo;
- Todos saques devem constar no Extrato.
### Extrato
- Deve listar todos saques e depósitos realizados na conta;
- No fim da listagem deve ser exibido o saldo atual da conta.

## Versão 2:
O objetivo da versão 2 desse código é otimizá-lo e modularizá-lo. Além disso, criaremos algumas outras funções que serão especificadas a seguir:
### Depositar
- Deve receber argumentos apenas por posição (positional only);
- Deve seguir todos requisitos da versão 1.
### Sacar
- Deve receber argumentos apenas por nome (keyword only);
- Deve seguir todos requisitos da versão 1.
### Extrato
- Deve receber argumentos por posição e nome;
- Deve seguir todos requisitos da versão 1.
### Criar Usuário
- Deve armazenar os usuários em uma lista;
- Um usuário é composto por nome, data de nascimento, cpf e endereço;
- Não podemos cadastrar dois usuários com o mesmo CPF.
### Criar Conta Corrente
- Deve armazenar contas em uma lista;
- Uma conta é composta por agência, número da conta e usuário;
- O número da conta é sequencial e deve iniciar em 1;
- O número da agência é fixo: "0001";
- O usuário pode ter mais de uma conta, mas uma conta pertence somente a um usuário.

