from app import db
from app.models import UnidadeDeSaude  # ajuste aqui se tiver mais modelos

db.create_all()
print("Tabelas criadas com sucesso.")
