from app import db

class Administrador(db.Model):
    __tablename__ = 'Administrador'

    id_administrador = db.Column(db.Integer, primary_key=True)
    email= db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(100), nullable=False)
    nome_barbearia = db.Column(db.String(100), nullable=False)
    


class Funcionarios(db.Model):
    __tablename__ = 'Funcionarios'

    id_funcionario = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    admin_id = db.Column(db.Integer, db.ForeignKey('Administrador.id_administrador'), nullable=False)
    administrador = db.relationship('Administrador', backref='funcionarios')


class Servicos(db.Model):
    __tablename__ = 'Servicos'

    id_servico = db.Column(db.Integer, primary_key=True)
    nome_servico = db.Column(db.String(100), nullable=False)
    valor_servico = db.Column(db.Numeric(10, 2))
    tempo_servico = db.Column(db.Integer)
    admin_id = db.Column(db.Integer, db.ForeignKey('Administrador.id_administrador'), nullable=False)
    administrador = db.relationship('Administrador', backref='servicos')


class Horarios(db.Model):
    __tablename__ = 'Horarios'

    id_horario = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date, nullable=False)
    horario = db.Column(db.Time, nullable=False)
    preenchido = db.Column(db.Boolean, nullable=False, default=False)

    # Ligação com Funcionarios
    id_funcionario = db.Column(
        db.Integer,
        db.ForeignKey('Funcionarios.id_funcionario'),
        nullable=False
    )

    funcionario = db.relationship('Funcionarios', backref='horarios')
    admin_id = db.Column(db.Integer, db.ForeignKey('Administrador.id_administrador'), nullable=False)
    administrador = db.relationship('Administrador', backref='horarios')


class Agendamentos(db.Model):
    __tablename__ = 'Agendamentos'

    id_agendamento = db.Column(db.Integer, primary_key=True)

    # Relacionamento com Horarios
    id_horario = db.Column(
        db.Integer,
        db.ForeignKey('Horarios.id_horario'),
        nullable=False
    )
    horario = db.relationship('Horarios', backref='agendamentos')

    # Relacionamento com Servicos
    id_servico = db.Column(
        db.Integer,
        db.ForeignKey('Servicos.id_servico'),
        nullable=False
    )
    servico = db.relationship('Servicos', backref='agendamentos')

    
    nome_funcionario = db.Column(db.String(100), nullable=False)

    nome_cliente = db.Column(db.String(100), nullable=False)
    telefone_cliente = db.Column(db.String(20), nullable=False)
    admin_id = db.Column(db.Integer, db.ForeignKey('Administrador.id_administrador'), nullable=False)
    administrador = db.relationship('Administrador', backref='agendamentos')
