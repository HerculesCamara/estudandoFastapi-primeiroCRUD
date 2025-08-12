from database import engine

def test_connection():
    try:
        with engine.connect() as connection:
            result = connection.execute("SELECT 1")
            print("Conexão OK! Resultado do teste:", result.scalar())
    except Exception as e:
        print("Erro ao conectar no banco:", e)

if __name__ == "__main__":
    test_connection()
