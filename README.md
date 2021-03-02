# forms_django

# Alura Receita

👋 Olá, Seja Bem-vindo(a) ao 'Alura Receita'.

# Projeto 'Alura Receita' do curso [Formulários no Django 3: criando e validando dados](https://cursos.alura.com.br/course/django-validando-formularios)

# Aulas

<details>
    <summary>Formulário com Django Forms Ver primeiro vídeo</summary>
    <ul>
        <li>Introdução</li>
        <li>Saudações e ambiente</li>
        <li>Iniciando a aplicação</li>
        <li>Django Form</li>
        <li>Melhorando o visual</li>
        <li>Faça como eu fiz na aula</li>
        <li>A classe forms do Django</li>
        <li>O que aprendemos?</li>
    <ul>
</details>

<details>
    <summary>Alterando e manipulando dados</summary>
    <ul>
        <li>Exibindo dados</li>
        <li>Melhorando o código</li>
        <li>Widget e calendário</li>
        <li>Estilizando os inputs</li>
        <li>Faça como eu fiz na aula</li>
        <li>Dados do formulário</li>
        <li>O que aprendemos?</li>
    <ul>
</details>

<details>
    <summary>Novos campos e alterando o visual</summary>
    <ul>
        <li>Novos campos</li>
        <li>Widget tweaks</li>
        <li>Faça como eu fiz na aula</li>
        <li>Para saber mais</li>
        <li>O que aprendemos?</li>
    <ul>
</details>

<details>
    <summary>Validações</summary>
    <ul>
        <li>Clean_field</li>
        <li>Exibindo mensagem de erro</li>
        <li>Clean</li>
        <li>Validando datas</li>
        <li>Faça como eu fiz na aula</li>
        <li>Clean e Clean_</li>
        <li>O que aprendemos?</li>
    <ul>
</details>

<details>
    <summary>Modelos e formulários</summary>
    <ul>
        <li>Preparando o ambiente</li>
        <li>Criando modelos</li>
        <li>ModelForm</li>
        <li>Formulários</li>
        <li>Faça como eu fiz na aula</li>
        <li>O formulário da Valentina</li>
        <li>O que aprendemos?</li>
        <li>Conclusão</li>
        <li>Parabéns</li>
    <ul>
</details>

# Notas das aulas:

* Introdução: Projeto e subindo servidor  
    Rode no seu terminal:
    ```sh
    sudo docker-compose run web django-admin.py startproject alurapassagens .
    ```

## Sobre o projeto:

### Permissões de arquivos:

Ao se criar migrações, adicionar libs ou qualquer outro comando que crie arquivos dentro do contâiner Docker o proprietário para edição se torna o contâiner, sendo assim você precisará rodar o comando abaixo para alterar essas permissões e você poder editar:

```sh
sudo chown -R $USER:$USER .
```

# Exigências

**:warning: Atenção:** É necessário que os desenvolvedores usem o Docker no seu ambiente de desenvolvimento.

- **🛠 Modo Desenvolvimento Docker**
    - :computer: [Linux Ubuntu LTS](https://ubuntu.com/download/desktop)
    - 🐳 [Docker](https://docs.docker.com/engine/installation/) Deve estar instalado.
    - 🐳 [Docker Compose](https://docs.docker.com/compose/) Deve estar instalado.
    - **💡 Dica:** [Documentação do Docker](https://docs.docker.com/)

# Instalando

## 🐳 Modo Desenvolvimento com Docker

Após instalar o docker e docker-compose, estando na pasta raiz do projeto, execute:

```sh
docker-compose up
```

Para se certificar que os seus containers subiram corretamente, todos os containers deve estar com o status `UP`, execute:

```sh
docker-compose ps -a
```

Para acessar o container da aplicação, execute:

```sh
docker-compose run --rm web bash
```

Para acessar a instância do banco de dados, execute:

```sh
docker exec-it [nome do db] bash
```

Para derrubar e subir a instância do docker novamente, execute:

```sh
docker-compose down && docker-compose up
```

🚀 :clap: Para visualizar o sistema basta acessar no navegador no endereço: [localhost:8000](localhost:8000)

# Referências utilizadas

[1° Como criar uma aplicação Django com Docker](https://github.com/claudimf/django-docker)

[2° Criar um projeto em Django](https://github.com/claudimf/try_django)