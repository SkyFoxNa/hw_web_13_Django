import runpy


def migrate_database():
    runpy.run_module("migration")


if __name__ == "__main__":
    migrate_database()
