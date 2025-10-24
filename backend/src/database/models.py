from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Cria o engine e a base
engine = create_engine('sqlite:///database.db', echo=True) # engine especifica o tipo de banco de dados e sua localização
Base = declarative_base()

# Modelo Challenge
class Challenge(Base):
    __tablename__ = 'Challenges'

    id = Column(Integer, primary_key=True)
    difficulty = Column(String, nullable=False)
    date_created = Column(DateTime, default=datetime.now)
    created_by = Column(String, nullable=False)
    title = Column(String, nullable=False)
    options = Column(String, nullable=False)  # Armazena as opções como uma string separada por vírgulas
    correct_answer_id = Column(Integer, nullable=False)
    explanation = Column(String, nullable=False)

# Modelo ChallengeQuota (fora da classe anterior!)
class ChallengeQuota(Base):
    __tablename__ = 'ChallengeQuotas'

    id = Column(Integer, primary_key=True)
    user_id = Column(String, nullable=False, unique=True)
    quota_remaining = Column(Integer, nullable=False, default=50)
    last_reset_date = Column(DateTime, default=datetime.now)

# Cria as tabelas no banco de dados
Base.metadata.create_all(engine)

# Cria a sessão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Função para gerenciar sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
