# fome_zero
This repository contains files and scripts to built a company strategy dashboards
# 1. Problema de negócio
A empresa Fome Zero é uma marketplace de restaurantes. Ou seja, seu core
business é facilitar o encontro e negociações de clientes e restaurantes. Os
restaurantes fazem o cadastro dentro da plataforma da Fome Zero, que disponibiliza
informações como endereço, tipo de culinária servida, se possui reservas, se faz
entregas e também uma nota de avaliação dos serviços e produtos do restaurante,
dentre outras informações.
O CEO Guerra também foi recém contratado e precisa entender melhor o negócio
para conseguir tomar as melhores decisões estratégicas e alavancar ainda mais a
Fome Zero, e para isso, ele precisa que seja feita uma análise nos dados da
empresa e que sejam gerados dashboards, a partir dessas análises, para responder
às seguintes perguntas:
## Geral
1. Quantos restaurantes únicos estão registrados?
2. Quantos países únicos estão registrados?
3. Quantas cidades únicas estão registradas?
4. Qual o total de avaliações feitas?
5. Qual o total de tipos de culinária registrados?
## Pais
1. Qual o nome do país que possui mais cidades registradas?
2. Qual o nome do país que possui mais restaurantes registrados?
3. Qual o nome do país que possui mais restaurantes com o nível de preço igual a 4
registrados?
4. Qual o nome do país que possui a maior quantidade de tipos de culinária
distintos?
5. Qual o nome do país que possui a maior quantidade de avaliações feitas?
6. Qual o nome do país que possui a maior quantidade de restaurantes que fazem
entrega?
7. Qual o nome do país que possui a maior quantidade de restaurantes que aceitam
reservas?
8. Qual o nome do país que possui, na média, a maior quantidade de avaliações
registrada?
9. Qual o nome do país que possui, na média, a maior nota média registrada?
10. Qual o nome do país que possui, na média, a menor nota média registrada?
11. Qual a média de preço de um prato para dois por país?

## Cidade
1. Qual o nome da cidade que possui mais restaurantes registrados?
2. Qual o nome da cidade que possui mais restaurantes com nota média acima de
4?
3. Qual o nome da cidade que possui mais restaurantes com nota média abaixo de
2.5?
4. Qual o nome da cidade que possui o maior valor médio de um prato para dois?
Conteúdo licenciado para Aroldo Brancalhao Junior - 281.217.858-20
5. Qual o nome da cidade que possui a maior quantidade de tipos de culinária
distintas?
6. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem
reservas?
7. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem
entregas?
8. Qual o nome da cidade que possui a maior quantidade de restaurantes que
aceitam pedidos online?

## Restaurantes
1. Qual o nome do restaurante que possui a maior quantidade de avaliações?
2. Qual o nome do restaurante com a maior nota média?
3. Qual o nome do restaurante que possui o maior valor de uma prato para duas
pessoas?
4. Qual o nome do restaurante de tipo de culinária brasileira que possui a menor
média de avaliação?
5. Qual o nome do restaurante de tipo de culinária brasileira, e que é do Brasil, que
possui a maior média de avaliação?
6. Os restaurantes que aceitam pedido online são também, na média, os
restaurantes que mais possuem avaliações registradas?
7. Os restaurantes que fazem reservas são também, na média, os restaurantes que
possuem o maior valor médio de um prato para duas pessoas?
8. Os restaurantes do tipo de culinária japonesa dos Estados Unidos da América
possuem um valor médio de prato para duas pessoas maior que as churrascarias
americanas (BBQ)?
Conteúdo licenciado para Aroldo Brancalhao Junior - 281.217.858-20

## Tipos de Culinária
1. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do
restaurante com a maior média de avaliação?
2. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do
restaurante com a menor média de avaliação?
3. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do
restaurante com a maior média de avaliação?
4. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do
restaurante com a menor média de avaliação?
5. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do
restaurante com a maior média de avaliação?
6. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do
restaurante com a menor média de avaliação?
7. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do
restaurante com a maior média de avaliação?
8. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do
restaurante com a menor média de avaliação?
9. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do
restaurante com a maior média de avaliação?
10. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do
restaurante com a menor média de avaliação?
11. Qual o tipo de culinária que possui o maior valor médio de um prato para duas
pessoas?
12. Qual o tipo de culinária que possui a maior nota média?
13. Qual o tipo de culinária que possui mais restaurantes que aceitam pedidos
online e fazem entregas?

