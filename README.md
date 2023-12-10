# MVP Sprint Qualidade de Software, Segurança e Sistemas Inteligentes

## Descrição do projeto:
        Este projeto faz parte das exigências da sprint Qualidade de Software,
    Segurança e Sistemas Inteligentes da pós graduação da PUC-Rio,
    curso de Engenharia de Software, turma de julho de 2023.
        Neste projeto se encontram o back_end, front_end e arquivo do colab
    com o modelo implementando técnicas de aprendizado de máquina para a
    predição do risco de surgimento de doenças coronárias no prazo de 10
    anos a partir de alguns dados fornecidos ao modelo.

## Funcionalidades do projeto:
        As funcionalidades consistem na maioria das operações básicas no
    banco de dados (Create, Read, Delete), sendo que a interação com a
    aplicação pode tanto ocorrer pelo front_end, cliente de API como
    Insomnia ou Postman quanto pelo browser, através de ferramentas
    como Swagger, etc.

## Link do vídeo de apresentação:

    #######link Youtube - vídeo público não listado.##########

## Link do Colab:
        Além de o colab notebook com o modelo treinado estar presente neste
    repositório, ele pode ser acessado diretamente pelo navegador
    através do link:

    https://colab.research.google.com/drive/1D8KKh0ycPaRWDTnp3cCvy4dEIvm8idgg#scrollTo=JAIp6d9w5QG8&uniqifier=1

## Árvore de módulos. O sistema de pastas e arquivos do projeto está estruturado:
    Projeto
    |__ application
        |__ back_end
            |__ database
                |__ db.sqlite3
            |__ log
                |__ gunicorn.detailed.log
            |__ model
                |__ __init__.py
                |__ base.py
                |__ evaluator.py
                |__ loader.py
                |__ prediction.py
                |__ preprocessor.py
                |__ trained_model.py
            |__ schemas
                |__ __init__.py
                |__ error.py
                |__ prediction.py
            |__ trained_model
                |__ trained_model.pkl
            |__ app.py
            |__ logger.py
            |__ test_models.py
        |__ front_end
            |__ img
                |__ hospital-1-1500x600.jpg
                |__ hospital-2-1024x577.jpg
            |__ static
                |__ favicon.ico.png
            index.html
            scripts.js
            styles.css
        |__ requirements.txt
    |__ dataset
        |__ heart_disease.csv
    |__ notebook
        |__ MVP_Machine_Learning_Attila_Barcellos_Sipos.ipynb
    |__ README.md

## Como executar
        Será necessário ter todas as libs(módulos) python listadas no
    requirements.txt instaladas.
    Após clonar o repositório, é necessário ir ao diretório raiz
    (pasta back_end), pelo terminal, para poder executar os comandos
    descritos abaixo.
    É fortemente indicado o uso de ambientes virtuais do tipo virtualenv.

    Passos para a execução da API via ambiente virtual:

        #1 navegar para a pasta application, de preferência
        #2 criar o diretório do ambiente: mkdir <diretorio_ambiente_virtual>
        #3 navegar para a pasta do ambiente virtual criada
        #4 criar o ambiente virtual: virtualenv <nome_do_ambiente>
        #5 digitar source <nome_do_ambiente>/bin/activate
        #6 pip install -r requirements.txt
        #7 se dirigir para a pasta back_end
        #8 flask run –host 0.0.0.0 --port 5000 --reload
        #9 digite no navegador http://localhost:5000/#/ para verificar
            o status da API em execução.
        #10 com o back_end em execução, arraste o arquivo index.html
            para o navegador para interagir com o front_end.

## Sobre o banco de dados
        A aplicação possui um banco de dados populado, mas se quiser, é
    só deletar o banco de dados de antes de iniciar a aplicação Flask 
    que um novo banco de dados será criado automaticamente.
