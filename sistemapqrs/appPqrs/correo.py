import yagmail
import threading
import traceback
import tempfile
from decouple import config

def enviar_correo_asincrono(correo_destino, asunto, mensaje):
    def enviar(correo_destino, asunto, mensaje):
        try:
            html_mensaje = f"""
            <!DOCTYPE html>
            <html>
              <body>
                <p>Hola</p>
                <p>{mensaje}</p>
                <p>Saludos,</p>
                <p><b>Mi App Darwin Gomez </b></p>
              </body>
            </html>
            """
            with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False, encoding='utf-8') as temp_html:
                temp_html.write(html_mensaje)
                temp_html_path = temp_html.name
            yag = yagmail.SMTP(
                user=config('EMAIL_USER'),
                password=config('EMAIL_PASSWORD'))
            yag.send(
                to=correo_destino,
                subject=asunto,
                contents=[yagmail.inline(temp_html_path)])
            print("Correo enviado exitosamente.")
        except Exception as e:
            print("Error al enviar el correo:",e)
            traceback.print_exc()
    hilo = threading.Thread(target=enviar, args=(correo_destino, asunto, mensaje))
    hilo.start()