# MachineLearning - Regressão Logística

Projeto de Machine Learning para prever o risco de churn (cancelamento) de clientes usando um modelo de regressão logística treinado e salvo em arquivos `.joblib`.

O sistema recebe duas variáveis do usuário:
- `Meses_Assinatura`
- `Horas_Assistidas`

E retorna:
- a previsão binária (`0` ou `1`)
- o risco percentual de churn

## Objetivo

Este repositório demonstra de forma simples como:
- treinar ou carregar um modelo de classificação;
- aplicar pré-processamento com `StandardScaler`;
- salvar e reutilizar artefatos de ML usando `joblib`;
- construir uma interface de console para prever churn em tempo real.

## Como o projeto funciona

O script principal `main.py`:
1. coleta os dados de entrada via console;
2. carrega o scaler salvo em `scaler_churn.joblib`;
3. transforma os dados de entrada;
4. carrega o modelo treinado em `modelo_churn.joblib`;
5. realiza a predição;
6. exibe a decisão final e a probabilidade de churn.

## Estrutura do repositório

```text
.
├── .gitignore
├── README.md
├── main.py
├── modelo_churn.joblib
├── scaler_churn.joblib
└── .idea/                  # arquivos locais de IDE (opcional)
```

## Requisitos

- Python 3.9+
- pip
- pandas
- scikit-learn
- joblib

## Instalação

Clone o repositório:

```bash
git clone https://github.com/alessandrooCosta/MachineLearning_Regress-o_Logistica.git
cd MachineLearning_Regress-o_Logistica
```

Crie um ambiente virtual e instale as dependências:

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
# ou no Windows:
# venv\Scripts\activate

python -m pip install --upgrade pip
pip install pandas scikit-learn joblib
```

## Execução

No diretório do projeto, execute:

```bash
python main.py
```

O programa pedirá duas informações:

```text
Quantos meses de assitura este cliente possui ?
Quantas horas de assistidas em cliente possui ?
```

## Exemplo de saída

```text
Calculo de Churn!
------------------------
Responda as perguntas a seguir
Quantos meses de assitura este cliente possui ?
> 6
Quantas horas de assistidas em cliente possui ?
> 12

------------------------
Previsão: O cliente tende a CONTINUAR ATIVO ✅
Risco de Churn: 12.34%
```

## Interpretação do resultado

A previsão produz um resultado binário:

- `0` → cliente continua ativo
- `1` → cliente tende a cancelar

A probabilidade de churn é calculada pelo modelo e exibida em porcentagem.

## Artefatos do modelo

### `modelo_churn.joblib`
Arquivo que contém o modelo treinado de regressão logística já pronto para predição.

### `scaler_churn.joblib`
Arquivo que armazena o objeto de padronização utilizado para transformar os dados antes da previsão.

## Observações

Este projeto é um exemplo didático e pode ser expandido com:
- `requirements.txt` para reprodutibilidade;
- dataset real com documentação das colunas;
- treinamento em um script separado (`train.py`);
- validação de entradas e tratamentos de erro;
- interface web ou API (`FastAPI`/`Flask`);
- testes automatizados.

## Melhorias recomendadas

- adicionar `requirements.txt` com versões fixas das bibliotecas;
- incluir notebook de análise exploratória;
- separar treinamento e inferência em arquivos distintos;
- salvar métricas e metadata do modelo;
- transformar a aplicação em API REST ou CLI mais robusto.

## Licença

Este repositório não informa uma licença explícita. Se você pretende compartilhar publicamente o projeto, recomenda-se adicionar uma licença como MIT ou Apache 2.0.

## Autor

- alessandrooCosta

---

Se quiser, posso também criar:
- um `requirements.txt`;
- um script de treinamento (`train.py`);
- uma versão com API em `FastAPI`;
- um README ainda mais profissional em inglês ou em português, com badges e screenshots.
