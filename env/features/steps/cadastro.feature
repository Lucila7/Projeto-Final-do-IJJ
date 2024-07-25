Feature: Cadastro de novo produto da loja

    Como funcionário do site do Instituto Joga junto
    Quero preencher o formulário de cadastro 
    Para enviar um novo produto

@cad
    Scenario: Cadastro de um novo produto com sucesso
    Given que eu estou na página de cadastro de produto
    And eu aperto no botão "+ Adicionar"
    When eu preencher o formulário com os dados do produto
    And apertar no botão de "ENVIAR NOVO PRODUTO"
    Then eu devo ver a mensagem de sucesso "Produto cadastrado com sucesso" 
