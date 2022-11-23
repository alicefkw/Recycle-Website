     Para funcionar o projeto na máquina local, é necessário ter o Python instalado (a versão utilizada para este desenvolvimento foi o Python 3.10.8) e então instalar algumas dependências antes de ligar o site.
     Essas dependências serão instaladas com o pip, um controlador de pacotes do Python. É recomendado ter na instalado na máquina apenas uma versão do Python para evitar possíveis problemas, então será possível se referir ao pip como ‘pip’ ou ‘pip3’ (não tem problema usar ‘pip’ com a versão Python3+). 
    Os comandos do Python no CMD podem ser dados ao se referir a ele como ‘python’, ‘python3’ ou ‘py’, dependendo de como ele foi instalado.
     Para organização das dependências, é recomendado criar um ambiente virtual (disponível através do pacote virtualenv — instalável através do CMD com o comando pip install virtualenv). O comando pip freeze verifica as dependências instaladas. Com o virtualenv instalado e diretório no CMD estando dentro da pasta desejada para instalar as bibliotecas, o comando python -m venv django criará um ambiente virtual com o nome ‘django’.
     Para ativar este ambiente virtual, toda vez será necessário navegar até a pasta onde ele foi criado e digitar, no Windows, o comando django\scripts\activate.
     Com o ambiente virtual ativo, digite o comando pip install django, espere a finalização das instalações e então digite python manage.py runserver. É possível desativar o ambiente virtual com o comando deactivate.
     Abra um navegador, (se estiver fazendo alterações no código, abra o navegador de preferência no modo anônimo para os dados de navegação não ficarem salvos e não atrapalharem na atualização do desenvolvimento) e então entre no URL localhost:8000.
 
Voilà!   
