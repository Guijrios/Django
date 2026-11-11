# Demo Django - Parte 3: Relacionamento 1:N

Este repositório contém a entrega da **Parte 3** do roteiro de evolução do projeto `demo-django` para a disciplina de Programação Web. Nesta etapa, foi implementado o relacionamento de banco de dados um-para-muitos (1:N) utilizando o ORM do Django.

* **Novo Modelo `Categoria`:** Criação da tabela de categorias no banco de dados SQLite.
* **Chave Estrangeira (ForeignKey):** Atualização do modelo `Mensagem` para incluir uma referência à `Categoria` (relacionamento 1:N), permitindo mensagens sem categoria (`null=True`, `blank=True`) e configurando `on_delete=models.SET_NULL`.
* **Painel Administrativo:** Registro do novo modelo `Categoria` no `admin.py` e adição de filtros (`list_filter`) na listagem de mensagens.
* **Interface (Templates):** Atualização do arquivo `index.html` para renderizar condicionalmente uma "badge" com o nome da categoria associada a cada mensagem, estilizada com Tailwind CSS.


<img width="1600" height="686" alt="image" src="https://github.com/user-attachments/assets/3cc0282e-6513-4d52-b57a-1be0741d4ab6" />
<img width="1600" height="450" alt="image" src="https://github.com/user-attachments/assets/f3f5e4ee-c68a-4e91-a506-42672fd6257f" />

