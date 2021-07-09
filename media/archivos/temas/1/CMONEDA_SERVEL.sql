CREATE TABLE region (
    id_region       NUMBER PRIMARY KEY,
    nombre_region   VARCHAR(150) NOT NULL
);

CREATE TABLE distrito (
    id_distrito       NUMBER PRIMARY KEY,
    nombre_distrito   VARCHAR(10) NOT NULL,
    id_region         NUMBER NOT NULL,
    FOREIGN KEY ( id_region )
        REFERENCES region ( id_region )
);

CREATE TABLE comuna (
    id_comuna       NUMBER PRIMARY KEY,
    nombre_comuna   VARCHAR2(100) NOT NULL,
    id_distrito NOT NULL,
    FOREIGN KEY ( id_junta_electoral )
        REFERENCES distrito ( id_distrito )
);

CREATE TABLE circ_electoral (
    id_circ_electoral       NUMBER PRIMARY KEY,
    nombre_circ_electoral   VARCHAR2(100) NOT NULL,
    id_comuna               NUMBER NOT NULL,
    FOREIGN KEY ( id_comuna )
        REFERENCES comuna ( id_comuna )
);

CREATE TABLE proveedor (
    id_proveedor       NUMBER PRIMARY KEY,
    nombre_proveedor   VARCHAR2(150) NOT NULL
);

CREATE TABLE proceso (
    id_proceso       NUMBER PRIMARY KEY,
    nombre_proceso   VARCHAR(150) NOT NULL,
    serie            VARCHAR2(10) NOT NULL,
    estado           NUMBER DEFAULT 0
);

CREATE TABLE tipo_voto (
    id_tipo_voto       NUMBER PRIMARY KEY,
    nombre_tipo_voto   VARCHAR(150) NOT NULL,
    descripcion        VARCHAR(100) NOT NULL,
    color              VARCHAR(100) NOT NULL
);

CREATE TABLE votos (
    id_voto             NUMBER PRIMARY KEY,
    id_proceso          NUMBER NOT NULL,
    id_proveedor        NUMBER NOT NULL,
    id_tipo_voto        NUMBER NOT NULL,
    id_circ_electoral   NUMBER NOT NULL,
    mesa                VARCHAR2(50) NOT NULL,
    serie               VARCHAR2(10) NOT NULL,
    electores           NUMBER DEFAULT 0,
    desde               NUMBER NOT NULL,
    hasta               NUMBER NOT NULL,
    barra_fajo          VARCHAR2(50) NOT NULL UNIQUE,
    tipo_cedula         VARCHAR2(10) NOT NULL,
    fajos_x_caja        NUMBER NOT NULL,
    barra_caja          VARCHAR2(50) NOT NULL UNIQUE,
    numero_fajo         VARCHAR2(100) NOT NULL,
    rango_caja          VARCHAR2(10) NOT NULL,
    voto_x_fajo         NUMBER NOT NULL,
    etnia               VARCHAR2(50) DEFAULT 'NO INDIGENA',
    corr_fajo           NUMBER DEFAULT - 1,
    FOREIGN KEY ( id_proceso )
        REFERENCES proceso ( id_proceso ),
    FOREIGN KEY ( id_proveedor )
        REFERENCES proveedor ( id_proveedor ),
    FOREIGN KEY ( id_tipo_voto )
        REFERENCES tipo_voto ( id_tipo_voto ),
    FOREIGN KEY ( id_circ_electoral )
        REFERENCES circ_electoral ( id_circ_electoral )
);

CREATE TABLE usuarios (
    nombre_usuario   VARCHAR2(50) PRIMARY KEY,
    nombre           VARCHAR2(100) NOT NULL,
    salt             VARCHAR2(50) NOT NULL,
    password         VARCHAR2(256) NOT NULL
);

CREATE TABLE db_impresion (
    id_db_impresion   NUMBER PRIMARY KEY,
    fecha             DATE NOT NULL,
    nombre_usuario    VARCHAR2(50) NOT NULL,
    id_tipo_voto      NUMBER NOT NULL,
    FOREIGN KEY ( id_tipo_voto )
        REFERENCES tipo_voto ( id_tipo_voto )
);

CREATE TABLE db_impresion_detalle (
    id_db_impresion_detalle   NUMBER PRIMARY KEY,
    id_db_impresion           NUMBER NOT NULL,
    id_voto                   NUMBER NOT NULL,
    FOREIGN KEY ( id_db_impresion )
        REFERENCES db_impresion ( id_db_impresion ),
    FOREIGN KEY ( id_voto )
        REFERENCES votos ( id_voto )
);

CREATE TABLE db_reposicion (
    id_db_repo   NUMBER PRIMARY KEY,
    fecha             DATE NOT NULL,
    nombre_usuario    VARCHAR2(50) NOT NULL,
    id_tipo_voto      NUMBER NOT NULL,
    comentario        VARCHAR(2500),
    universo          VARCHAR(100) NOT NULL,
    FOREIGN KEY ( id_tipo_voto )
        REFERENCES tipo_voto ( id_tipo_voto )
);

CREATE TABLE db_reposicion_detalle (
    id_db_repo_detalle   NUMBER PRIMARY KEY,
    id_db_repo           NUMBER NOT NULL,
    serie                   NUMBER NOT NULL,
    FOREIGN KEY ( id_db_repo )
        REFERENCES db_reposicion ( id_db_repo )
);

INSERT INTO usuarios VALUES (
    'rjara',
    'Rubén Jara',
    '2635262021040339',
    'c2bd8e8b7637f52f6465dcfe478ee1fb9633620868869bad51e39a2ac3e1895a7fe88e8f0541eb029baced4d2cefc1e0c5289ef5ac7ebefb4659ea9b5209fdb2'
);

COMMIT;