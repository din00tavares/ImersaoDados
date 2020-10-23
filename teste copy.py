import pandas as pd

def ajustaCampos():


    resultado = chunk[['NU_ANO','NU_IDADE','NU_NOTA_CN','NU_NOTA_CH','NU_NOTA_LC','NU_NOTA_MT','NU_NOTA_COMP1','NU_NOTA_COMP2','NU_NOTA_COMP3','NU_NOTA_COMP4','NU_NOTA_COMP5','NU_NOTA_REDACAO']]





dfChunks = pd.read_csv('MICRODADOS_ENEM_2019.csv', chunksize=100, sep=';', encoding='latin1')

camposRelevantes = ['NU_INSCRICAO','NU_ANO','CO_MUNICIPIO_RESIDENCIA','NU_IDADE','TP_SEXO','TP_ESTADO_CIVIL','TP_COR_RACA','TP_NACIONALIDADE','CO_MUNICIPIO_NASCIMENTO','TP_ST_CONCLUSAO','TP_ANO_CONCLUIU','TP_ESCOLA','TP_ENSINO','IN_TREINEIRO','CO_MUNICIPIO_ESC','TP_DEPENDENCIA_ADM_ESC','TP_LOCALIZACAO_ESC','TP_SIT_FUNC_ESC','IN_BAIXA_VISAO','IN_CEGUEIRA','IN_SURDEZ','IN_DEFICIENCIA_AUDITIVA','IN_SURDO_CEGUEIRA','IN_DEFICIENCIA_FISICA','IN_DEFICIENCIA_MENTAL','IN_DEFICIT_ATENCAO','IN_DISLEXIA','IN_DISCALCULIA','IN_AUTISMO','IN_VISAO_MONOCULAR','IN_OUTRA_DEF','IN_GESTANTE','IN_LACTANTE','IN_IDOSO','IN_ESTUDA_CLASSE_HOSPITALAR','IN_SEM_RECURSO','IN_BRAILLE','IN_AMPLIADA_24','IN_AMPLIADA_18','IN_LEDOR','IN_ACESSO','IN_TRANSCRICAO','IN_LIBRAS','IN_TEMPO_ADICIONAL','IN_LEITURA_LABIAL','IN_MESA_CADEIRA_RODAS','IN_MESA_CADEIRA_SEPARADA','IN_APOIO_PERNA','IN_GUIA_INTERPRETE','IN_COMPUTADOR','IN_CADEIRA_ESPECIAL','IN_CADEIRA_CANHOTO','IN_CADEIRA_ACOLCHOADA','IN_PROVA_DEITADO','IN_MOBILIARIO_OBESO','IN_LAMINA_OVERLAY','IN_PROTETOR_AURICULAR','IN_MEDIDOR_GLICOSE','IN_MAQUINA_BRAILE','IN_SOROBAN','IN_MARCA_PASSO','IN_SONDA','IN_MEDICAMENTOS','IN_SALA_INDIVIDUAL','IN_SALA_ESPECIAL','IN_SALA_ACOMPANHANTE','IN_MOBILIARIO_ESPECIFICO','IN_MATERIAL_ESPECIFICO','IN_NOME_SOCIAL','CO_MUNICIPIO_PROVA','TP_PRESENCA_CN','TP_PRESENCA_CH','TP_PRESENCA_LC','TP_PRESENCA_MT','NU_NOTA_CN','NU_NOTA_CH','NU_NOTA_LC','NU_NOTA_MT','TP_LINGUA','TP_STATUS_REDACAO','NU_NOTA_COMP1','NU_NOTA_COMP2','NU_NOTA_COMP3','NU_NOTA_COMP4','NU_NOTA_COMP5','NU_NOTA_REDACAO','Q001','Q002','Q003','Q004','Q005','Q006','Q007','Q008','Q009','Q010','Q011','Q012','Q013','Q014','Q015','Q016','Q017','Q018','Q019','Q020','Q021','Q022','Q023','Q024','Q025']

