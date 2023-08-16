# boot-dev-environ

### Programa para iniciar automaticante um ambiente em desenvolvimento com Backend e Frontend

- É necessário copiar o .env.example e apagar a extensão .example da cópia para que seja criado um arquivo .env
Modifique o .env criado de acordo com as suas configurações

DEBUG=true

APP={NOME DA APLICAÇÃO}

PATH-BACKEND={CAMINHO DO BACKEND} - Necessário separar os diretórios com \\(dupla contra barra)

PATH-FRONTEND={CAMINHO DO FRONTEND} - Necessário separar os diretórios com \\(dupla contra barra)

START-SERVER-BACKEND={COMANDO PARA INICIAR O SERVIDOR BACKEND PELO TERMINAL}

START-SERVER-FRONTEND={COMANDO PARA INICIAR O SERVIDOR BACKEND PELO TERMINAL}

TERMINAL={TERMINAL UTILIZADO} ex. Git Bash

PROGRAM-TEST-API={PROGRAMA PARA TESTAR ROTAS DA API} - Ainda não ativo no código

- Após isso, certifique-se que já possui as bibliotecas pyautogui e python-dotenv instaladas para executar o projeto
- Para executar o projeto abra um terminal no mesmo diretório e digite python BootDevEnviron.py ou então utilize o atalho CTRL + F5 

**Obs:**

- **O script precisa do VsCode instalado, pois são utilizados atalhos desse programa para abertura de terminal, por exemplo**

- **Não é utilizado nenhum tipo de interação com o mouse a partir do pyautogui de forma que seja compatível para a maioria dos ambientes**

