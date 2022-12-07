-- Inserção de Tarefa Diária
INSERT INTO TB_TAREFAS(
	NOME_USUARIO,
	ID_TAREFA, 
	NOME_TAREFA, 
	TIPO_TAREFA, 
	DATA_CRIACAO, 
	DATA_CONCLUSAO,
	TAREFA_CONCLUIDA
)
VALUES(
'BiancaZL',
'1',
'Fazer trabalho de Tópicos em Informática',
'Diária',
'021222', -- DDMMAA
'0',
0
)


-- Inserção de Tarefa no Inventário
INSERT INTO TB_TAREFAS(
	NOME_USUARIO,
	ID_TAREFA, 
	NOME_TAREFA, 
	TIPO_TAREFA, 
	DATA_CRIACAO, 
	DATA_CONCLUSAO,
	TAREFA_CONCLUIDA
)
VALUES(
'BiancaZL',
'2',
'Fazer tarefa de Inteligência artificial',
'Inventário',
'021222', -- DDMMAA
'0',
0
)

