from pysqlified.bformatting import log, print_sql_query


def main():
	log("Hello from pysqlified!", 'success')
	log("Hello from pysqlified!", 'warning')
	log("Hello from pysqlified!", 'error')
	log("Hello from pysqlified!", 'note')

	print_sql_query('''CREATE IF NOT EXISTS TABLE Users(
	id INTEGER PRIMARY KEY,
	name STRING UNIQUE,
	age INTEGER
)
''')


if __name__ == "__main__":
	main()
