<h1>Dashboard Python - Eleições Paraibana 2020</h1>
<p>Os Dados utilizados nesse projeto são das eleções de 2020 do estado da Paraíba, coletado no Portal dos dados Abertos do <a href="https://dadosabertos.tse.jus.br/">TSE</a>:</p>
<p>Esse projeto foi desenvolvido e elabora para atender as demandas avaliativas da disciplina de Estatística Computacional no Instituo Federal da Paraíba,
 Campus Campina Grande.</p>
 
<ul>
 <p> -- Foram utiliza as seguintes bibliotecas para o seu desenvolvimento:</p>
  <li>Pandas;
   <li>Numpy;
    <li>Dash;
     <li>dash_bootstrap_components;
      <li>Plotly;
       <p><strong>OBS:</strong> Foi preciso conhecimento básico em HTML e CSS para o desenvolvimento do Dashboard.</p>
</ul>
<br>
<p><strong>Descrição das variáveis encontrada nas tabelas:</strong></p>
<code><pre>
<strong>TABELA RECEITAS_CANDIDATOS:</strong>
Variável – Descrição
DT _GERACAO	- Data de geração das informações data da extração dos dados.
HH_GERACAO - Hora de geração das informações hora da extração dos dados - Horário de Brasília.
ANO_ELEICAO - Ano da eleição (referente ao ano eleitoral de pesquisa).
CD _TIPO_ELEICAO - Código do tipo de eleição.
NM_TIPO_ELEICAO - Nome do tipo de eleição.
CD_ELEICAO - Código da eleição.
DS_ELEICAO - Descrição da eleição.
DT_ELEICAO - Data em que ocorreu a eleição.
ST_TURNO - O indicativo se prestador de contas teve prestação para 2º turno.
TP_PRESTACAO_CONTAS - Tipo de entrega da prestação de contas. Pode assumir os valores: Parcial	(referente à entrega parcial de prestação de contas); Final (referente à entrega final da prestação); Relatório financeiro (referente à entrega do relatório financeiro).
DT_PRESTACAO_CONTAS - Data de entrega da prestação de contas junto ao TSE.
SQ _PRESTADOR_CONTAS - Sequencial de identificação do prestador de contas junto ao TSE.
SG_UF - Sigla da unidade da federação de abrangência do prestador de contas.
SG_UE - Sigla da Unidade Eleitoral do candidato (Em caso de eleição majoritária é a sigla da UF que o candidato concorre e em caso de eleição municipal é o código TSE do município).
NM_UE - Nome de Unidade Eleitoral do candidato (Em caso de eleição majoritária é o nome da UF que o candidato concorre e em caso de eleição municipal é o nome do município).
NR _CNPJ_PRESTADOR_CONTA	 - Número do CNPJ do prestador de contas.
CD_CARGO - Código do cargo do candidato prestador de contas.
DS _CARGO - Descrição do cargo do candidato prestador de contas.
SQ _CANDIDATO - Sequencial do candidato prestador de contas.
NR _CANDIDATO - Número do candidato prestador de contas.
NM _CANDIDATO - Nome completo do candidato.
NR _CPF_CANDIDATO - CPF do candidato registrado na Justiça Eleitoral.
NR_CPF	_VICE_CANDIDATO - CPF do candidato à vice/suplente do titular, se houver.
NR_PARTIDO - Número do partido do candidato.
SG_PARTIDO - Sigla do partido do candidato.
NM_PARTIDO - Nome do partido do candidato.
CD_FONTE_RECEITA - Código de identificação do tipo de fonte de recursos da doação, informado pelo prestador de contas em relação à doação.
DS_FONTE_RECEITA - Descrição do tipo de fonte do recurso da doação, informado pelo prestador de contas em relação à doação.
CD_ORIGEM_RECEITA - Código de identificação do tipo de origem do recurso (DRD), informado pelo prestador de contas em relação à doação.
DS_ORIGEM_RECEITA - Descrição do o tipo de origem do recurso (DRD), informado pelo prestador de contas em relação à doação.
CD_NATUREZA_RECEITA - Código de identificação da natureza do tipo de espécie de recursos da doação.
DS_NATUREZA_RECEITA - Descrição da natureza do tipo espécie do recurso da doação. Pode assumir os valores 'Financeiro' ou 'Estimável'.
CD_ESPECIE_RECEITA - Código de identificação do tipo de espécie de recursos da doação.
DS_ESPECIE_RECEITA - Descrição do tipo de espécie do recurso da doação, quando natureza do recurso for igual a financeiro.
CD_CNAE_DOADOR - Código CNAE do doador, se pessoa jurídica.
DS_CNAE_DOADOR - Descrição do CNAE (Código do Setor Econômico) do doador, se pessoa jurídica.
NR_CPF_CNPJ_DOADOR - Numero do CPF/CNPJ do doador declarado à Justiça Eleitoral.
NM_DOADOR - Nome do doador declarado à Justiça Eleitoral.
NM_DOADOR_RFB - Nome do doador cadastrado na Receita Federal do Brasil.
CD_ESFERA_PARTIDARIA_DOADOR - Código do tipo de esfera partidária do doador, quando doador 'Órgão partidário'.
DS_ESFERA_PARTIDARIA_DOADOR - Descrição do tipo de esfera partidária do doador. Pode assumir os valores: 'Nacional', 'Estadual', 'Distrital' e 'Municipal'. Válido para quando doador 'Órgão partidário'.
SG_UF_DOADOR - Sigla da unidade da federação do doador, quando doador candidato ou órgão partidário.
CD_MUNICIPIO_DOADOR - Código do município do doador, quando a esfera partidária do doador for municipal.
NM_MUNICIPIO_DOADOR - Descrição do município do doador, quando a esfera partidária do doador for municipal.
SQ_CANDIDATO_DOADOR - Sequencial do candidato doador, quando doação de candidato.
NR_CANDIDATO_DOADOR - Número do candidato declarado pelo prestador de contas, quando doação de candidato.
CD_CARGO_CANDIDATO_DOADOR - Código do cargo do candidato declarado pelo prestador de contas, quando doação de candidato.
DS_CARGO_CANDIDATO_DOADOR - Descrição do cargo do candidato declarado pelo prestador de contas, quando doação de candidato.
NR_PARTIDO_DOADOR	 - Número do partido declarado pelo prestador de contas, quando doador candidato ou órgão partidário.
SG_PARTIDO_DOADOR	 - Sigla do partido declarado pelo prestador de contas, quando doador candidato ou órgão partidário.
NM_PARTIDO_DOADOR - Nome do partido declarado pelo prestador de contas, quando doador candidato ou órgão partidário.
NR_RECIBO_DOACAO - Número de recibo de doação informada pelo prestador de contas em relação à doação.
NR_DOCUMENTO_DOACAO - Número do documento de recebimento informado pelo prestador de contas em relação à doação.
SQ_RECEITA - Sequencial de identificação do registro da receita declarada pelo prestador de contas.
DT_RECEITA - Data da doação declarada à Justiça Eleitoral.
DS_RECEITA - Descrição Resumida informada pelo prestador de contas em relação à doação.
VR_RECEITA - Valor da doação em Reais (R$).

