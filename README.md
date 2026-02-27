# Automação de Cadastro de Produtos

## Sobre o Projeto
Este projeto consiste em um script de automação desenvolvido em Python para realizar o cadastro automático de produtos em um sistema web. A ferramenta foi criada para otimizar o processo de cadastramento em massa, eliminando a necessidade de inserção manual de dados e reduzindo significativamente o tempo de trabalho.

## Funcionalidades
- Acesso automatizado ao navegador
- Login automático no sistema
- Leitura de dados a partir de arquivo CSV
- Preenchimento automático de formulários
- Cadastro sequencial de múltiplos produtos
- Tratamento de campos opcionais (observações)

## Tecnologias Utilizadas
- Python 3.13.7
- PyAutoGUI (automação de interface gráfica)
- Pandas (manipulação de dados)
- Time (controle de temporização)

## Estrutura do Projeto

### Bibliotecas Necessárias
```
import pyautogui
import time
import pandas
```

### Fluxo de Automação

#### Passo 1: Acesso ao Sistema
- Abre o navegador Chrome
- Navega até o site de cadastro
- Aguarda o carregamento completo da página

#### Passo 2: Login
- Preenche as credenciais de acesso
- Email: projetodev@gmail.com
- Senha: 12345
- Confirma o login

#### Passo 3: Importação da Base de Dados
- Lê o arquivo produtos.csv
- Carrega as informações dos produtos a serem cadastrados

#### Passo 4: Cadastro dos Produtos
Para cada produto na base de dados, o script:
1. Preenche o código do produto
2. Preenche a marca
3. Preenche o tipo
4. Preenche a categoria
5. Preenche o preço unitário
6. Preenche o custo
7. Preenche observações (quando disponível)
8. Envia o formulário
9. Retorna ao topo da página para o próximo cadastro

## Configuração do Ambiente

### Instalação das Dependências
```
pip install pyautogui pandas
```

### Arquivo de Dados
O script espera um arquivo `produtos.csv` com a seguinte estrutura:
- codigo
- marca
- tipo
- categoria
- preco_unitario
- custo
- obs

## Personalização

### Ajuste de Coordenadas
As coordenadas de clique (x, y) no script precisam ser ajustadas conforme a resolução da tela e posicionamento dos elementos no site:

```python
pyautogui.click(x=728, y=407)  # Ajuste conforme necessário
```

### Tempo de Execução
O tempo de pausa entre comandos pode ser ajustado:
```python
pyautogui.PAUSE = 0.5  # Tempo em segundos
time.sleep(4)  # Pausa específica para carregamento
```

## Tratamento de Dados
- Conversão automática de números para string
- Tratamento especial para valores nulos (NaN) no campo de observações
- Prevenção de erros durante a digitação

## Como Utilizar

1. Prepare o arquivo produtos.csv com os dados necessários
2. Ajuste as coordenadas dos cliques conforme sua tela
3. Execute o script:
```
python automacao_cadastro.py
```
4. Acompanhe a automação realizando o cadastro automático

## Observações Importantes
- O script depende da resolução da tela e posicionamento dos elementos
- É necessário manter o navegador em foco durante a execução
- Recomenda-se testar com poucos produtos antes de executar em massa
- O tempo de pausa pode precisar de ajustes conforme a velocidade da internet

## Possíveis Melhorias
- Implementar detecção automática de elementos na tela
- Adicionar logs de produtos cadastrados
- Incluir tratamento de erros mais robusto
- Permitir configuração via arquivo externo
- Adicionar interface gráfica para configuração

## Contribuição
Sinta-se à vontade para sugerir melhorias ou relatar problemas através de issues no repositório do projeto.

---
Este projeto foi desenvolvido para demonstrar como a automação de tarefas repetitivas pode aumentar a produtividade e reduzir erros manuais em processos de cadastramento em massa.
