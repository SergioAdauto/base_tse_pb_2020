import pandas as pd
import numpy as np

from dash import Dash, dcc, html, Input, Output, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px


dc = pd.read_csv(filepath_or_buffer='https://github.com/SergioAdauto/base_tse_pb_2020/raw/main/despesas_contratadas_candidatos_2020_PB.zip', sep=';', decimal = '.', compression='zip', encoding='latin-1')
dp = pd.read_csv(filepath_or_buffer='https://github.com/SergioAdauto/base_tse_pb_2020/raw/main/despesas_pagas_candidatos_2020_PB.zip', sep=';', decimal = '.', compression='zip', encoding='latin-1')

rc = pd.read_csv(filepath_or_buffer='https://github.com/SergioAdauto/base_tse_pb_2020/raw/main/receitas_candidatos_2020_PB.zip', sep=';', decimal = '.', compression='zip', encoding='latin-1')

despesas_contratadas = dc.query('NM_UE == "CAMPINA GRANDE"')
despesas_pagas = dp
receita_candidatos = rc.query('NM_UE == "CAMPINA GRANDE"')


df_despesas = despesas_contratadas[['DS_CARGO',
                                    'NM_CANDIDATO', 
                                    'NR_CPF_CANDIDATO', 
                                    'NR_PARTIDO', 
                                    'SG_PARTIDO', 
                                    'NM_PARTIDO', 
                                    'SQ_DESPESA', 
                                    'VR_DESPESA_CONTRATADA']].merge(
    right=despesas_pagas[['DS_ORIGEM_DESPESA', 'SQ_DESPESA', 'VR_PAGTO_DESPESA']], on='SQ_DESPESA')



df_receitas = receita_candidatos[['DS_CARGO',
                    'NM_CANDIDATO',
                    'NR_CPF_CANDIDATO',
                    'NR_PARTIDO',
                    'SG_PARTIDO',
                    'NM_PARTIDO',
                    'DS_ORIGEM_RECEITA',
                    'VR_RECEITA',
                    'DS_RECEITA']]



df_despesas['VR_DESPESA_CONTRATADA'] = df_despesas['VR_DESPESA_CONTRATADA'].str.replace(',', '.')
df_receitas['VR_RECEITA'] = df_receitas['VR_RECEITA'].str.replace(',', '.')
df_despesas['VR_PAGTO_DESPESA'] = (df_despesas['VR_PAGTO_DESPESA'].str.replace(',', '.')).astype(np.float32)

df_despesas = df_despesas.astype({'NR_CPF_CANDIDATO':str, 'NR_PARTIDO':object, 'SQ_DESPESA':object, 'VR_DESPESA_CONTRATADA':np.float32})
df_receitas = df_receitas.astype({'NR_CPF_CANDIDATO':str, 'NR_PARTIDO':object, 'VR_RECEITA':np.float32})



partidos = df_receitas['SG_PARTIDO'].unique()
tot_partidos = len(df_receitas['SG_PARTIDO'].unique())
candidato = df_receitas['NM_CANDIDATO'].unique()
tot_cadidato = len(df_receitas['NM_CANDIDATO'].unique())


despesas = df_despesas[['SG_PARTIDO','SQ_DESPESA','VR_DESPESA_CONTRATADA']].groupby(['SG_PARTIDO','SQ_DESPESA']).sum().reset_index()
despesas['VR_PAGTO_DESPESA'] = df_despesas[['SG_PARTIDO', 'SQ_DESPESA', 'VR_PAGTO_DESPESA']].value_counts().to_frame().reset_index().rename(columns={0:'count'}).apply(lambda desp: desp['VR_PAGTO_DESPESA'], axis=1)

