import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# === CONFIGURAÇÃO DA PÁGINA ===
st.set_page_config(
    page_title="Dashboard de Atendimentos fim de ANO",
    page_icon="📊",
    layout="wide"
)

# === DADOS (Embutidos para facilitar a execução) ===
# Estes dados refletem a análise validada anteriormente
data_daily = [
    {"Unidade": "CENTRO", "Periodo": "2023/2024", "Dia_Mes": "30/12", "Qtd": 6},
    {"Unidade": "CENTRO", "Periodo": "2024/2025", "Dia_Mes": "30/12", "Qtd": 13},
    {"Unidade": "CENTRO", "Periodo": "2024/2025", "Dia_Mes": "31/12", "Qtd": 5},
    {"Unidade": "CENTRO", "Periodo": "2023/2024", "Dia_Mes": "02/01", "Qtd": 26},
    {"Unidade": "CENTRO", "Periodo": "2024/2025", "Dia_Mes": "02/01", "Qtd": 15},
    {"Unidade": "CENTRO", "Periodo": "2023/2024", "Dia_Mes": "03/01", "Qtd": 31},
    {"Unidade": "CENTRO", "Periodo": "2024/2025", "Dia_Mes": "03/01", "Qtd": 14},
    {"Unidade": "CENTRO", "Periodo": "2023/2024", "Dia_Mes": "04/01", "Qtd": 35},
    {"Unidade": "CENTRO", "Periodo": "2024/2025", "Dia_Mes": "04/01", "Qtd": 8},
    {"Unidade": "CENTRO", "Periodo": "2023/2024", "Dia_Mes": "05/01", "Qtd": 37},
    
    {"Unidade": "O.B.", "Periodo": "2024/2025", "Dia_Mes": "30/12", "Qtd": 11},
    {"Unidade": "O.B.", "Periodo": "2024/2025", "Dia_Mes": "31/12", "Qtd": 6},
    {"Unidade": "O.B.", "Periodo": "2024/2025", "Dia_Mes": "02/01", "Qtd": 6},
    {"Unidade": "O.B.", "Periodo": "2024/2025", "Dia_Mes": "03/01", "Qtd": 20},
    {"Unidade": "O.B.", "Periodo": "2024/2025", "Dia_Mes": "04/01", "Qtd": 4},
    
    {"Unidade": "TILLI", "Periodo": "2024/2025", "Dia_Mes": "30/12", "Qtd": 47},
    {"Unidade": "TILLI", "Periodo": "2024/2025", "Dia_Mes": "31/12", "Qtd": 24},
    {"Unidade": "TILLI", "Periodo": "2024/2025", "Dia_Mes": "02/01", "Qtd": 34},
    {"Unidade": "TILLI", "Periodo": "2024/2025", "Dia_Mes": "03/01", "Qtd": 54},
    {"Unidade": "TILLI", "Periodo": "2024/2025", "Dia_Mes": "04/01", "Qtd": 31},
    {"Unidade": "TILLI", "Periodo": "2024/2025", "Dia_Mes": "05/01", "Qtd": 22}
]

data_hourly = [
    {"Unidade": "TILLI", "Hora": 6, "Qtd": 29}, {"Unidade": "TILLI", "Hora": 7, "Qtd": 52},
    {"Unidade": "TILLI", "Hora": 8, "Qtd": 46}, {"Unidade": "TILLI", "Hora": 9, "Qtd": 42},
    {"Unidade": "TILLI", "Hora": 10, "Qtd": 27}, {"Unidade": "TILLI", "Hora": 11, "Qtd": 7},
    {"Unidade": "TILLI", "Hora": 12, "Qtd": 6}, {"Unidade": "TILLI", "Hora": 13, "Qtd": 3},
    
    {"Unidade": "CENTRO", "Hora": 6, "Qtd": 8}, {"Unidade": "CENTRO", "Hora": 7, "Qtd": 12},
    {"Unidade": "CENTRO", "Hora": 8, "Qtd": 7}, {"Unidade": "CENTRO", "Hora": 9, "Qtd": 16},
    {"Unidade": "CENTRO", "Hora": 10, "Qtd": 4}, {"Unidade": "CENTRO", "Hora": 11, "Qtd": 3},
    {"Unidade": "CENTRO", "Hora": 12, "Qtd": 3}, {"Unidade": "CENTRO", "Hora": 13, "Qtd": 2},
    
    {"Unidade": "O.B.", "Hora": 6, "Qtd": 4}, {"Unidade": "O.B.", "Hora": 7, "Qtd": 12},
    {"Unidade": "O.B.", "Hora": 8, "Qtd": 9}, {"Unidade": "O.B.", "Hora": 9, "Qtd": 12},
    {"Unidade": "O.B.", "Hora": 10, "Qtd": 7}, {"Unidade": "O.B.", "Hora": 11, "Qtd": 1},
    {"Unidade": "O.B.", "Hora": 12, "Qtd": 2}
]

