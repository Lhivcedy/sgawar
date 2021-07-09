CREATE TABLE categoria_productos (
    id INT PRIMARY KEY,
    nombre_categoria VARCHAR(100)
)  ENGINE=INNODB;


CREATE TABLE productos (
    id INT PRIMARY KEY,
    sku VARCHAR(15) NOT NULL UNIQUE,
    nombre VARCHAR(100) NOT NULL,
    url_imagen VARCHAR(1000) NOT NULL,
    id_categoria INT NOT NULL,
    valor_venta INT NOT NULL,
    valor_arriendo INT NOT NULL,
    estado int not null,
    FOREIGN KEY (id_categoria)
        REFERENCES categoria_productos (id)
)  ENGINE=INNODB;

CREATE TABLE medios_pago (
    id INT NOT NULL PRIMARY KEY,
    nombre_medio_pago VARCHAR(400) NOT NULL
)  ENGINE=INNODB;

CREATE TABLE arriendos (
    id INT PRIMARY KEY,
    usuario VARCHAR(50) NOT NULL,
    id_medio_pago INT NOT NULL,
    fecha_arriendo DATE NOT NULL,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE NOT NULL,
    fecha_devolucion DATE NOT NULL,
    FOREIGN KEY (usuario)
        REFERENCES users (nombre_usuario),
    FOREIGN KEY (id_medio_pago)
        REFERENCES medios_pago (id)
)  ENGINE=INNODB;

CREATE TABLE arriendos_detalle (
    id INT PRIMARY KEY,
    id_arriendo int not null,
    id_producto INT NOT NULL,
    precio_arriendo INT NOT NULL,
    valor_garantia INT NOT NULL,
    valor_multa_dia int not null,
    foreign key (id_arriendo) references arriendos (id),
    foreign key (id_producto) references productos (id)
)  ENGINE=INNODB;


drop table arriendos_detalle;
drop table arriendos;