# Analisar os gastos e receitas dos partidos políticos em 2020:
# OBS: Não existe descrição das origens de receitas e dos gastos, são dados brutos.
receita_partido = df_receitas[['SG_PARTIDO','VR_RECEITA']].groupby('SG_PARTIDO').sum().reset_index()
despesa__partido = despesas[['SG_PARTIDO', 'VR_DESPESA_CONTRATADA', 'VR_PAGTO_DESPESA']].groupby('SG_PARTIDO').sum().reset_index()
despesa__partido['DIF_DESPESAS'] = despesa__partido.apply(lambda desp: desp['VR_DESPESA_CONTRATADA'] - desp['VR_PAGTO_DESPESA'], axis=1)
despesa__partido['VR_DESPESA_TOTAL'] = despesa__partido['VR_DESPESA_CONTRATADA'] + despesa__partido['VR_PAGTO_DESPESA']
# Junto dos dados brutos das despesas e receitas
receita_despesa_partido = receita_partido
receita_despesa_partido['VR_DESPESAS'] = despesa__partido['VR_DESPESA_TOTAL']
receita_despesa_partido['VR_DESPESA_CONTRATADA'] = despesa__partido['VR_DESPESA_CONTRATADA']
receita_despesa_partido['VR_PAGTO_DESPESA'] = despesa__partido['VR_PAGTO_DESPESA']

# Informações sobre despesas e receitas dos candidato a prefeito:
receita_cand_prefeito = df_receitas.query('DS_CARGO == "Prefeito"')
despesa_cand_prefeito = df_despesas.query('DS_CARGO == "Prefeito"')

tabela_prefeito_receita = receita_cand_prefeito.groupby(['NM_CANDIDATO', 'SG_PARTIDO']).sum().reset_index().rename(columns={'NM_CANDIDATO':'Candidato', 'SG_PARTIDO':'Partido','VR_RECEITA':'Receita Total'})
tabela_prefeito_receita['Receita Total'] = tabela_prefeito_receita['Receita Total'].round(2)

tabela_prefeito_despesa = despesa_cand_prefeito.groupby(['NM_CANDIDATO', 'SG_PARTIDO']).sum().reset_index().rename(columns={'NM_CANDIDATO':'Candidato', 'SG_PARTIDO':'Partido','VR_DESPESA_CONTRATADA':'Despesa Total Contratada', 'VR_PAGTO_DESPESA':'Despesa Total Paga'})
tabela_prefeito_despesa['Despesa Total'] = (tabela_prefeito_despesa['Despesa Total Contratada'] + tabela_prefeito_despesa['Despesa Total Paga']).round(2)
tabela_prefeito_despesa['Despesa Total Contratada'] = tabela_prefeito_despesa['Despesa Total Contratada'].round(2)
tabela_prefeito_despesa['Despesa Total Paga'] = tabela_prefeito_despesa['Despesa Total Paga'].round(2)




# Informações sobre as despesas e receitas dos candidatos a vereadores:
receita_cand_vereador = df_receitas.query('DS_CARGO == "Vereador"')
despesa_cand_vereador = df_despesas.query('DS_CARGO == "Vereador"')

tabela_vereador_receita = receita_cand_vereador.groupby(['NM_CANDIDATO', 'SG_PARTIDO']).sum().reset_index().rename(columns={'NM_CANDIDATO':'Candidato', 'SG_PARTIDO':'Partido','VR_RECEITA':'Receita Total'})
tabela_vereador_receita['Receita Total'] = tabela_vereador_receita['Receita Total'].round(2)

tabela_vereador_despesa = despesa_cand_vereador.groupby(['NM_CANDIDATO', 'SG_PARTIDO']).sum().reset_index().rename(columns={'NM_CANDIDATO':'Candidato', 'SG_PARTIDO':'Partido','VR_DESPESA_CONTRATADA':'Despesa Total Contratada', 'VR_PAGTO_DESPESA':'Despesa Total Paga'})
tabela_vereador_despesa['Despesa Total'] = (tabela_vereador_despesa['Despesa Total Contratada'] + tabela_vereador_despesa['Despesa Total Paga']).round(2)
tabela_vereador_despesa['Despesa Total Contratada'] = tabela_vereador_despesa['Despesa Total Contratada'].round(2)
tabela_vereador_despesa['Despesa Total Paga'] = tabela_vereador_despesa['Despesa Total Paga'].round(2)



