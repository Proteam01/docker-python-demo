import psycopg2 

def create_tables():
    conn = psycopg2.connect("dbname=docker-user user=docker-user password=sample host=localhost port=5432")
    statements = [
        "CREATE TABLE books (id integer NOT NULL,name character varying(80),CONSTRAINT books_pkey PRIMARY KEY (id))",
        "insert into books values ( 1, 'C++')",
        "insert into books values (2,'Java')",
        "insert into books values (3,'C#')",
        "insert into books values (4,'Python')"
    ]
    cursor = conn.cursor()
    for statement in statements:
        print(statement)
        cursor.execute(statement)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    print('creating tables...')
    create_tables()
