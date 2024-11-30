# Veri tabanı bağlantısı
engine = create_engine('sqlite:///highschool.db')
Base.metadata.create_all(engine)

# Oturum başlatma
Session = sessionmaker(bind=engine)
session = Session()