#detalhe das despesas dos candidato a prefeito:
detalhes_receita_prefeito = df_receitas.query('DS_CARGO == "Prefeito"')[['DS_ORIGEM_RECEITA', 'VR_RECEITA']].groupby('DS_ORIGEM_RECEITA').sum().reset_index().sort_values(by='VR_RECEITA')
x = df_despesas.query('DS_CARGO == "Prefeito"')[['DS_ORIGEM_DESPESA','SQ_DESPESA','VR_DESPESA_CONTRATADA']].groupby(['DS_ORIGEM_DESPESA','SQ_DESPESA']).sum()
y = df_despesas.query('DS_CARGO == "Prefeito"')[['DS_ORIGEM_DESPESA', 'SQ_DESPESA', 'VR_PAGTO_DESPESA']].value_counts(sort=False).to_frame().reset_index().rename(columns={0:'count'}).drop(columns='count')

detalhes_despesas = x.merge(right=y, on='SQ_DESPESA')
detalhes_despesas = detalhes_despesas[['DS_ORIGEM_DESPESA','VR_DESPESA_CONTRATADA', 'VR_PAGTO_DESPESA']].groupby('DS_ORIGEM_DESPESA').sum()
detalhes_despesas['DIF_DESPESA'] = detalhes_despesas['VR_DESPESA_CONTRATADA'] - detalhes_despesas['VR_PAGTO_DESPESA']
detalhes_despesas['TOT_DESPESA'] = detalhes_despesas['DIF_DESPESA'] + detalhes_despesas['VR_PAGTO_DESPESA']
detalhes_despesas.reset_index(inplace=True)

detalhes_despesas_prefeito = detalhes_despesas.sort_values(by='TOT_DESPESA', ascending=True, ignore_index=True)




#detalhe das despesas dos candidados a vereador:
detalhes_receita_vereador = df_receitas.query('DS_CARGO == "Vereador"')[['DS_ORIGEM_RECEITA', 'VR_RECEITA']].groupby('DS_ORIGEM_RECEITA').sum().reset_index().sort_values(by='VR_RECEITA')
x = df_despesas.query('DS_CARGO == "Vereador"')[['DS_ORIGEM_DESPESA','SQ_DESPESA','VR_DESPESA_CONTRATADA']].groupby(['DS_ORIGEM_DESPESA','SQ_DESPESA']).sum()
y = df_despesas.query('DS_CARGO == "Vereador"')[['DS_ORIGEM_DESPESA', 'SQ_DESPESA', 'VR_PAGTO_DESPESA']].value_counts(sort=False).to_frame().reset_index().rename(columns={0:'count'}).drop(columns='count')

detalhes_despesas = x.merge(right=y, on='SQ_DESPESA')
detalhes_despesas = detalhes_despesas[['DS_ORIGEM_DESPESA','VR_DESPESA_CONTRATADA', 'VR_PAGTO_DESPESA']].groupby('DS_ORIGEM_DESPESA').sum()
detalhes_despesas['DIF_DESPESA'] = detalhes_despesas['VR_DESPESA_CONTRATADA'] - detalhes_despesas['VR_PAGTO_DESPESA']
detalhes_despesas['TOT_DESPESA'] = detalhes_despesas['DIF_DESPESA'] + detalhes_despesas['VR_PAGTO_DESPESA']
detalhes_despesas.reset_index(inplace=True)

detalhes_despesas_vereador = detalhes_despesas.sort_values(by='TOT_DESPESA', ascending=True, ignore_index=True)



