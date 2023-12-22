![airbnb](img/airbnb.png)


# Projeto de Previsão de Preços para Anúncios no Airbnb - Rio de Janeiro

# 1. Contexto
No universo do Airbnb, a oferta de acomodações é diversificada, indo desde quartos simples até propriedades inteiras. Cada anfitrião é incentivado a criar anúncios detalhados para destacar as características únicas de seus imóveis. A variedade de personalizações inclui informações como a quantidade mínima de diárias, preço, número de quartos, regras de cancelamento, taxas extras para hóspedes adicionais e requisitos de verificação de identidade do locador.

# 2. Objetivo do Projeto
Este projeto visa construir um modelo de previsão de preços para auxiliar anfitriões e locatários no Rio de Janeiro. A ideia é fornecer uma ferramenta acessível para que proprietários possam estabelecer preços justos para suas diárias, enquanto também ajuda locatários a avaliar se um imóvel está com preço atrativo em comparação com propriedades similares.

# 3. Dados Disponíveis
Os dados utilizados no projeto foram extraídos do Kaggle e abrangem o período de abril de 2018 a maio de 2020, com exceção do mês de junho de 2018. As informações incluem os preços dos imóveis em reais (R$) e suas características específicas para cada mês.

https://www.kaggle.com/allanbruno/airbnb-rio-de-janeiro

# 4. Expectativas Iniciais
Algumas hipóteses iniciais foram levantadas para direcionar a análise:

**Sazonalidade:** A sazonalidade pode desempenhar um papel crucial, especialmente em meses como dezembro, que historicamente podem apresentar preços mais elevados no Rio de Janeiro.

**Localização:** Dada a diversidade da cidade, a localização do imóvel é esperada para ser um fator determinante nos preços, influenciando elementos como segurança, beleza natural e proximidade a pontos turísticos.

**Adicionais/Comodidades:** A presença ou ausência de comodidades adicionais pode impactar significativamente os preços, dado o contexto de prédios e casas antigas no Rio de Janeiro.

# 5. Principais Observações Retiradas do Modelo de Previsão:
### 1. Variação de Preços ao Longo do Ano:
Ao analisar alguns testes do modelo, foi possivel observar uma variação significativa nos preços sugeridos entre os meses 8 e 12, mesmo quando todas as características dos imóveis eram idênticas, essa diferença revelou uma influência sazonal substancial, indicando que fatores externos podem impactar os preços independentemente das características intrínsecas dos imóveis.

### 2. Impacto da Remoção de Outliers nas Áreas Próximas à Praia para o Modelo:
A remoção de outliers revelou uma tendência interessante seguida pelo modelo: áreas próximas à praia, provavelmente onde estava concentrado muitos desses outliers, apresentaram preços mais baixos do que o esperado. Isso indica que após a remoção de valores altos, os lugares mais próximos da praia não demonstraram o preço elevado esperado, algo que é comum em qualquer localidade proxima a alguma praia, indicando uma possível distorção na previsão dessas localidades pelo modelo.

### 3. Diferença de Preços entre Apartamentos e Casas:
Uma análise comparativa entre testes de previsões utilizando apartamentos e casas, considerando características e localização semelhantes, foi possivel perceber que apartamentos tendem a ter preços mais altos, esta observação sugere que, além das características específicas, o tipo de propriedade desempenha um papel crucial na determinação dos preços para o modelo, com casas sendo uma opção mais acessível em comparação com apartamentos.

### 4. **Adaptação do Modelo para Deployment:**
Inicialmente, utilizou-se o modelo Extratrees, que apresentou bom desempenho com R² em torno de 97.57%. No entanto, devido ao tamanho do modelo, optou-se pelo XGBoost para permitir o deploy do projeto. Mesmo assim, foi necessário reduzir a complexidade do modelo para que fosse possivel o upload do painel, resultando na diminuição de algumas métricas, como a diminuiçãodo R², e no aumento significativo do MAPE. Essas adaptações foram essenciais para manter a funcionalidade do painel em produção.

# 6. O Produto Final do Projeto
O resultado final deste projeto é um painel online acessível em qualquer dispositivo conectado à internet. Hospedado na nuvem, o painel oferece uma interface intuitiva para fornecer características específicas de imóveis, utilizando o modelo de previsão desenvolvido, o painel realiza previsões de preços permitindo que anfitriões e locatários obtenham estimativas de preços com base nas características do local.
Este painel representa não apenas a conclusão do projeto, mas também uma ferramenta prática e valiosa para auxiliar na hora da escolha dos valores para propriedades no Rio de Janeiro.

O painel pode ser acessado através desse link: https://airbnbrioproject.streamlit.app/

# 7. Conclusão 
O Objetivo do projeto envolveu a construção e treinamento de um modelo de machine learning capaz de prever os preços com base nas características dos imóveis. Ao testar o modelo, foi possivel obter algumas previsões e insights significativos.
Em resumo, este projeto não apenas atingiu seus objetivos iniciais, mas também forneceu uma ferramenta prática para que anfitriões e locatários possam ter uma base de valores cobrados por imoveis, baseado em suas carcteristicas.

# 8. Proximos Passos
  
### 1. Tratamento de Outliers para Aprimorar a Precisão Local:
Adotar estratégias específicas para preservar a integridade dos dados sem remover os outlier para ter uma previsão de valor mais precisa baseada em localização.

### 2. Expansão para Dados de Múltiplas Cidades:
Procurar por bases de dados mais abrangentes que incluam informações de diversas cidades para aumentar a abrangencia do modelo.

### 3. Avaliação de Métricas de Desempenho:
Buscar uma compreensão mais granular da eficácia do modelo em diferentes contextos, identificando áreas de melhoria específicas.