# 2. Premissas assumidas para a análise
Marketplace foi o modelo de negócio assumido.
Os 3 principais visões do negócio foram: Visão Countries, Visão Cities e Visão Cuisines.

# 3. Estratégia da solução
O painel estratégico foi desenvolvido utilizando as métricas que refletem as 3 principais visões do modelo de negócio da empresa:
Visão do crescimento de países
Visão do crescimento das cidades
Visão do crescimento dos tipos culinarios
Cada visão é representada pelo seguinte conjunto de métricas.
## Visão do crescimento de países
      a. Quantidade de Restaurantes Registrados por País.
      b. Quantidade de Cidades Registrados por País.
      c. Média de Avaliações feitas por País. 
      d. Média de Preço de um prato para duas pessoas po País.
## Visão do crescimento das cidades
      a. Top 10 Cidades com mais Restaurantes na Base de Dados.
      b. Top 7 Cidades com Restaurantes com média de avaliação acima de 4. 
      c. Top 7 Cidades com Restaurantes com média de avaliação abaixo de 2.5. 
      d. Top 10 Cidades mais Restaurantes com tipos culinários distintos. 
## Visão do crescimento dos tipos culinarios
      a. Melhores Restaurantes dos Principais tipos Culinários.
      b. Top Restaurantes. 
      c. Top Melhores Tipos de Culinárias.          
      d. Top Piores Tipos de Culinárias. 
# 4. Top 3 Insights de dados
Após analisar os dados da empresa Fome Zero e responder às perguntas do CEO, foram obtidos os seguintes insights:
A diversidade de tipos de culinária é um dos pontos fortes da empresa. Com um total de X tipos de culinária registrados, a Fome Zero pode atrair um público amplo e diversificado, atendendo às preferências culinárias dos clientes.
A presença de restaurantes que oferecem serviços como entrega e reservas é um diferencial competitivo. Identificou-se que os restaurantes que oferecem esses serviços possuem, em média, uma maior quantidade de avaliações registradas e um valor médio de um prato para duas pessoas mais alto, indicando que esses serviços agregam valor à experiência do cliente.
A avaliação média dos restaurantes varia de acordo com o tipo de culinária. Observou-se que restaurantes de culinária italiana e japonesa têm, em média, uma avaliação mais alta, enquanto restaurantes de culinária brasileira apresentam uma avaliação média mais baixa. Isso pode indicar oportunidades de melhoria para os restaurantes brasileiros, a fim de melhorar a qualidade dos serviços e produtos oferecidos.


# 5. O produto final do projeto
Painel online, hospedado em um Cloud e disponível para acesso em qualquer dispositivo conectado à internet. O painel pode ser acessado através desse link: https://aroldo-fome-zero.streamlit.app/Countries

# 6. Conclusão
Com base na análise dos dados, é possível concluir que a empresa Fome Zero possui uma plataforma diversificada, com uma ampla variedade de tipos de culinária e serviços oferecidos. A presença de restaurantes que oferecem entrega e reservas mostra-se vantajosa para a empresa, uma vez que esses serviços estão associados a uma maior quantidade de avaliações e um valor médio de prato mais alto. Além disso, a análise das avaliações por tipo de culinária permite identificar oportunidades de melhoria e possíveis áreas de foco para a empresa.
# 7. Próximo passos
1. Análise de sazonalidade: Investigar a existência de padrões sazonais nos dados, como variações no número de avaliações ou na demanda por tipos de culinária ao longo do ano. Isso pode permitir o planejamento de promoções sazonais e ajustes na oferta de restaurantes.
2. Análise de feedback dos clientes: Explorar as avaliações e feedbacks dos clientes de forma mais detalhada, buscando identificar padrões e áreas específicas de melhoria. Isso pode incluir a análise de sentimentos nos comentários dos clientes e a identificação de palavras-chave recorrentes relacionadas a pontos fortes e fracos dos restaurantes.
3. Análise de rentabilidade por restaurante: Avaliar a rentabilidade de cada restaurante registrado na plataforma, levando em consideração fatores como custos operacionais, volume de vendas e preços médios dos pratos. Isso pode ajudar a identificar restaurantes com melhor desempenho financeiro e fornecer insights para otimização de custos.
