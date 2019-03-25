def drop_tables():
    pass

def create_tables():
    pass

def init_db() -> None:
    """ (re)Create tables in database """

    drop_tables(TABLES)
    create_tables(TABLES)