#Aplicação Dash:
app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='DASHBOARD ANALÍTICO ELEIÇÕES CAMPINA GRANDE(PB) 2020: RECEITAS E DESPESAS',
           style={"background-image": "linear-gradient(45deg, #3549B0, #222F70, #4863F0, #4C69FC, #4059D6)", "color":"#ffffff", "margin":"auto", "padding":"50px", "text-align":"center"}),
    
    html.Div(id='cards', style={"display":"flex",'width': '75%', "margin":"auto", "padding":"15px 0px", "text-align":"center"}),
    
    dcc.Tabs(id='tabs-party-date', value='Receita', children=[
        dcc.Tab(label='Receita', value='Receita'),
        dcc.Tab(label='Despesa', value='Despesa'),
    ], style={"display":"block",'width': '65%', "margin":"auto", "padding":"10px"}),
    html.Div(id='tabs', style={'width': '75%', "margin":"auto", "padding":"15px"}),
    
    dcc.Tabs(id='tabs_mayor_councilor', value='Prefeito', children=[
        dcc.Tab(label='Prefeito', value='Prefeito'),
        dcc.Tab(label='Vereador', value='Vereador'),
    ], style={"display":"block",'width': '65%', "margin":"auto"}),
    html.Div(children=[
        html.Div(id='mayor_councilor', style={"flex": "2",'width': '60%', "margin":"auto", "padding":"15px"}),
        html.Div(id='select_party', style={"flex": "1",'width': '35%',"margin":"auto"}),
    ],style={"display":"flex",'width': '80%', "margin":"10px auto"}),
    
    html.H6(children='Desenvolvido por Sérgio Adauto S.P. de Carvalho & Vinicius B. Montenegro', style={"background-image": "linear-gradient(45deg, #3549B0, #222F70, #4863F0, #4C69FC, #4059D6)", "color":"#ffffff", "margin":"auto", "padding":"5px", "text-align":"center"})
    ], style={ "background-color": "#E7E7E7", "margin":"auto", "padding":"0"})

@app.callback(
    Output('tabs', 'children'),
    Input('tabs-party-date', 'value')   
)
def tab_1(option):
    if option == 'Receita':
        return html.Div([
                html.H3(children='Receita dos Partidos Políticos para as Eleições de 2020', style={"display":"block",'width': '75%', "margin":"auto"}),
                dcc.Graph(
                    figure= px.bar(receita_despesa_partido, x="SG_PARTIDO", y="VR_RECEITA",
                                  barmode="group", text_auto='.2s',
                                  labels={'VR_RECEITA':'Valor da Receita', 'SG_PARTIDO':'Partidos'}, 
                                  )
                         )])
    elif option == 'Despesa':
        return html.Div([
                html.H3(children='Despesas Realizada pelos Partidos Políticos nas Eleições de 2020', style={"display":"block",'width': '75%', "margin":"auto"}),
                dcc.Graph(
                    figure= px.bar(receita_despesa_partido, x="SG_PARTIDO", y="VR_DESPESAS",
                                  barmode="group", text_auto='.2s',
                                  labels={'VR_DESPESAS':'Valor das Despesas', 'SG_PARTIDO':'Partidos'}, 
                                  )
                         )])
    
    
