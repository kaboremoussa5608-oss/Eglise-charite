from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return """
        <html>
            <head>
                    <title>ÉGLISE PENTECÔTE DE LA CHARITÉ</title>
                            <meta charset="UTF-8">
                                </head>
                                    <body style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; text-align: center; padding: 0; margin: 0; background-color: #f4f7f6;">

                                                    <div style="background-color: #2c3e50; color: white; padding: 40px 20px;">
                                                                <h1 style="margin: 0; font-size: 2em;">ÉGLISE PENTECÔTE DE LA CHARITÉ INTERNATIONALE</h1>
                                                                            <p style="font-style: italic; margin-top: 10px;">"La Charité qui unit les nations"</p>
                                                                                    </div>

                                                                                            <div style="max-width: 800px; margin: 30px auto; background: white; padding: 20px; border-radius: 10px; shadow: 0 4px 6px rgba(0,0,0,0.1);">
                                                                                                        <h2 style="color: #e67e22; border-bottom: 2px solid #e67e22; display: inline-block; padding-bottom: 5px;">📅 Nos Rendez-vous</h2>
                                                                                                                    <p style="font-size: 1.1em;"><b>Grand Culte :</b> Tous les dimanches à 09h00</p>
                                                                                                                                <p style="font-size: 1.1em;"><b>Intercession :</b> Mercredi à 18h30</p>
                                                                                                                                            <p style="font-size: 1.1em;"><b>Réunion de Jeunesse :</b> Samedi à 16h00</p>

                                                                                                                                                                    <h2 style="color: #e67e22; border-bottom: 2px solid #e67e22; display: inline-block; padding-bottom: 5px; margin-top: 30px;">📢 Annonces</h2>
                                                                                                                                                                                <div style="background-color: #fff3e0; padding: 15px; border-radius: 5px; border-left: 5px solid #ff9800;">
                                                                                                                                                                                                <p>Bienvenue à tous nos nouveaux membres ! N'hésitez pas à vous rapprocher du secrétariat pour toute information.</p>
                                                                                                                                                                                                            </div>
                                                                                                                                                                                                                    </div>

                                                                                                                                                                                                                            <footer style="margin-top: 50px; padding: 20px; color: #7f8c8d; font-size: 0.9em;">
                                                                                                                                                                                                                                        © 2026 - Département Communication de l'Église <br>
                                                                                                                                                                                                                                                    Développé par Moussa Kaboré
                                                                                                                                                                                                                                                            </footer>
                                                                                                                                                                                                                                                                </body>
                                                                                                                                                                                                                                                                    </html>
                                                                                                                                                                                                                                                                        """

if __name__ == "__main__":
    app.run(debug=True)
                                                                                                                                                                                                                                                                            
