from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey,Column,String,Integer,CHAR,Numeric,Float,Boolean,DECIMAL,DateTime,Text
db = SQLAlchemy()
############################################################
class cat(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), nullable=False)
    catid = Column(Integer, ForeignKey('subcat.id'))

class subcat(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), nullable=False)
    #img1 = Column(String(50))
    catid = Column(Integer)
    rel1 = db.relationship('cat', backref='subcat')

##########################################################
class articulos(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(30), nullable=False)  #, unique=True
    precio = Column(Float, default=0)
    info = Column(String(20))                           
    img1 = Column(String(50))
    stock = Column(Integer, default=1)
    subcatid = Column(Integer, ForeignKey('subcat.id'))
    rel2 = db.relationship("subcat", backref='articulos') #rel_cat = db.relationship('sub_cat', foreign_keys=[catid], backref='articulos')

    #re_fact = db.relationship("car_factura", back_populates="re_articulo")
    #def __repr__(self):
    #    return self.nombre
    #con back_populates 
    #relacion2 = db.relationship("sub_cat", back_populates="relacion1")

###########################################################
class usuarios(db.Model):
    id = Column(Integer,autoincrement=True, primary_key=True)
    nombre = Column(String(30), nullable=False)
    usuario = Column(String(30), nullable=False, unique=True) #,unique=True
    password = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False)
    admin = Column(Boolean, default=False)
    #fecha = Column(DateTime, default=datetime.now)
    #fecha = Column(DateTime, default=datetime.today)

class Pedido(db.Model):
    id = Column(Integer, primary_key=True)
    #usuario_id = Column(Integer)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))  # Cambiar el nombre de la columna y la referencia a la tabla de usuarios
    #fecha = db.Column(db.DateTime, default=datetime.now)
    total = Column(Float)
    detalles = db.relationship('DetallePedido', backref='pedido', lazy=True)

class DetallePedido(db.Model):
    id = Column(Integer, primary_key=True)
    producto_id = Column(Integer)
    cantidad = Column(Integer)
    precio = Column(Float)
    pedido_id = Column(Integer, ForeignKey('pedido.id'))

