from sqlalchemy import create_engine, text
from settings import DB_NAME, DB_PASSWORD, DB_SERVER_NAME, DB_USER

def insert(message, person_name):

	db = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_SERVER_NAME}/{DB_NAME}')
	with db.connect() as connection:
		with connection.begin():
			connection.execute(text(f"""INSERT INTO usage ("date", person, completion_tokens, prompt_tokens, total_tokens) 
				VALUES (CURRENT_TIMESTAMP(0), '{person_name}',{a_completion_tokens},{a_prompt_tokens},{a_total_tokens})
				"""))

def statistic():
	db = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_SERVER_NAME}/{DB_NAME}')
	sql = 'SELECT person, SUM(completion_tokens) as compl, SUM(prompt_tokens) as prompt, SUM(total_tokens) as total FROM "usage" GROUP BY person'
	dbconn = db.raw_connection()
	df = pd.read_sql(sql, dbconn)
	dbconn.close()
	return df.to_string(index=False, justify='initial')


if __name__ == '__main__':
	insert('test note', 'chandler')
