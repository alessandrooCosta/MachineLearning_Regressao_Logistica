import joblib
import pandas as pd
import warnings
warnings.filterwarnings('ignore', category=UserWarning)

print("Calculo de Churn!")
print("------------------------")
print("Responda as perguntas a seguir")
meses = float(input("Quantos meses de assitura este cliente possui ? \n"))
horas = float(input("Quantas horas de assistidas em cliente possui ?"))

modelo_carregado = joblib.load('modelo_churn.joblib')
scaler_carregado = joblib.load('scaler_churn.joblib')

dados_usuario = pd.DataFrame([[meses, horas]], columns=['Meses_Assinatura', 'Horas_Assistidas'])

dados_escalados = scaler_carregado.transform(dados_usuario)

previsao = modelo_carregado.predict(dados_escalados)
probabilidade = modelo_carregado.predict_proba(dados_escalados)[0][1]

status = "CANCELAR ❌" if previsao[0] == 1 else "CONTINUAR ATIVO ✅"
print("\n------------------------")
print(f"Previsão: O cliente tende a {status}")
print(f"Risco de Churn: {probabilidade * 100:.2f}%")