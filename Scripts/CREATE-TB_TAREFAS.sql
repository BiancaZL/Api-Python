CREATE TABLE TB_TAREFAS
(
	NOME_USUARIO VARCHAR(15),
	ID_TAREFA VARCHAR(10),
	NOME_TAREFA VARCHAR(50),
	TIPO_TAREFA VARCHAR(10),
	DATA_CRIACAO VARCHAR(8),
	DATA_CONCLUSAO VARCHAR(8),
	TAREFA_CONCLUIDA BIT NOT NULL, --Pode ser 0 ou 1
)
