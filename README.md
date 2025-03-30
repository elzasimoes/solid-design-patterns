# **Sistema de Gerenciamento de Pedidos**

## **Descrição**

Este projeto implementa um sistema de gerenciamento de pedidos que simula um fluxo de pedidos de clientes, incluindo cálculo de totais, notificações, pagamento e atualização de status.

---

## **Funcionalidades**

- **Cadastro de Clientes e Itens**: Gerencia informações de clientes e produtos.
- **Gestão de Pedidos**: Suporte a pedidos para delivery e retirada.
- **Sistema de Pagamento**: Simulação de processamento de pagamentos.
- **Notificações**: Envio de notificações por e-mail e SMS.
- **Atualização de Status**: Rastreamento e notificação do status do pedido.
---

## **Tecnologias Utilizadas**

- **Python 3.10+**
- Design Patterns: _Factory Method, Template, Strategy, Facade, Observer_.
- Princípios **SOLID**.

S - Princípio da Responsabilidade Única
Aplicamos este princípio ao garantir que cada classe tivesse uma única responsabilidade. Isso nos permitiu modularizar o código, tornando-o mais legível e fácil de testar. Por exemplo, ao criar classes para diferentes tipos de pedidos, garantimos que cada uma delas tivesse uma função clara e específica.

O - Princípio Aberto-Fechado
Implementamos o princípio ao projetar o sistema de forma que ele fosse aberto para extensão, mas fechado para modificação. Utilizamos herança e interfaces para permitir que novas funcionalidades fossem adicionadas sem alterar o código existente. Por exemplo, ao adicionar novos tipos de pagamento, fazemos isso estendendo classes base sem modificar diretamente o código original.

L - Princípio da Substituição de Liskov
Aplicamos esse princípio ao garantir que as subclasses pudessem ser usadas no lugar de suas classes base sem causar erros. Ao implementar a classe base para pagamentos, suas subclasses (como Pagamento com Cartão e Pagamento com Boleto) foram desenhadas para serem intercambiáveis, mantendo a integridade do sistema.

I - Princípio da Segregação de Interface
Com esse princípio, garantimos que as interfaces fossem específicas e não forçasse implementações desnecessárias. Por exemplo, ao criar diferentes tipos de notificações, as interfaces de envio de notificações foram separadas para que cada tipo (SMS, Email) implementasse apenas o que era necessário para sua funcionalidade.

D - Princípio da Inversão de Dependência
Esse princípio foi aplicado ao garantir que as classes dependessem de abstrações, e não de implementações concretas. Ao utilizar injeção de dependência, as classes de pagamento, por exemplo, não estavam diretamente acopladas às suas implementações, permitindo flexibilidade e facilitando a manutenção e os testes.

Ao aplicar os princípios SOLID no seu projeto, garantimos um código mais modular, facilitando a manutenção, expansão e entendimento da aplicação. Isso reduz o acoplamento entre as partes do sistema, tornando-o mais resiliente a mudanças, além de incentivar a reutilização de componentes. Assim, construímos uma base sólida para o crescimento do nosso projeto e na melhoria contínua do fluxo de trabalho.

## **Estrutura do Projeto**

```
.
├── cliente.py
├── item.py
├── main.py
├── notificacao/
│   ├── notificacao.py
│   ├── notificacao_email.py
│   ├── notificacao_sms.py
│   └── notificacao_facade.py
├── observador/
│   └── observador_status.py
├── pagamento/
│   ├── pagamento.py
│   ├── pagamento_cartao.py
│   └── pagamento_pix.py
├── pedido/
│   ├── pedido.py
│   ├── pedido_delivery.py
│   └── pedido_retirada.py
└── README.md
```

---

## **Como Executar**

1. Acesse o arquivo `main.py`.
2. Execute o programa:
   ```bash
   python main.py
   ```

---

## **Exemplo de Uso**

- **Cadastrar Cliente e Itens**:
  Crie um cliente e adicione itens ao pedido.
- **Criar Pedido**:
  Escolha entre _delivery_ ou _retirada_.
- **Efetuar Pagamento**:
  Simule pagamentos via Pix ou Cartão.
- **Receber Notificações**:
  Clientes recebem notificações do status do pedido.

---

## **Autoria**

Projeto desenvolvido como estudo dos princípios **SOLID** e padrões de design para organização de software escalável e modular.

Feito pela Escola de Programação da Alura!

Fique à vontade para contribuir! 🎉