<br>
<strong>TABELA DESPESAS-PAGAS-CANDIDATOS:</strong>

Variável – Descrição
DT_GERACAO - Data de geração das informações (data da extração dos dados).
HH_GERACAO - Hora de geração das informações (hora da extração dos dados) - Horário de Brasília.
ANO_ELEICAO	- Ano da eleição (referente ao ano eleitoral de pesquisa	).
CD_TIPO_ELEICAO - Código do tipo de eleição.
NM_TIPO_ELEICAO - Nome do tipo de eleição.
CD_ELEICAO - Código da eleição.
DS_ELEICAO - Descrição da eleição.
DT_ELEICAO - Data em que ocorreu a eleição.
ST_TURNO - Indicativo se o prestador de contas participou do 2º turno.
TP_PRESTACAO_CONTAS - Tipo de entrega da prestação de contas. Pode assumir os valores: Relatório financeiro (referente à entrega do relatório financeiro); Parcial (referente à entrega parcial de prestação de contas)	; Final (referente à entrega final da prestação).
DT_PRESTACAO_CONTAS  -  Data de entrega da prestação de contas junto ao TSE.
SQ_PRESTADOR_CONTAS - Sequencial de identificação do prestador de contas junto à Justiça Eleitoral.
SG_UF - Sigla da unidade da federação de abrangência do prestador de contas.
DS_TIPO_DOCUMENTO	 Tipo de documento. Pode assumir os valores 'Recibo', 'Cupom Fiscal', 'Fatura', 'Nota Fiscal', 'Duplicata', 'Outros'. 
NR_DOCUMENTO Número de documento que comprove a despesa.
CD_FONTE_DESPESA - Código de identificação do tipo de fonte de recursos da despesa, informado pelo prestador de contas.
DS_FONTE_DESPESA - Descrição do tipo de fonte do recurso da despesa, informado pelo prestador de contas.
CD_ORIGEM_DESPESA - Código de identificação do tipo de origem da despesa (DRD), informado pelo prestador de contas em relação à despesa.
DS_ORIGEM_DESPESA	- Descrição do tipo de origem da despesa (DRD)	, informado pelo prestador de contas em relação à despesa. 
CD_NATUREZA_DESPESA - Código da natureza de recursos da despesa.
DS_NATUREZA_DESPESA - Descrição da natureza de recursos da despesa. Pode assumir os valores 'Financeiro' ou 'Estimável'.
CD_ESPECIE_RECURSO -  Código de identificação da espécie de recursos para pagamento da despesa.
DS_ESPECIE_RECURSO - Descrição da espécie do recurso para pagamento da despesa.
SQ_DESPESA - Sequencial de identificação do registro da despesa declarada pelo prestador de contas.
SQ_PARCELAMENTO_DESPESA	- Sequencial de identificação do registro da despesa parcelada paga, declarada pelo prestador de contas.
DT_PAGTO_DESPESA - Data de pagamento da despesa declarada à Justiça Eleitoral.
DS_DESPESA - Descrição da despesa.
VR_PAGTO_DESPESA	Valor pago da despesa em Reais (R$), informada pelo prestador de contas.

