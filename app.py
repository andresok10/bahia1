from flask import Flask
from flask_wtf.csrf import CSRFProtect   #from flask_wtf import FlaskForm,CSRFProtect  # pip install Flask-WTF
from modelo1 import *
from fun_inicio import app_blueprint as a
from fun_categorias import app_blueprint as b
from fun_productos import app_blueprint as c
from fun_usuarios import app_blueprint as d
app = Flask(__name__)
app.secret_key="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
#app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql+psycopg2://postgres:123456@localhost:5432/test'
#engine=create_engine('postgresql://ok:7qF6RmXo5vKNJ4QzWOQDD4NyPGigclw9@dpg-cpgajvmct0pc73dag83g-a:5432/db1_dhy6')

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://ok:b5Dko0Kgdnn3L7Oj6Qpl05Lz0rTopmSc@dpg-cphs6eq1hbls73b8isk0-a:5432/db1_oi4n"
#app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/bahia3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
csrf = CSRFProtect(app)

app.register_blueprint(a)
app.register_blueprint(b)
app.register_blueprint(c)
app.register_blueprint(d)

app.app_context().push()
db.create_all()

try:
    db.session.add_all(consultas)
    db.session.commit()
    db.session.close()
except:
    pass

if __name__ == '__main__':
    #csrf = CSRFProtect(app)
    app.run(host='0.0.0.0', debug=True)
    #app.run(debug=True)
#ImportError: cannot import name 'app_blueprint1' from partially initialized module 'fun_inicio' (most likely due to a circular import) 
#<a href="/perfil">
#    {{ session['nombre'] }}
#    <!--<img style="width:50px;height:30px;" src="{{url_for('static',filename='images/logos-iconos/perfil1.jpg')}}">-->
#</a>

#@media screen and (min-width:800px) {
#            .titulo{font-size: 18px;justify-content: flex-end}
#            .parrafo_publicidad1 p{font-size:16px;}
#            .cont_nav a{margin: 0px 4px;}
#            .caja_galeria{margin: 0px 4px;}
#            .img_galeriaxxx{width:100%;}
#            h3{display: none;}
#        }