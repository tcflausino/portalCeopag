import pandas as pd
import mysql.connector
from mysql.connector import Error

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="162.215.129.240",
            user="wwceop_portal",
            password="Ce@pag23*",
            database="wwceop_portal"
        )
        if connection.is_connected():
            print("Conectado ao banco de dados")
            return connection
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

def insert_customer_data(customers):
    connection = connect_to_database()
    if connection is None:
        return

    cursor = connection.cursor()

    insert_query = """
    INSERT INTO ec (
        data, cnpj, razaosocial, fantasia, uf, cidade, endereco, num, complemento, bairro, cep, telefone, tipoantecipacao,
        segmentoagl, pctantecipa, status, franqueado, parceiro, vendedor, faixa, classificacao, email, caf, adquirente, idpagseguro,
        segmento, fatestimado, tipoconta, banco, agencia, conta, codigoestoque, contadigital, aluguelpos, valoraluguel,
        formapagtoaluguel, datainialuguel, justificativa, obs, anexo1, anexo2, idrede, modeloliquidacao, modeloganho,
        aquisicaopos, contatobxfat
    ) VALUES (
        %(data)s, %(cnpj)s, %(razaosocial)s, %(fantasia)s, %(uf)s, %(cidade)s, %(endereco)s, %(num)s, %(complemento)s, %(bairro)s, %(cep)s, %(telefone)s,
        %(tipoantecipacao)s, %(segmentoagl)s, %(pctantecipa)s, %(status)s, %(franqueado)s, %(parceiro)s, %(vendedor)s, %(faixa)s,
        %(classificacao)s, %(email)s, %(caf)s, %(adquirente)s, %(idpagseguro)s, %(segmento)s, %(fatestimado)s, %(tipoconta)s, %(banco)s,
        %(agencia)s, %(conta)s, %(codigoestoque)s, %(contadigital)s, %(aluguelpos)s, %(valoraluguel)s, %(formapagtoaluguel)s,
        %(datainialuguel)s, %(justificativa)s, %(obs)s, %(anexo1)s, %(anexo2)s, %(idrede)s, %(modeloliquidacao)s, %(modeloganho)s,
        %(aquisicaopos)s, %(contatobxfat)s
    )
    """

    try:
        for _, row in customers.iterrows():
            cursor.execute(insert_query, row.to_dict())
            print(f"Inserido: {row.to_dict()}")  
        connection.commit()
        print("Dados dos clientes inseridos com sucesso!")
    except Error as e:
        print(f"Erro ao inserir dados: {e}")
        connection.rollback()
    finally:
        cursor.close()
        connection.close()

def read_excel(file_path):
    data = pd.read_excel(file_path)
    return data

if __name__ == "__main__":
    excel_file_path = 'teste.xlsx'
    customer_data = read_excel(excel_file_path)
    insert_customer_data(customer_data)