<br>
<strong>TABELA DESPESAS_CONTRATADAS_CANDIDATOS:</strong>

Variável – Descrição
DT_GERACAO - Data de geração das informações (data da extração dos dados).
HH_GERACAO - Hora de geração das informações (hora da extração dos dados)	- Horário de Brasília.
ANO_ELEICAO - Ano da eleição	(referente ao ano eleitoral de pesquisa).
CD - Código do tipo de eleição.
NM_TIPO_ELEICAO - Nome do tipo de eleição.
CDCódigo da eleição.
DS_ELEICAO - Descrição da eleição.
DT_ELEICAO - Data em que ocorreu a eleição.
ST_TURNO - O indicativo se prestador de contas teve prestação para 2º turno.
TP_PRESTACAO_CONTAS - Tipo de entrega da prestação de contas. Pode assumir os valores: Parcial	(referente à entrega parcial de prestação de contas); Final (referente à entrega final da prestação); Relatório financeiro (referente à entrega do relatório financeiro).
DT_PRESTACAO_CONTAS -Data de entrega da prestação de contas junto ao TSE.
SQ_PRESTADOR_CONTAS - Sequencial de identificação do prestador de contas junto ao TSE.
SG_UF - Sigla da unidade da federação de abrangência do prestador de contas.
SG_UE - Sigla da Unidade Eleitoral do candidato (Em caso de eleição majoritária é a sigla da UF que o candidato concorre e em caso de eleição municipal é o código TSE do município).
NM_UE	 - Nome de Unidade Eleitoral do candidato (Em caso de eleição majoritária é o nome da UF que o candidato concorre e em caso de eleição municipal é o nome do município	).
NR_CNPJ_PRESTADOR_CONTA - Numero do CNPJ do prestador de contas.
CD_CARGO - Código do cargo do candidato prestador de contas.
DS_CARGO - Descrição do cargo do candidato prestador de contas.
SQ_CANDIDATO - Sequencial do candidato prestador de contas.
NR_CANDIDATO - Número do candidato prestador de contas.
NM_CANDIDATO - Nome completo do candidato.
NR_CPF_CANDIDATO - CPF do candidato registrado na Justiça Eleitoral.
NR_CPF	_VICE_CANDIDATO - CPF do candidato à vice/suplente do titular, se houver.
NR_PARTIDO - Número do partido do candidato.
SG_PARTIDO - Sigla do partido do candidato.
NM_PARTIDO - Nome do partido do candidato.
CD_TIPO_FORNECEDOR - Código de identificação do tipo de fornecedor informada pelo prestador de contas em relação à despesa.
DS_TIPO_FORNECEDOR - Descrição do tipo de fornecedor informada pelo prestador de contas em relação à despesa. Pode assumir os valores: 'Pessoa Física' ou 'Pessoa Jurídica'.
CD_CNAE_FORNECEDOR - Código CNAE do fornecedor de bens e/ou serviços, se pessoa jurídica.
DS_CNAE_FORNECEDOR - Descrição do CNAE (Código do Setor Econômico) do fornecedor de bens e/ou serviços, se pessoa jurídica.
NR_CPF_CNPJ_FORNECEDOR - Número do CPF/CNPJ do fornecedor de bens e/ou serviços informada pelo prestador de contas em relação à despesa.
NM_FORNECEDOR - Nome do fornecedor de bens e/ou serviços declarado a Justiça Eleitoral, informada pelo prestador de contas em relação à despesa.
NM_FORNECEDOR_RFB - Nome do fornecedor cadastrado na Receita Federal do Brasil, informada pelo prestador de contas em relação à despesa.
CD_ESFERA_PART_FORNECEDOR - Código do tipo de esfera partidária do fornecedor, quando fornecedor 'Órgão partidário'.
DS_ESFERA_PART_FORNECEDOR - Descrição do tipo de esfera partidária do fornecedor. Pode assumir os valores: 'Nacional', 'Estadual', 'Distrital' e 'Municipal'. Válida para quando fornecedor 'Órgão partidário'.
SG_UF_FORNECEDOR - Sigla da unidade da federação do fornecedor, quando fornecedor candidato ou órgão partidário.
CD_MUNICIPIO_FORNECEDOR	- Código do município do fornecedor, quando a esfera partidária do fornecedor for municipal.
NM_MUNICIPIO_FORNECEDOR	- Descrição do município do fornecedor, quando a esfera partidária do fornecedor for municipal.
SQ_CANDIDATO_FORNECEDOR - Sequencial do candidato fornecedor, quando fornecedor candidato.
NR_CANDIDATO_FORNECEDOR - Número do candidato declarado pelo prestador de contas, quando fornecedor candidato.
CD_CARGO_FORNECEDOR - Código do cargo do candidato declarado pelo prestador de contas, quando fornecedor.
DS_CARGO_FORNECEDOR - Descrição do cargo do candidato declarado pelo prestador de contas, quando fornecedor .
NR_PARTIDO_FORNECEDOR - Número do partido declarado pelo prestador de contas, quando fornecedor candidato ou órgão partidário.
SD_PARTIDO_FORNECEDOR - Sigla do partido declarado pelo prestador de contas, quando fornecedor candidato ou órgão partidário.
NM_PARTIDO_FORNECEDOR - Nome do partido declarado pelo prestador de contas, quando fornecedor candidato ou órgão partidário.
DS_TIPO_DOCUMENTO	 - Tipo de documento. Podendo assumir os valores 'Recibo', 'Cupom Fiscal', 'Fatura', 'Nota Fiscal', 'Duplicata', 'Outros'.
NR_DOCUMENTO - Número de documento que comprove a despesa.
SQ_DESPESA - Sequencial de identificação do registro da despesa declarada pelo prestador de contas.
DT_DESPESA - Data da despesa declarada à Justiça Eleitoral.
DS_DESPESA - Descrição do gasto no elenco de aplicações informada pelo prestador de contas em relação à despesa.
VR_DESPESA_CONTRATADA - Valor da despesa contratada em Reais (R$), informada pelo prestador de contas em relação à despesa.	
</pre></code>
