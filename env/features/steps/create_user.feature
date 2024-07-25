Feature: Cadastro de login na loja do Instituto Joga Junto

    Como funcionário do site do Instituto Joga junto
    Quero preencher os dados de login de cadastro
    Para acessar a página de produtos

@create
    Scenario: Criaçao de novo usuário na página do Instituto com sucesso
    Given que eu estou na página do Instituto
    And eu clico em 'Clique aqui e registre-se'
    When eu preencho os campos com os dados 
    And clicar em 'Criar conta'
    Then será exibido 'Usuário cadastrado com sucesso'