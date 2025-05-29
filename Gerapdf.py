import pyodbc
from fpdf import FPDF

server = ""
database = ""
username = ""
password = ""

cnxn = pyodbc.connect(
    "DRIVER={SQL Server};SERVER="
    + server
    + ";DATABASE="
    + database
    + ";ENCRYPT=no;UID="
    + username
    + ";PWD="
    + password
)
print("Conexão Bem Sucedida")

cursor = cnxn.cursor()
cursor.execute(f"SELECT COLUMN_NAME FROM information_schema.columns WHERE table_name = 'CAP_REPORT'")
columns= cursor.fetchall()


pdf=FPDF(orientation='L',unit='pt',format='A4')
pdf.add_page()

for column in columns:
    pdf.set_font(family='Times', size=7)
    if columns[0] == "'Row#',":
        pdf.cell(w=20,h=20,txt=column[0])
    else:
        pdf.cell(w=40,h=20,txt=column[0])
pdf.ln()

cursor.execute("Select * FROM [EVO_SA_PRD_2018].[dbo].[CAP_REPORT_EVO]")
rows=cursor.fetchall()

for row in rows:
    for element in row:
         pdf.set_font(family='Times', size=7)
         pdf.cell(w=40,h=20,txt=str(element))
    pdf.ln()
pdf.output('CAP.pdf')