df_daily = pd.DataFrame(data_daily)
df_hourly = pd.DataFrame(data_hourly)

# === BARRA LATERAL (Sidebar) ===
st.sidebar.title("Filtros")
unidades = sorted(df_daily['Unidade'].unique())
selected_unit = st.sidebar.selectbox("Selecione a Unidade:", ["TODAS"] + unidades)

# === TÍTULO E ANÁLISE ===
st.title("📊 Painel Estratégico de Atendimentos")
st.markdown("---")

# Box de Análise
with st.container():
    st.subheader("💡 Análise de Viabilidade (Dez/Jan)")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("**TILLI: ALTA DEMANDA**\n\nVolume robusto (>35/dia). Pico matinal forte. \n\n✅ **Abrir** (Sugestão: 06h - 10h30)")
    with col2:
        st.warning("**CENTRO: VOLUME MÉDIO**\n\nVolume de ~11/dia, mas com extensão maior até 11h.\n\n⚠️ **Avaliar** (Backup)")
    with col3:
        st.error("**O.B.: BAIXA DEMANDA**\n\nVolume <10/dia e horário curto.\n\n❌ **Não Recomendado**")

st.markdown("---")

# === GRÁFICOS ===

# Lógica de Filtro
if selected_unit != "TODAS":
    df_d_show = df_daily[df_daily['Unidade'] == selected_unit]
    df_h_show = df_hourly[df_hourly['Unidade'] == selected_unit]
    title_suffix = f" - {selected_unit}"
else:
    df_d_show = df_daily
    df_h_show = df_hourly
    title_suffix = " - Geral"

# Tabs para organizar
tab1, tab2 = st.tabs(["📅 Comparativo Diário", "⏰ Perfil Horário"])

with tab1:
    st.subheader(f"Comparativo de Volume Diário (Ano Anterior vs Atual){title_suffix}")
    
    # Criar gráfico de barras agrupadas
    fig_daily = px.bar(
        df_d_show, 
        x="Dia_Mes", 
        y="Qtd", 
        color="Periodo", 
        barmode="group",
        text="Qtd",
        color_discrete_map={"2023/2024": "#95a5a6", "2024/2025": "#004B8D"},
        labels={"Qtd": "Atendimentos", "Dia_Mes": "Dia", "Periodo": "Ano Ref."},
        height=400
    )
    fig_daily.update_traces(textposition='outside')
    fig_daily.update_layout(xaxis={'categoryorder':'array', 'categoryarray': ['30/12','31/12','02/01','03/01','04/01','05/01']})
    st.plotly_chart(fig_daily, use_container_width=True)

with tab2:
    st.subheader(f"Extensão Horária (Acumulado 2024/25){title_suffix}")
    st.markdown("*Este gráfico mostra o volume total acumulado por hora para ajudar a identificar o horário de queda de movimento.*")
    
    # Criar gráfico de linhas
    fig_hourly = px.line(
        df_h_show, 
        x="Hora", 
        y="Qtd", 
        color="Unidade",
        markers=True,
        symbol="Unidade",
        color_discrete_map={"TILLI": "#004B8D", "CENTRO": "#E67E22", "O.B.": "#27AE60"},
        labels={"Qtd": "Volume Acumulado", "Hora": "Hora do Dia"},
        height=400
    )
    fig_hourly.update_layout(xaxis=dict(tickmode='linear', tick0=6, dtick=1))
    fig_hourly.update_traces(line=dict(width=3), marker=dict(size=8))
    st.plotly_chart(fig_hourly, use_container_width=True)

# === DATA TABLE (Opcional) ===
with st.expander("Ver Dados Brutos"):

    st.dataframe(df_d_show.pivot_table(index=["Unidade", "Dia_Mes"], columns="Periodo", values="Qtd", fill_value=0))
