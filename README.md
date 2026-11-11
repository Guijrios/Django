# Demo Django - Parte 4: Relacionamento N:N (Muitos-para-Muitos)

Guilherme Jesus Rios Silveira 22.2.4076 BCC481 Programação Web 
---


Este repositório contém a entrega da **Parte 4** do roteiro de evolução do projeto `demo-django`. O projeto consiste em uma aplicação web de página única desenvolvida com **Django**, utilizando banco de dados **SQLite**, estilização via **Tailwind CSS** (CDN) e containerização com **Docker**.

Nesta quarta etapa, a estrutura do banco de dados foi expandida para suportar um **relacionamento muitos-para-muitos (N:N)**, permitindo que uma mensagem possua múltiplas tags e uma tag esteja associada a múltiplas mensagens.

* **Novo Modelo `Tag`:** Criação de uma tabela para armazenar palavras-chave, utilizando `SlugField` para garantir URLs amigáveis e `unique=True` para evitar duplicidade
* **Relacionamento Muitos-para-Muitos (`ManyToManyField`):** Inclusão do campo `tags` no modelo `Mensagem`, permitindo a associação N:N entre mensagens e tags sem a necessidade de criar a tabela intermediária manualmente
* **Melhorias no Painel Administrativo:** Registro do modelo `Tag` no `admin.py` e configuração do atributo `filter_horizontal` para criar uma interface de seleção dupla (disponíveis/escolhidas) mais intuitiva no cadastro de mensagens
* **Interface (Templates):** Atualização do arquivo `index.html` para iterar sobre a relação N:N (`m.tags.all`) e exibir as tags cadastradas em formato de *hashtags* logo abaixo do conteúdo de cada mensagem.

<img width="1600" height="767" alt="image" src="https://github.com/user-attachments/assets/ef9c2fd7-0f95-4570-a17a-dd9fcf91f3b2" />
<img width="1600" height="810" alt="image" src="https://github.com/user-attachments/assets/8a501fb8-6d92-4938-be0a-a87eb22c550a" />
<img width="1600" height="507" alt="image" src="https://github.com/user-attachments/assets/c6066f0d-2c81-4281-a739-594a02d4335d" />
<img width="1600" height="584" alt="image" src="https://github.com/user-attachments/assets/6a756ea4-f867-44c8-abf5-0164f38f7f36" />


