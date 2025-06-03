import pandas as pd
import matplotlib.pyplot as plt

# Carregar a planilha (certifique-se de que o arquivo esteja no mesmo diretório ou informe o caminho completo)
# A aba utilizada é "RESULTADOS ENCONTRADOS"
df = pd.read_excel('RESULTADOS FBE - PROFISSIONAIS DE SAÚDE (1) (2).xlsx', sheet_name='RESULTADOS ENCONTRADOS')

# Verificar os nomes das colunas
print(df.columns)

# -------------------------------------------------------------------
# 1. Percentual do TIPO DE PARTICIPANTE
def plot_tipo_participante(data):
    # Cálculo dos percentuais de cada tipo de participante
    percent_tipo = data['TIPO DE PARTICIPANTE'].value_counts(normalize=True) * 100
    print("Percentual por TIPO DE PARTICIPANTE:")
    print(percent_tipo)
    
    # Gráfico de barras
    plt.figure(figsize=(8,6))
    ax = percent_tipo.sort_index().plot(kind='bar', color='skyblue')
    plt.title('Percentual por Tipo de Participante')
    plt.xlabel('Tipo de Participante')
    plt.ylabel('Porcentagem (%)')
    
    # Adicionar rótulos de porcentagem em cada barra
    for i, value in enumerate(percent_tipo.sort_index()):
        plt.text(i, value + 1, f'{value:.1f}%', ha='center', fontsize=10)
    
    plt.tight_layout()
    plt.show()

# -------------------------------------------------------------------
# 2. Percentual da Queixa Principal
def plot_queixa_principal(data):
    percent_queixa = data['Queixa Principal'].value_counts(normalize=True) * 100
    print("Percentual por Queixa Principal:")
    print(percent_queixa)
    
    plt.figure(figsize=(10,6))
    ax = percent_queixa.sort_values().plot(kind='bar', color='lightgreen')
    plt.title('Percentual da Queixa Principal')
    plt.xlabel('Queixa Principal')
    plt.ylabel('Porcentagem (%)')
    plt.xticks(rotation=45, ha='right')
    
    for i, value in enumerate(percent_queixa.sort_values()):
        plt.text(i, value + 1, f'{value:.1f}%', ha='center', fontsize=10)
    
    plt.tight_layout()
    plt.show()

# -------------------------------------------------------------------
# 3. Percentual em relação à avaliação dos parâmetros clínicos
def plot_parametros_avaliados(data):
    percent_param = data['Os parâmetros clínicos foram avaliados?'].value_counts(normalize=True) * 100
    print("Percentual dos parâmetros clínicos avaliados:")
    print(percent_param)
    
    plt.figure(figsize=(8,6))
    ax = percent_param.sort_index().plot(kind='bar', color='salmon')
    plt.title('Avaliação dos Parâmetros Clínicos')
    plt.xlabel('Resposta')
    plt.ylabel('Porcentagem (%)')
    
    for i, value in enumerate(percent_param.sort_index()):
        plt.text(i, value + 1, f'{value:.1f}%', ha='center', fontsize=10)
    
    plt.tight_layout()
    plt.show()

# -------------------------------------------------------------------
# 4. Percentual das intervenções não-farmacológicas presentes nas diretrizes
def plot_intervencoes_nao_farmacologicas(data):
    percent_nao_farma = data['Intervenções não-farmacológicas'].value_counts(normalize=True) * 100
    print("Percentual para intervenções não-farmacológicas:")
    print(percent_nao_farma)
    
    plt.figure(figsize=(8,6))
    ax = percent_nao_farma.sort_index().plot(kind='bar', color='plum')
    plt.title('Intervenções Não-Farmacológicas nas Diretrizes')
    plt.xlabel('Resposta')
    plt.ylabel('Porcentagem (%)')
    
    for i, value in enumerate(percent_nao_farma.sort_index()):
        plt.text(i, value + 1, f'{value:.1f}%', ha='center', fontsize=10)
    
    plt.tight_layout()
    plt.show()

