import smtplib,ssl
from email.message import EmailMessage

email=''
emailaut=''
password =''

# Criando a mensagem
msg = EmailMessage()
msg['Subject'] = 'Relatório Contas a Pagar'
msg['From'] = email
msg['To'] = ''
msg.set_content('Relatório Contas a Pagar')

# Adicionando o anexo
with open('C:/TEMP/CAP.pdf', 'rb') as f:
    file_data = f.read()
    file_name = f.name

msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename='CAP.PDF')

# Enviando o email
context = ssl.create_default_context()
with smtplib.SMTP('smtp.office365.com', 587) as smtp:
    smtp.starttls(context=context)
    smtp.login(emailaut, password)
    smtp.send_message(msg)

print('Email enviado com sucesso!')