@app.callback(
    Output('mayor_councilor', 'children'),
    Input('tabs-party-date', 'value'),
    Input('tabs_mayor_councilor', 'value')
)  
def search_tabs(option, tabs):
    if option == 'Receita':
        if tabs == 'Prefeito':
            return html.Div([
                html.H3(children='Origem das Receita para Candidatos a Prefeito', style={"display":"block",'width': '75%', "margin":"auto"}),
                dcc.Graph(
                    figure= px.bar(detalhes_receita_prefeito, x="VR_RECEITA", y="DS_ORIGEM_RECEITA", 
                                  barmode="group", text_auto='.2s',
                                  labels={'VR_RECEITA':'Valor da Receita', 'DS_ORIGEM_RECEITA':'Origem da Receita'}, 
                                  )
                         )])
        elif tabs == 'Vereador':
            return html.Div([
                html.H3(children='Origem das Receita para Candidatos a Vereadores', style={"display":"block",'width': '75%', "margin":"auto"}),
                dcc.Graph(
                    figure= px.bar(detalhes_receita_vereador, x="VR_RECEITA", y="DS_ORIGEM_RECEITA",
                                  barmode="group", text_auto='.2s',
                                  labels={'VR_RECEITA':'Valor da Receita', 'DS_ORIGEM_RECEITA':'Origem da Receita'}, 
                                  )
                         )])
    elif option == 'Despesa':
        if tabs == 'Prefeito':
            return html.Div([
                html.H3(children='Origem das Despesas dos Candidatos a Prefeito', style={"display":"block",'width': '75%', "margin":"auto"}),
                dcc.Graph(
                    figure= px.bar(detalhes_despesas_prefeito, x="TOT_DESPESA", y="DS_ORIGEM_DESPESA", 
                                  barmode="group", text_auto='.2s',
                                  labels={'TOT_DESPESA':'Despesas', 'DS_ORIGEM_DESPESA':'Origem das Despesas'}, 
                                  )
                         )])
        elif tabs == 'Vereador':
            return html.Div([
                html.H3(children='Origem das Despesas dos Candidatos a Vereadores', style={"display":"block",'width': '75%', "margin":"auto"}),
                dcc.Graph(
                    figure= px.bar(detalhes_despesas_vereador, x="TOT_DESPESA", y="DS_ORIGEM_DESPESA", 
                                  barmode="group", text_auto='.2s',
                                  labels={'TOT_DESPESA':'Despesas', 'DS_ORIGEM_DESPESA':'Origem das Despesas'}, 
                                  )
                         )])

@app.callback(
    Output('cards', 'children'),
    Input('tabs-party-date', 'value'),
)         
def tab_1(option):
    if option == 'Receita':
        return html.Div([
                 dbc.Card( dbc.CardBody([html.H2(tot_cadidato, className="card-title"),
                                html.H4("Total de Candidatos", className="card-subtitle")]), 
                        style={"flex": "1","width": "10%", "margin":"auto", "padding":"30px", 
                              "background-color": "#ffffff", "border-radius": "10px 0px 0px 0px"}),
                 dbc.Card( dbc.CardBody([html.H2(tot_partidos, className="card-title"),
                                  html.H4("Total de Partidos", className="card-subtitle")]),
                        style={"flex": "1","width": "10%", "padding":"30px", 
                                  "background-color": "#ffffff"}),
                 dbc.Card( dbc.CardBody([html.H2(round(receita_partido['VR_RECEITA'].sum()/tot_cadidato,0), className="card-title"),
                                  html.H4("Receita Média por Candidatos", className="card-subtitle")]),
                        style={"flex": "1","width": "15%", "padding":"30px", 
                                "background-color": "#ffffff", "border-radius": "0px 0px 10px 0px"})
                   ])
    elif option == 'Despesa':
        return html.Div([
                 dbc.Card( dbc.CardBody([html.H2(tot_cadidato, className="card-title"),
                                html.H4("Total de Candidatos", className="card-subtitle")]), 
                        style={"flex": "1","width": "10%", "margin":"auto", "padding":"30px", 
                              "background-color": "#ffffff", "border-radius": "10px 0px 0px 0px"}),
                 dbc.Card( dbc.CardBody([html.H2(tot_partidos, className="card-title"),
                                  html.H4("Total de Partidos", className="card-subtitle")]),
                        style={"flex": "1","width": "10%", "padding":"30px", 
                                  "background-color": "#ffffff"}),
                 dbc.Card( dbc.CardBody([html.H2(round(despesa__partido['VR_DESPESA_CONTRATADA'].sum()/tot_cadidato,2), className="card-title"),
                                html.H4("Despesa Média Por Candidato", className="card-subtitle")]),
                        style={"flex": "1","width": "20%", "padding":"30px", 
                                "background-color": "#ffffff", "border-radius": "0px 0px 10px 0px"})
                   ])
    
