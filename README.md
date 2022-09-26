# AmiguBlog

Basicamente eu fiz um projeto simples para extrair padrões de crochê de um blog. 
Com meu código eu consigo pegar o link onde é encontrado o padrão e o link onde é encontrado a imagem do seu respectivo padrão. 
Eu só peguei os links dos padrões de gatos e cães, porque achei desnecessário pegar mais do que isso para um projeto demonstrativo uma vez que para pegar os outros seria da mesma forma. 
A RestAPI eu fiz com o uso do Flask.
Em relação a hospedagem e interface gráfica da API, eu tive dificuldades, pois não tenho experiência com front-end, apesar de me interessar e na grade do meu curso logo logo terei que aprender mais.
Eu tentei a hospedagem tanto nos servidores AWS quanto nos servidores Heroku, porém, sem sucesso.
Uma outra alternativa que achei, foi fazer uma interface gráfica com o Tkinter, porém não gastei tanto tempo com a personalização para ser aparentemente bonito, mas é totalmente funcional.
As partes mais difíceis do projeto para mim, foram a hospedagem e a criação da interface gráfica, o restante eu ja tinha conhecimento de como fazer.
Na RESTAPI basicamente é só usar as rotas para executar os código feitos para extração de cada uma das funções. 
As criação das funções de scraping estão explicadas no próprio código dentro de seus respectivos .py files "cats.py" e "dogs.py".
A interface gráfica feita pelo Tkinter foi feita de forma que vc clique no botão "+" e "-" para mudar o numero do padrão que você quer acessar.
Quando você escolher o padrão que vc quiser acessar, é só clicar nos botões Dogs ou Cats para receber os links dos padrões respectivos ao número "Pattern"

Thiago Velasco 
linkedin.com/in/thiago-velasco-7204b3218/