try:
    consultas=[
    usuarios(nombre="dave1x",usuario="dave1",password="qqww",email="ok1@gmail.com",admin=True),
    usuarios(nombre="dave2x",usuario="dave2",password="aass",email="ok2@gmail.com",admin=False),

    cat(nombre="Mujer", catid=1),
    cat(nombre="Hombre", catid=2),
    cat(nombre="Niño", catid=3),
    cat(nombre="Niña", catid=4),

    subcat(nombre="blusas", catid=1),
    subcat(nombre="Faldas/vestidos", catid=1),
    subcat(nombre="calzado-damas", catid=1),
    subcat(nombre="accesorio", catid=1),

    subcat(nombre="camisas/camisetas", catid=2),
    subcat(nombre="Pantalones", catid=2),
    subcat(nombre="calzado-caballeros", catid=2),
    subcat(nombre="accesorio", catid=2),

    subcat(nombre="blusas", catid=3),
    subcat(nombre="Faldas/vestidos", catid=3),
    subcat(nombre="calzado-niña", catid=3),
    subcat(nombre="accesorio-niña", catid=3),

    subcat(nombre="camisa/camisetas", catid=4),
    subcat(nombre="Pantalones", catid=4),
    subcat(nombre="calzado-niño", catid=4),
    subcat(nombre="accesorio-niño", catid=4),

    # mujer
    articulos(img1="blusa1.webp", nombre="ok1",precio=10.22, info="xxx",stock=2,subcatid=1),
    articulos(img1="blusa2.webp", nombre="ok2",precio=20.22, info="xxx",stock=3,subcatid=1),
    articulos(img1="chaqueta1.webp", nombre="ok3",precio=30.22, info="xxx",stock=5,subcatid=1),
    articulos(img1="chaqueta-casual1.jpg", nombre="ok4",precio=40.22, info="xxx",stock=5,subcatid=1),

    articulos(img1="falda1.jpg",nombre="ok5",precio=10.22, info="xxx",stock=5,subcatid=2),
    articulos(img1="falda2.jpg",nombre="ok6",precio=20.22, info="xxx",stock=5,subcatid=2),
    articulos(img1="vestido1.jpg",nombre="ok7",precio=30.22, info="xxx",stock=5,subcatid=2),
    articulos(img1="vestido2.jpg",nombre="ok8",precio=40.22, info="xxx",stock=5,subcatid=2),

    articulos(img1="zapato1.webp",nombre="ok9",precio=10.22, info="xxx",stock=9,subcatid=3),
    articulos(img1="zapato6.jpg",nombre="ok10",precio=20.22, info="xxx",stock=10,subcatid=3),
    articulos(img1="zapato11.jpg",nombre="ok11",precio=30.22, info="xxx",stock=11,subcatid=3),
    articulos(img1="zapato2.webp",nombre="ok12",precio=40.22, info="xxx",stock=12,subcatid=3),

    articulos(img1="cartera1.png",nombre="ok13",precio=10.22, info="xxx",stock=13,subcatid=4),
    articulos(img1="cartera2.jpg",nombre="ok14",precio=20.22, info="xxx",stock=14,subcatid=4),
    articulos(img1="gafa1.webp",nombre="ok15",precio=30.22, info="xxx",stock=15,subcatid=4),
    articulos(img1="gafa2.webp",nombre="ok16",precio=40.22, info="xxx",stock=16,subcatid=4),
    # hombre
    articulos(img1="camisa1.jpg",nombre="ok17",precio=10.22, info="xxx",stock=1,subcatid=5),
    articulos(img1="camisa2.webp",nombre="ok18",precio=20.22, info="xxx",stock=2,subcatid=5),
    articulos(img1="camisa3.webp",nombre="ok19",precio=30.22, info="xxx",stock=3,subcatid=5),
    articulos(img1="camisa4.webp",nombre="ok20",precio=40.22, info="xxx",stock=4,subcatid=5),

    articulos(img1="pantalon1.webp",nombre="ok21",precio=10.22, info="xxx",stock=5,subcatid=6), 
    articulos(img1="pantalon2.jpeg",nombre="ok22",precio=20.22, info="xxx",stock=6,subcatid=6),
    articulos(img1="pantalon3.jpg",nombre="ok23",precio=30.22, info="xxx",stock=7,subcatid=6),
    articulos(img1="pantalon4.webp",nombre="ok24",precio=40.22, info="xxx",stock=8,subcatid=6),

    articulos(img1="zapato1.jpg",nombre="ok25",precio=10.22, info="xxx",stock=9,subcatid=7),
    articulos(img1="zapato2.webp",nombre="ok26",precio=20.22, info="xxx",stock=10,subcatid=7),
    articulos(img1="zapato3.webp",nombre="ok27",precio=30.22, info="xxx",stock=11,subcatid=7),
    articulos(img1="zapato4.jpeg",nombre="ok28",precio=40.22, info="xxx",stock=12,subcatid=7),

    articulos(img1="gafa1.jpg",nombre="ok29",precio=10.22, info="xxx",stock=13,subcatid=8),
    articulos(img1="gafa1.jpg",nombre="ok30",precio=20.22, info="xxx",stock=14,subcatid=8),
    articulos(img1="gorra1.jpg",nombre="ok31",precio=30.22, info="xxx",stock=15,subcatid=8),
    articulos(img1="gorra1.jpg",nombre="ok32",precio=40.22, info="xxx",stock=16,subcatid=8),
    # niños
    articulos(img1="camisa1.webp",nombre="ok33",precio=10.22, info="xxx",stock=1,subcatid=9),
    articulos(img1="camisa2.jpg",nombre="ok34",precio=20.22, info="xxx",stock=2,subcatid=9),
    articulos(img1="camisa3.webp",nombre="ok35",precio=30.22, info="xxx",stock=3,subcatid=9),
    articulos(img1="camisa4.jpg",nombre="ok36",precio=40.22, info="xxx",stock=4,subcatid=9),

    articulos(img1="pantalon1.webp",nombre="ok37",precio=10.22, info="xxx",stock=5,subcatid=10), 
    articulos(img1="pantalon2.jpg",nombre="ok38",precio=20.22, info="xxx",stock=6,subcatid=10),
    articulos(img1="pantalon3.jpg",nombre="ok39",precio=30.22, info="xxx",stock=7,subcatid=10),
    articulos(img1="pantalon4.jpg",nombre="ok40",precio=40.22, info="xxx",stock=8,subcatid=10),

    articulos(img1="zapato1.jpg",nombre="ok41",precio=10.22, info="xxx",stock=1,subcatid=11),
    articulos(img1="zapato2.webp",nombre="ok42",precio=20.22, info="xxx",stock=1,subcatid=11),
    articulos(img1="zapato3.webp",nombre="ok43",precio=30.22, info="xxx",stock=1,subcatid=11),
    articulos(img1="zapato4.jpg",nombre="ok44",precio=40.22, info="xxx",stock=1,subcatid=11),

    articulos(img1="gorra1.jpg",nombre="ok45",precio=10.22, info="xxx",stock=1,subcatid=12),
    articulos(img1="gorra2.jpg",nombre="ok46",precio=20.22, info="xxx",stock=1,subcatid=12),
    articulos(img1="gorra3.jpg",nombre="ok47",precio=30.22, info="xxx",stock=1,subcatid=12),
    articulos(img1="gorra4.jpg",nombre="ok48",precio=40.22, info="xxx",stock=1,subcatid=12),
    # niñas
    articulos(img1="blusa1.png",nombre="ok49",precio=10.22, info="xxx",stock=1,subcatid=13),
    articulos(img1="blusa2.jpg",nombre="ok50",precio=20.22, info="xxx",stock=1,subcatid=13),
    articulos(img1="blusa3.png",nombre="ok51",precio=30.22, info="xxx",stock=1,subcatid=13),
    articulos(img1="blusa4.webp",nombre="ok52",precio=40.22, info="xxx",stock=1,subcatid=13),

    articulos(img1="pantalon1.webp",nombre="ok53",precio=10.22, info="xxx",stock=1,subcatid=14), 
    articulos(img1="pantalon2.webp",nombre="ok54",precio=20.22, info="xxx",stock=1,subcatid=14),
    articulos(img1="pantalon3.webp",nombre="ok55",precio=30.22, info="xxx",stock=1,subcatid=14),
    articulos(img1="vestido1.webp",nombre="ok56",precio=40.22, info="xxx",stock=1,subcatid=14),

    articulos(img1="zapato1.jpg",nombre="ok57",precio=10.22, info="xxx",stock=1,subcatid=15),
    articulos(img1="zapato2.webp",nombre="ok58",precio=20.22, info="xxx",stock=1,subcatid=15),
    articulos(img1="zapato3.webp",nombre="ok59",precio=30.22, info="xxx",stock=1,subcatid=15),
    articulos(img1="zapato4.jpg",nombre="ok60",precio=40.22, info="xxx",stock=1,subcatid=15),

    articulos(img1="gafa2.jpeg",nombre="ok61",precio=10.22, info="xxx",stock=1,subcatid=16),
    articulos(img1="gafa4.jpg",nombre="ok62",precio=20.22, info="xxx",stock=1,subcatid=16),
    articulos(img1="gafa5.jpg",nombre="ok63",precio=30.22, info="xxx",stock=1,subcatid=16),
    articulos(img1="gorra1.jpg",nombre="ok64",precio=40.22, info="xxx",stock=1,subcatid=16)
    ]
    #db.session.add_all(consultas)
    #db.session.commit()
    #db.session.close()
except:
    pass