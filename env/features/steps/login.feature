Feature: Login na loja do Instituto Joga Junto

    Como funcionário do site do Instituto Joga junto
    Quero preencher os dados de login
    Para acessar a página de produtos

@login
    Scenario: Login na página do Instituto com sucesso
    Given que eu estou na página do Instituto
    When eu preencher os campos de login, já tendo um cadastro
    And apertar o botão 'Iniciar sessão'
    Then a tela de cadastro de produtos é mostrada.
    #Then eu devo logar com sucesso

@deslog
    Scenario: Deslogar da página do Instituto
    Given que eu estou logado na página do Instituto
    When clicar em 'Perfil'
    And em 'LogOut'
    Then retorno para a página inicial do Insituto