@app.callback(
    Output('dd-output-container', 'children'),
    Input('tabs-party-date', 'value'),
    Input('tabs_mayor_councilor', 'value'),
    Input('demo-dropdown', 'value')
)
def update_output(option, tabs, value):
    if option == 'Receita' and tabs == "Prefeito":
        if value == 'Todos':
            return html.Div([
                        dbc.Container([
                        dash_table.DataTable(tabela_prefeito_receita.to_dict('records'),[{"name": i, "id": i} for i in tabela_prefeito_receita.columns], id='tbl'),
                        dbc.Alert(id='tbl_out')])
                   ])
        
        else:
            return html.Div([
                        dbc.Container([
                            dash_table.DataTable(tabela_prefeito_receita.query(f'Partido == "{value}"').to_dict('records'),[{"name": i, "id": i} for i in tabela_prefeito_receita.columns], id='tbl'),
                            dbc.Alert(id='tbl_out')])
                    ])
    elif option == 'Despesa' and tabs == "Prefeito":
        if value == 'Todos':
            return html.Div([
                        dbc.Container([
                        dash_table.DataTable(tabela_prefeito_despesa.to_dict('records'),[{"name": i, "id": i} for i in tabela_prefeito_despesa.columns], id='tbl'),
                        dbc.Alert(id='tbl_out')])
                   ])
        else:
            return html.Div([
                        dbc.Container([
                            dash_table.DataTable(tabela_prefeito_despesa.query(f'Partido == "{value}"').to_dict('records'),[{"name": i, "id": i} for i in tabela_prefeito_despesa.columns], id='tbl'),
                            dbc.Alert(id='tbl_out')])
                    ])
    elif option == 'Receita' and tabs == "Vereador":
        if value == 'Todos':
            return html.Div([
                        dbc.Container([
                        dash_table.DataTable(tabela_vereador_receita.to_dict('records'),[{"name": i, "id": i} for i in tabela_vereador_receita.columns], id='tbl'),
                        dbc.Alert(id='tbl_out')])
                   ])
            
        else:
            return html.Div([
                        dbc.Container([
                            dash_table.DataTable(tabela_vereador_receita.query(f'Partido == "{value}"').to_dict('records'),[{"name": i, "id": i} for i in tabela_vereador_receita.columns], id='tbl'),
                            dbc.Alert(id='tbl_out')])
                    ])
    elif option == 'Despesa' and tabs == "Vereador":
        if value == 'Todos':
            return html.Div([
                        dbc.Container([
                        dash_table.DataTable(tabela_vereador_despesa.to_dict('records'),[{"name": i, "id": i} for i in tabela_vereador_despesa.columns], id='tbl'),
                        dbc.Alert(id='tbl_out')])
                   ])
            
        else:
            return html.Div([
                        dbc.Container([
                            dash_table.DataTable(tabela_vereador_despesa.query(f'Partido == "{value}"').to_dict('records'),[{"name": i, "id": i} for i in tabela_vereador_despesa.columns], id='tbl'),
                            dbc.Alert(id='tbl_out')])
                    ])
@app.callback(
    Output('select_party', 'children'),
    Input('tabs_mayor_councilor', 'value')
)
def select_search(tabs):
    if tabs == "Prefeito":
            return html.Div([
                            dcc.Dropdown(['Todos','PODE', 'PC do B', 'PSL', 'PSD', 'PSOL'], 'Todos', id='demo-dropdown'),
                            html.Div(id='dd-output-container', style={"overflow": "auto", "height":"200px"})
                            ],style={"display":"block",'width': '100%', "margin":"10px auto"})
    elif tabs == "Vereador":
           return html.Div([
                            dcc.Dropdown(['Todos','PODE', 'PROS', 'DEM', 'PSD', 'REPUBLICANOS', 'PC do B', 'PTB',
                                           'PSL', 'CIDADANIA', 'PT', 'UP', 'DC', 'PATRIOTA', 'MDB', 'PSC',
                                           'SOLIDARIEDADE', 'PP', 'PSB', 'PMN', 'PCO'], 'Todos', id='demo-dropdown'),
                            html.Div(id='dd-output-container', style={"overflow": "auto", "height":"200px"})
                            ],style={"display":"block",'width': '100%', "margin":"10px auto"})

    
    
if __name__ == '__main__':
     app.run_server(debug=True, use_reloader=False)