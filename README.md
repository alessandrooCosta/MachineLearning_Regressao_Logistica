# Previsão de Churn

Projeto simples para prever churn (cancelamento de clientes) usando um modelo de machine learning treinado e um scaler salvo. O repositório inclui um script de execução interativo (`main.py`) que carrega o modelo e o scaler, solicita duas entradas do usuário (meses de assinatura e horas assistidas) e retorna a previsão e a probabilidade de churn.

## O que é este projeto
Um exemplo educativo que demonstra como servir um modelo de classificação treinado em Python (scikit-learn) para prever se um cliente tem tendência a cancelar o serviço (churn) com base em duas variáveis: tempo de assinatura (meses) e horas assistidas.

### Stack
- **Linguagem(s):** Python
- **Runtime:** Python 3.x
- **Bibliotecas notáveis:** pandas, scikit-learn, joblib

## Organização do repositório
```
.gitignore        # Arquivos ignorados
.idea/             # Configurações do IDE (PyCharm/IntelliJ)
main.py            # Script principal (entrada CLI simples)
modelo_churn.joblib # Modelo treinado (joblib)
scaler_churn.joblib # Scaler usado para normalizar os dados (joblib)
```

Como funciona: `main.py` carrega `scaler_churn.joblib` para escalar as entradas fornecidas e então usa `modelo_churn.joblib` para prever 0 (cliente permanece) ou 1 (cliente cancela). A saída inclui também a probabilidade estimada de churn.

## Como executar
1. Clone o repositório

```bash
git clone https://github.com/alessandrooCosta/MachineLearning_Regress-o_Logistica.git
cd MachineLearning_Regress-o_Logistica
```

2. Crie um ambiente virtual e instale dependências

```bash
python -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate    # Windows (PowerShell)

pip install --upgrade pip
pip install pandas scikit-learn joblib
```

> Observação: não há um `requirements.txt` neste repositório — recomenda-se adicionar um para reprodutibilidade.

3. Execute o script

```bash
python main.py
```

O script pedirá:
- Quantos meses de assinatura o cliente possui?
- Quantas horas assistidas o cliente possui?

E então mostrará a previsão (CANCELAR ou CONTINUAR ATIVO) e a probabilidade de churn.

## Formato de entrada e saída
- Entrada: duas features numéricas (Meses_Assinatura, Horas_Assistidas)
- Saída: previsão binária (0 = continuar ativo, 1 = cancelar) e probabilidade associada ao rótulo de churn.

Exemplo de execução:

```
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

## Observações sobre os artefatos do modelo
- modelo_churn.joblib: provavelmente um classificador do scikit-learn salvo com joblib.
- scaler_churn.joblib: objeto scaler (por exemplo, StandardScaler) salvo com joblib para normalizar as entradas antes da predição.

Esses arquivos são binários e não estão versionados de forma transparente — para garantir reprodutibilidade, adicione:
- `requirements.txt` com versões exatas
- um notebook ou script `train.py` que mostra como o modelo foi treinado e avaliado
- uma descrição do conjunto de dados usado (colunas, amostragem, data)

## Melhorias recomendadas
- Adicionar `requirements.txt` ou `pyproject.toml`.
- Incluir um notebook (`notebooks/`) com EDA e processo de treinamento.
- Substituir entradas via `input()` por uma API (FastAPI/Flask) ou CLI com argumentos (argparse/click).
- Salvar metadados do modelo (features usadas, versão, métricas) e criar testes automatizados.
- Validar entradas do usuário (valores negativos/entrada inválida).

## Segurança e licença
- Este repositório não contém dados sensíveis visíveis, mas os modelos e dados devem ser tratados com cuidado para evitar vazamento de dados.
- Licença: adicione uma licença (por exemplo MIT) se quiser permitir uso público.

## Contato
Autor: alessandrooCosta

---

Se quiser, eu posso:
- adicionar automaticamente um `requirements.txt` com versões compatíveis;
- criar um notebook de exemplo com EDA e treinamento fictício (se você fornecer o dataset);
- transformar `main.py` numa API simples com FastAPI para testes locais.
