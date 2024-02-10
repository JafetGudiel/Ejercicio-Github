import smtplib

message = "Mensaje desde python"
subject = "Prueba de correo"

message = "Subject: {}\n\n{}".format(subject, message)


server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("marvinjafetgudiellopez@gmail.com", "Zelda ocarina")
server.sendmail("marvinjafetgudiellopez@gmail.com",
                "marvingudiellopez2004@gmail.com", message)

server.quit()
print("correo enviado con exito")
