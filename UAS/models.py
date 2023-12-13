from sqlalchemy import Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class laptop(Base):
    __tablename__ = 'laptop'
    id_laptop: Mapped[str] = mapped_column(primary_key=True)
    harga: Mapped[int] = mapped_column()
    ram: Mapped[int] = mapped_column()
    kapasitas_baterai: Mapped[int] = mapped_column()
    processor: Mapped[int] = mapped_column()
    penyimpanan_internal: Mapped[float] = mapped_column(type_=Float)  
    
    def __repr__(self) -> str:
        return f"Laptop(id_laptop={self.id_ponsel!r}, harga={self.harga!r})"
