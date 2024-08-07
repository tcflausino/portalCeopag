import mysql.connector
from mysql.connector import Error

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="",
            user="",
            password="",
            database=""
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
        for customer in customers:
            cursor.execute(insert_query, customer)
            print(f"Inserido: {customer}")  # Mensagem de depuração para cada linha inserida
        connection.commit()
        print("Dados dos clientes inseridos com sucesso!")
    except Error as e:
        print(f"Erro ao inserir dados: {e}")
        connection.rollback()
    finally:
        cursor.close()
        connection.close()

def generate_fictitious_data():
    # Gerar dados fictícios para testes
    return [
        {
            'data': '2024-08-06',
            'cnpj': '12345678000195',
            'razaosocial': 'Empresa Fictícia Ltda',
            'fantasia': 'Fictícia',
            'uf': 'SP',
            'cidade': 'São Paulo',
            'endereco': 'Rua Fictícia',
            'num': '456',
            'complemento': 'Sala 202',
            'bairro': 'Bairro Fictício',
            'cep': '06543210',
            'telefone': '11987654321',
            'tipoantecipacao': 'Fictício Tipo',
            'segmentoagl': 'SEG',
            'pctantecipa': 10.00,
            'status': 1,
            'franqueado': 1,
            'parceiro': 2,
            'vendedor': 3,
            'faixa': 4,
            'classificacao': 'ECO',
            'email': 'contato@ficticia.com',
            'caf': 'CAF456',
            'adquirente': 2,
            'idpagseguro': 'PS456',
            'segmento': 2,
            'fatestimado': 200000,
            'tipoconta': 2,
            'banco': '002',
            'agencia': '5678',
            'conta': '123456',
            'codigoestoque': 'EST456',
            'contadigital': 'DGT',
            'aluguelpos': 'POS',
            'valoraluguel': 750.00,
            'formapagtoaluguel': 'Transferência',
            'datainialuguel': '2024-08-01',
            'justificativa': 'Justificativa Fictícia',
            'obs': 'Observações Fictícias',
            'anexo1': 'ficticio1.pdf',
            'anexo2': 'ficticio2.pdf',
            'idrede': 2,
            'modeloliquidacao': 'Modelo2',
            'modeloganho': 'ModeloGanho2',
            'aquisicaopos': 'Aquisição2',
            'contatobxfat': 'CX'
        },
        # Adicione mais dados fictícios conforme necessário
    ]

if __name__ == "__main__":
    fictitious_data = generate_fictitious_data()
    insert_customer_data(fictitious_data)
