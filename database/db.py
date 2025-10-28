import sqlite3

from tkinter import messagebox

from utils.treatment import parse_price_filter
from utils.generator import *

def connect_db():
    try:
        conn = sqlite3.connect("rentcar.db")
        return conn
    except sqlite3.OperationalError as e:
        messagebox.showerror("Erro de conexão", f"Não foi possível conectar ao banco de dados: {e}")
        return None
    
def create_table():
    conn = connect_db()
    if conn is None:
        messagebox.showerror("Erro", "Não foi possível conectar ao banco de dados.")
        return False

    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS cars (
                id INTEGER PRIMARY KEY,
                model TEXT NOT NULL,
                year INTEGER NOT NULL,
                license_plate TEXT UNIQUE NOT NULL,
                fuel_type TEXT NOT NULL,
                category TEXT NOT NULL,
                brand TEXT NOT NULL,
                transmission TEXT NOT NULL,
                price_per_day REAL NOT NULL
            )
        ''')
        conn.commit()
    except sqlite3.IntegrityError as e:
        messagebox.showerror("Erro ao criar tabela", f"Não foi possível criar a tabela: {e}")
    except sqlite3.OperationalError as e:
        messagebox.showerror(f"Erro operacional: {e}")
    except Exception as e:
        messagebox.showerror(f"Erro inesperado: {e}")
    finally:
        conn.close()


def validateCarId(carId=None):
    conn = connect_db()
    if conn is None:
        messagebox.showerror("Erro", "Não foi possível conectar ao banco de dados.")
        return False
    
    try:
        if carId == None:
            carId = randomCarId()

        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM cars WHERE id = ?", (carId,))

        exists = cursor.fetchone()[0] > 0

        if exists:
            validateCarId(randomCarId())
        else:
            return carId
    except sqlite3.OperationalError as e:
        messagebox.showerror(f"Erro operacional: {e}")
        return False
    except Exception as e:
        messagebox.showerror(f"Erro inesperado: {e}")
        return False
    finally:
        conn.close()


def insert_car(car_data):
    conn = connect_db()
    if conn is None:
        messagebox.showerror("Erro", "Não foi possível conectar ao banco de dados.")
        return False
    
    carId = validateCarId()
    carPrice = generateCarPrice(
        category=car_data[4],
        brand=car_data[5],
        fuel_type=car_data[3],
        transmission=car_data[6],
        year=car_data[1]
    )

    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO cars (id,model, year, license_plate, fuel_type, category, brand, transmission, price_per_day)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (carId, *car_data, carPrice))

        conn.commit()
        conn.close()

        messagebox.showinfo("Sucesso", "Carro adicionado com sucesso.")
        return True
    except sqlite3.IntegrityError as e:
        messagebox.showerror("Erro", f"Não foi possível inserir os valores na tabela: {e}")
        return False
    except sqlite3.OperationalError as e:
        messagebox.showerror(f"Erro operacional: {e}")
        return False
    except Exception as e:
        messagebox.showerror(f"Erro inesperado: {e}")
        return False
    finally:
        conn.close()


def search_cars(filters=None):
    conn = connect_db()
    if conn is None:
        return False
    
    cursor = conn.cursor()
    query = "SELECT * FROM cars WHERE 1=1"
    params = []

    if not filters:
        filters = {}

    category = filters.get('category')
    brand = filters.get('brand')
    max_price_raw = filters.get('max_price')
    year = filters.get('year')

    # Categoria
    if category and category != "Todas as categorias":
        query += " AND category = ?"
        params.append(category)

    # Marca
    if brand and brand != "Todas as marcas":
        query += " AND brand = ?"
        params.append(brand)

    # Preço máximo
    max_price = parse_price_filter(max_price_raw)
    if max_price is not None and max_price != "Sem limite":
        query += " AND price_per_day <= ?"
        params.append(max_price)

    # Ano
    if year and year != "Todos os anos":
        query += " AND year = ?"
        params.append(int(year))

    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()
    return results


def get_car_by_id(carId):
    conn = connect_db()
    if conn is None:
        messagebox.showerror("Erro", "Não foi possível conectar ao banco de dados.")
        return False
    
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cars WHERE id = ?", (carId,))
        car = cursor.fetchone()

        return car
    except sqlite3.OperationalError as e:
        messagebox.showerror(f"Erro operacional: {e}")
        return False
    finally:
        conn.close()
    
    
def update_car(car_id, data):
    conn = connect_db()
    if conn is None:
        messagebox.showerror("Erro", "Não foi possível conectar ao banco de dados.")
        return False
    
    carPrice = generateCarPrice(
        category=data[4],
        brand=data[5],
        fuel_type=data[3],
        transmission=data[6],
        year=data[1]
    )
        
    try:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE cars SET model = ?, year = ?, license_plate = ?, fuel_type = ?, category = ?, brand = ?, transmission = ?, price_per_day = ?
            WHERE id = ? ''', (*data, carPrice, car_id ))
        conn.commit()
        messagebox.showinfo("Sucesso", "Carro atualizado com sucesso.")
    except sqlite3.OperationalError as e:
        messagebox.showerror(f"Erro operacional: {e}")
        return False

def delete_car(carId):
    conn = connect_db()
    if conn is None:
        messagebox.showerror("Erro", "Não foi possível conectar ao banco de dados.")
        return False
    
    try:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM cars WHERE id = ?', (carId,))
        conn.commit()

        messagebox.showinfo("Sucesso", "Carro excluído com sucesso.")
    except sqlite3.OperationalError as e:
        messagebox.showerror(f"Erro operacional: {e}")
        return False
    except Exception as e:
        messagebox.showerror(f"Erro inesperado: {e}")
        return False
    finally:
        conn.close()