dominio = {'id': [1,0],'Descricao': ['Sim','Não']}
dfDominioSimNao = pd.DataFrame(dominio,columns=dominio.keys())
dominio = {'id': [0,1],'Descricao': ['Inglês','Espanhol']}
dfDominioLingua = pd.DataFrame(dominio,columns=dominio.keys())
dominio = {'id': [0,1,2],'Descricao': ['Faltou à prova','Presente na prova','Eliminado na prova']}
dfDominioPresenca = pd.DataFrame(dominio,columns=dominio.keys())
dominio = {'id': ['M','F'],'Descricao': ['Masculino','Feminino']}
dfDominioSexo = pd.DataFrame(dominio,columns=dominio.keys())
dominio = {'id': [0,1,2,3,4],'Descricao': ['Não informado','Solteiro(a)','Casado(a)/Mora com companheiro(a)','Divorciado(a)/Desquitado(a)/Separado(a)','Viúvo(a)']}
dfDominioEstadoCivil = pd.DataFrame(dominio,columns=dominio.keys())
dominio = {'id': [0,1,2,3,4,5],'Descricao': ['Não declarado','Branca','Preta','Parda','Amarela','Indígena']}
dfDominioCorRaca = pd.DataFrame(dominio,columns=dominio.keys())
dominio = {'id': [0,1,2,3,4],'Descricao': ['Não informado','Brasileiro(a)','Brasileiro(a) Naturalizado(a)','Estrangeiro(a)','Brasileiro(a) Nato(a), nascido(a) no exterior']}
dfDominioNacionalidade = pd.DataFrame(dominio,columns=dominio.keys())
dominio = {'id': [0,1,2,3,4],'Descricao': ['Já concluí o Ensino Médio', 'Estou cursando e concluirei o Ensino Médio em 2019', 'Estou cursando e concluirei o Ensino Médio após 2019', 'Não concluí e não estou cursando o Ensino Médio']}
dfDominioConclusaoEnsinoMedio = pd.DataFrame(dominio,columns=dominio.keys())
dominio = {'id': [0,1,2,3,4,5,6,7,8,9,10,11,12,13],'Descricao': ['Não informado','2018','2017','2016','2015','2014','2013','2012','2011','2010','2009','2008','2007','Antes de 2007']}
dfDominioAnoConclusao = pd.DataFrame(dominio,columns=dominio.keys())
dominio = {'id': [1,2,3,4],'Descricao': ['Não Respondeu','Pública','Privada','Exterior']}
dfDominioTipoEscola = pd.DataFrame(dominio,columns=dominio.keys())
dominio = {'id': [1,2,3],'Descricao': ['Ensino Regular','Educação Especial - Modalidade Substitutiva','Educação de Jovens e Adultos']}
dfDominioTipoEnsino = pd.DataFrame(dominio,columns=dominio.keys())
dominio = {'id': [1,2,3,4],'Descricao': ['Federal','Estadual','Municipal','Privada']}
dfDominioDependenciaAdministrativa = pd.DataFrame(dominio,columns=dominio.keys())
dominio = {'id': [1,2],'Descricao': ['Urbana','Rural']}
dfDominioLocalicazaoEscola = pd.DataFrame(dominio,columns=dominio.keys())
dominio = {'id': [1,2,3],'Descricao': ['Em atividade','Paralisada','Extinta']}
dfDominioSituacaoEscola = pd.DataFrame(dominio,columns=dominio.keys())
dominio = {'id': [1,2,3,4,5,6,7,8,9],'Descricao': ['Sem problemas','Anulada','Cópia Texto Motivador','Em Branco','Fuga ao tema','Não atendimento ao tipo textual','Texto insuficiente','Parte desconectada']}
dfDominioRedacao = pd.DataFrame(dominio,columns=dominio.keys())
dominio = {'id':['A','B','C','D','E','F','G','H'] ,'Descricao': ['Nunca estudou.','Não completou a 4ª série/5º ano do Ensino Fundamental.','Completou a 4ª série/5º ano, mas não completou a 8ª série/9º ano do Ensino Fundamental.','Completou a 8ª série/9º ano do Ensino Fundamental, mas não completou o Ensino Médio.','Completou o Ensino Médio, mas não completou a Faculdade.','Completou a Faculdade, mas não completou a Pós-graduação.','Completou a Pós-graduação.','Não sei.']}
dfDominioQEscolaridade = pd.DataFrame(dominio,columns=dominio.keys())
dominio = {'id':['A','B','C','D','E','F'] ,'Descricao': ['Atividade Agrária', 'Atividade Básica', 'Atividade Técnica', 'Atividade Especializada', 'Atividade Gerencial', 'Não sei.'],'Detalhamento' : ['Grupo 1: Lavrador, agricultor sem empregados, bóia fria, criador de animais (gado, porcos, galinhas, ovelhas, cavalos etc.), apicultor, pescador, lenhador, seringueiro, extrativista.','Grupo 2: Diarista, empregado doméstico, cuidador de idosos, babá, cozinheiro (em casas particulares), motorista particular, jardineiro, faxineiro de empresas e prédios, vigilante, porteiro, carteiro, office-boy, vendedor, caixa, atendente de loja, auxiliar administrativo, recepcionista, servente de pedreiro, repositor de mercadoria.','Grupo 3: Padeiro, cozinheiro industrial ou em restaurantes, sapateiro, costureiro, joalheiro, torneiro mecânico, operador de máquinas, soldador, operário de fábrica, trabalhador da mineração, pedreiro, pintor, eletricista, encanador, motorista, caminhoneiro, taxista.','Grupo 4: Professor (de ensino fundamental ou médio, idioma, música, artes etc.), técnico (de enfermagem, contabilidade, eletrônica etc.), policial, militar de baixa patente (soldado, cabo, sargento), corretor de imóveis, supervisor, gerente, mestre de obras, pastor, microempresário (proprietário de empresa com menos de 10 empregados), pequeno comerciante, pequeno proprietário de terras, trabalhador autônomo ou por conta própria.','Grupo 5: Médico, engenheiro, dentista, psicólogo, economista, advogado, juiz, promotor, defensor, delegado, tenente, capitão, coronel, professor universitário, diretor em empresas públicas ou privadas, político, proprietário de empresas com mais de 10 empregados.','Não sei.']}
dfDominioQTrabalhoResponsavel = pd.DataFrame(dominio,columns=dominio.keys())
dominio = {'id': ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q'],'Descricao' : ['Nenhuma renda.','Até R$ 998,00.','De R$ 998,01 até R$ 1.497,00.','De R$ 1.497,01 até R$ 1.996,00.','De R$ 1.996,01 até R$ 2.495,00.','De R$ 2.495,01 até R$ 2.994,00.','De R$ 2.994,01 até R$ 3.992,00.','De R$ 3.992,01 até R$ 4.990,00.','De R$ 4.990,01 até R$ 5.988,00.','De R$ 5.988,01 até R$ 6.986,00.','De R$ 6.986,01 até R$ 7.984,00.','De R$ 7.984,01 até R$ 8.982,00.','De R$ 8.982,01 até R$ 9.980,00.','De R$ 9.980,01 até R$ 11.976,00.','De R$ 11.976,01 até R$ 14.970,00.','De R$ 14.970,01 até R$ 19.960,00.','Mais de R$ 19.960,00.'],'RendaMinima': [0,998,1497,1996,2495,2994,3992,4990,5988,6986,7984,8982,9980,11976,14970,19960,24950],'RendaMaxima': [0,0,998 ,1497 ,1996 ,2495 ,2994 ,3992 ,4990 ,5988 ,6986 ,7984 ,8982 ,9980 ,11976 ,14970 ,19960]}
dfDominioQRenda = pd.DataFrame(dominio,columns=dominio.keys())
dominio = {'id': ['A','B','C','D'],'Descricao': ['Não.','Sim, um ou dois dias por semana.','Sim, três ou quatro dias por semana.','Sim, pelo menos cinco dias por semana.']}
dfDominioQEmpregadaDomestica = pd.DataFrame(dominio,columns=dominio.keys())
dominio = {'id': ['A','B'],'Descricao': ['Não.','Sim.']}
dfDominioQNaoSim = pd.DataFrame(dominio,columns=dominio.keys())
dominio = {'id': ['A','B','C','D','E'] ,'Descricao': ['Não.','Sim, um(a).','Sim, dois(duas).','Sim, três.','Sim, quatro ou mais.']}
dfDominioQQuantosN = pd.DataFrame(dominio,columns=dominio.keys())
dfCidades = pd.read_csv('MunicipiosBrasil.csv', sep=';', encoding='latin1')


chunk_list = []
for chunk in dfChunks:
    chunk = chunk[camposRelevantes]
    chunk_list.append(ajustaCampos())
df_concat = pd.concat(chunk_list)

df_concat.to_csv('df_enem_2019_completo_filtrado.csv', encoding='utf-8', index=False)