# -------------------------------------------------------------------
# 5. Percentual das intervenções farmacológicas presentes nas diretrizes
def plot_intervencoes_farmacologicas(data):
    # Converter os valores para minúsculas para unificar as respostas
    respostas = data['As intervenções farmacológicas estão presentes nas diretrizes?'].str.lower()
    # Repadronizar: transformar 'sim' em 'Sim' e 'não' em 'Não'
    respostas = respostas.replace({'sim': 'Sim', 'não': 'Não'})
    
    # Calcular os percentuais
    percent_farma = respostas.value_counts(normalize=True) * 100
    print("Percentual para intervenções farmacológicas:")
    print(percent_farma)
    
    plt.figure(figsize=(8,6))
    ax = percent_farma.sort_index().plot(kind='bar', color='gold')
    plt.title('Intervenções Farmacológicas nas Diretrizes')
    plt.xlabel('Resposta')
    plt.ylabel('Porcentagem (%)')
    
    for i, value in enumerate(percent_farma.sort_index()):
        plt.text(i, value + 1, f'{value:.1f}%', ha='center', fontsize=10)
    
    plt.tight_layout()
    plt.show()

# -------------------------------------------------------------------
# 6. Relação entre Queixa Principal e Conformidade das Intervenções Farmacológicas
def plot_conformidade_queixa(data):
    # Função para classificar a conformidade:
    def classificar_conformidade(resp):
        # Considere ajustar os valores conforme os textos presentes na sua planilha
        if str(resp).strip().lower() == "conforme":
            return "Conforme"
        else:
            return "Não/Parcialmente Conforme"
    
    # Cria uma nova coluna com a classificação
    data['Conformidade Interv. Farmacológicas'] = data['As intervenções farmacológicas estão presentes nas diretrizes?'].apply(classificar_conformidade)
    
    # Tabela cruzada entre Queixa Principal e Conformidade
    tabela_conformidade = pd.crosstab(data['Queixa Principal'], data['Conformidade Interv. Farmacológicas'])
    # Converter os valores em porcentagem por linha (para cada queixa)
    tabela_conformidade_pct = tabela_conformidade.div(tabela_conformidade.sum(axis=1), axis=0) * 100
    
    print("Tabela de porcentagens (por Queixa Principal) em relação à conformidade das intervenções farmacológicas:")
    print(tabela_conformidade_pct)
    
    # Gráfico de barras agrupadas
    plt.figure(figsize=(12,7))
    ax = tabela_conformidade_pct.plot(kind='bar', color=['seagreen', 'tomato'], edgecolor='black')
    plt.title('Queixa Principal x Conformidade das Intervenções Farmacológicas')
    plt.xlabel('Queixa Principal')
    plt.ylabel('Porcentagem (%)')
    plt.legend(title='Conformidade', loc='upper right')
    plt.xticks(rotation=45, ha='right')
    
    # Adicionar os rótulos de porcentagem em cada barra
    for patch in ax.patches:
        ax.annotate(f'{patch.get_height():.1f}%', 
                    (patch.get_x() + patch.get_width() / 2, patch.get_height()),
                    ha='center', va='baseline', fontsize=9, color='black')
    
    plt.tight_layout()
    plt.show()
    
    # Salvar a tabela de conformidade em um arquivo Excel
    tabela_conformidade_pct.to_excel('tabela_conformidade_saida_novo.xlsx')
    print("Arquivo 'tabela_conformidade_saida_novo.xlsx' salvo com sucesso!")

# -------------------------------------------------------------------
# Execução das funções de plotagem
if __name__ == "__main__":
    plot_tipo_participante(df)
    plot_queixa_principal(df)
    plot_parametros_avaliados(df)
    plot_intervencoes_nao_farmacologicas(df)
    plot_intervencoes_farmacologicas(df)
    plot_conformidade_queixa(df)
