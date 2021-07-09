--Joselyn Pino Entrega 1
---creacion de usuario
--CREATE USER proyecto_bd2021 IDENTIFIED BY 123;

-- SE OTORGAN TODOS LOS PRIVILEGIOS AL USUARIO
--GRANT ALL PRIVILEGES TO proyecto_bd2021;

--creacion de tablas solo 5 son con incremento que serian las que tienen más información.

--Joselyn Pino 013v

--Proyecto bd part 1

--SENTENCIA
/*CREATE SEQUENCE SEQ_CONTACT INCREMENT BY 1 START WITH 1 MAXVALUE 999999999999 MINVALUE 1;

CREATE SEQUENCE SEQ_CV INCREMENT BY 1 START WITH 1 MAXVALUE 999999999999 MINVALUE 1;
CREATE SEQUENCE SEQ_POSTULANTE INCREMENT BY 1 START WITH 1 MAXVALUE 999999999999 MINVALUE 1;

CREATE SEQUENCE SEQ_REQ_FORMACION_ACA INCREMENT BY 1 START WITH 1 MAXVALUE 999999999999 MINVALUE 1;
CREATE SEQUENCE SEQ_FORMACION_ACADE INCREMENT BY 1 START WITH 1 MAXVALUE 999999999999 MINVALUE 1;*/

-----drop table
/*DROP TABLE cv_postulante;

DROP TABLE postulante;

DROP TABLE req_formacion_academica;

DROP TABLE formacion_academica;

DROP TABLE dato_contact;

DROP TABLE perfil_acad_prof;

DROP TABLE descr_program_perfect;

DROP TABLE participacion_proyect;

DROP TABLE perfil_acad_prof_bec;

DROP TABLE criterio_ponderacion;

DROP TABLE req_min_postulacion;

DROP TABLE postulacion_beca;

DROP TABLE documentos_obligatorios;

DROP TABLE info_insti_extra;

DROP TABLE informacion_complementaria;

DROP TABLE experiencia_laboral;

DROP TABLE estudios_secundarios;

DROP TABLE grado_academico;

DROP TABLE instituciones_publicas;

DROP TABLE jerarquia_academica;

DROP TABLE linea_investigacion;

DROP TABLE subespecialidad;

DROP TABLE modulo;

DROP TABLE idioma_requerido;

DROP TABLE etapas_postulacion;

DROP TABLE estado_civil;

DROP TABLE nacionalidad;

DROP TABLE estudios_especializacion;

DROP TABLE titulo_profesional;

DROP TABLE tipo_estudio;

DROP TABLE institucion;

DROP TABLE ciudad;

DROP TABLE region;

DROP TABLE pais;*/


-- creacion de tablas
CREATE TABLE pais (
    id_pais   NUMBER(3) NOT NULL,
    nombre    VARCHAR(50) NOT NULL
);

ALTER TABLE pais ADD CONSTRAINT pais_pk PRIMARY KEY ( id_pais );

CREATE TABLE region (
    id_region   NUMBER(3) NOT NULL,
    nombre      VARCHAR(50) NOT NULL,
    id_pais     NUMBER(3) NOT NULL
);

ALTER TABLE region ADD CONSTRAINT region_pk PRIMARY KEY ( id_region );

CREATE TABLE ciudad (
    id_ciudad   NUMBER(3) NOT NULL,
    nombre      VARCHAR(50) NOT NULL,
    id_pais     NUMBER(3) NOT NULL
);

ALTER TABLE ciudad ADD CONSTRAINT ciudad_pk PRIMARY KEY ( id_ciudad );

CREATE TABLE institucion (
    id_institucion   NUMBER(3) NOT NULL,
    nombre           VARCHAR(50) NOT NULL
);

ALTER TABLE institucion ADD CONSTRAINT institucion_pk PRIMARY KEY ( id_institucion );

CREATE TABLE tipo_estudio (
    id_tipo_estudio   NUMBER(3) NOT NULL,
    descripcion       VARCHAR(50) NOT NULL
);

ALTER TABLE tipo_estudio ADD CONSTRAINT tipo_estudio_pk PRIMARY KEY ( id_tipo_estudio );

CREATE TABLE titulo_profesional (
    id_profesional    NUMBER(3) NOT NULL,
    nombre_carrera    VARCHAR(50) NOT NULL,
    fecha_obtencion   DATE NOT NULL,
    id_tipo_estudio   NUMBER(3) NOT NULL,
    id_institucion    NUMBER(3) NOT NULL
);

ALTER TABLE titulo_profesional ADD CONSTRAINT titulo_profesional_pk PRIMARY KEY ( id_profesional );

CREATE TABLE estudios_especializacion (
    id_especializacion   NUMBER(3) NOT NULL,
    nombre_programa      VARCHAR(50) NOT NULL,
    id_institucion       NUMBER(3) NOT NULL,
    id_tipo_estudio      NUMBER(3) NOT NULL
);

ALTER TABLE estudios_especializacion ADD CONSTRAINT estudios_especializacion_pk PRIMARY KEY ( id_especializacion );

CREATE TABLE nacionalidad (
    id_nacionalidad   NUMBER(3) NOT NULL,
    nombre            VARCHAR(50) NOT NULL
);

ALTER TABLE nacionalidad ADD CONSTRAINT nacionalidad_pk PRIMARY KEY ( id_nacionalidad );

CREATE TABLE estado_civil (
    id_estado_civil   NUMBER(3) NOT NULL,
    descripcion       VARCHAR(50) NOT NULL
);

ALTER TABLE estado_civil ADD CONSTRAINT estado_civil PRIMARY KEY ( id_estado_civil );

CREATE TABLE etapas_postulacion (
    id_etapa       NUMBER(3) NOT NULL,
    nombre_etapa   VARCHAR(50) NOT NULL,
    descripcion    VARCHAR(50) NOT NULL
);

ALTER TABLE etapas_postulacion ADD CONSTRAINT etapas_postulacion_pk PRIMARY KEY ( id_etapa );

CREATE TABLE idioma_requerido (
    id_idioma   NUMBER(3) NOT NULL,
    nombre      VARCHAR(50) NOT NULL
);

ALTER TABLE idioma_requerido ADD CONSTRAINT idioma_requerido_pk PRIMARY KEY ( id_idioma );

CREATE TABLE modulo (
    id_modulo       NUMBER(3) NOT NULL,
    nombre_modulo   VARCHAR(50) NOT NULL,
    sub_modulo      VARCHAR(50) NOT NULL
);

ALTER TABLE modulo ADD CONSTRAINT modulo_pk PRIMARY KEY ( id_modulo );

CREATE TABLE subespecialidad (
    id_subespecialidad   NUMBER(3) NOT NULL,
    nombre               VARCHAR(50) NOT NULL
);

ALTER TABLE subespecialidad ADD CONSTRAINT subepecialidad_pk PRIMARY KEY ( id_subespecialidad );

CREATE TABLE linea_investigacion (
    id_linea              NUMBER(3) NOT NULL,
    linea_investigativa   VARCHAR(50) NOT NULL,
    diciplina             VARCHAR(50) NOT NULL
);

ALTER TABLE linea_investigacion ADD CONSTRAINT linea_investigacion_pk PRIMARY KEY ( id_linea );

CREATE TABLE jerarquia_academica (
    id_jerarquia       NUMBER(3) NOT NULL,
    nombre_jerarquia   VARCHAR(50) NOT NULL,
    compromiso         VARCHAR(50) NOT NULL,
    id_institucion     NUMBER(3) NOT NULL
);

ALTER TABLE jerarquia_academica ADD CONSTRAINT jerarquia_academica_pk PRIMARY KEY ( id_jerarquia );

CREATE TABLE instituciones_publicas (
    id_institucion_pub    NUMBER(3) NOT NULL,
    nombre                VARCHAR(50) NOT NULL,
    experiencia_laboral   NUMBER(3) NOT NULL
);

ALTER TABLE instituciones_publicas ADD CONSTRAINT entituciones_publicas_pk PRIMARY KEY ( id_institucion_pub );

CREATE TABLE grado_academico (
    id_grado          NUMBER(3) NOT NULL,
    nombre_programa   VARCHAR(50) NOT NULL,
    ano_obtencion     DATE NOT NULL,
    id_institucion    NUMBER(3) NOT NULL,
    id_tipo_estudio   NUMBER(3) NOT NULL
);

ALTER TABLE grado_academico ADD CONSTRAINT grado_academico_pk PRIMARY KEY ( id_grado );

CREATE TABLE estudios_secundarios (
    id_estudios                  NUMBER(3) NOT NULL,
    dependecia_establecimiento   VARCHAR(50) NOT NULL,
    tipo_establecimiento         VARCHAR(50) NOT NULL,
    id_pais                      NUMBER(3) NOT NULL
);

ALTER TABLE estudios_secundarios ADD CONSTRAINT estudios_secundarios_pk PRIMARY KEY ( id_estudios );

CREATE TABLE experiencia_laboral (
    id_experiencia_lab   NUMBER(3) NOT NULL,
    nombre_              VARCHAR(50) NOT NULL,
    duracion             NUMBER(5) NOT NULL,
    jornada              NUMBER(5) NOT NULL,
    fecha_inicio         DATE NOT NULL,
    fecha_termino        DATE NOT NULL,
    id_institucion_pub   NUMBER(3) NOT NULL
);

ALTER TABLE experiencia_laboral ADD CONSTRAINT experiencia_laboral_pk PRIMARY KEY ( id_experiencia_lab );

CREATE TABLE informacion_complementaria (
    id_complementaria   NUMBER(3) NOT NULL,
    numero_hijos        NUMBER(3) NOT NULL,
    pueblo_originario   CHAR NOT NULL,
    discapacidad        CHAR NOT NULL,
    hijos_hace_5        CHAR NOT NULL
);

ALTER TABLE informacion_complementaria ADD CONSTRAINT informacion_complementaria_pk PRIMARY KEY ( id_complementaria );

CREATE TABLE info_insti_extra (
    id_inst_extra   NUMBER(3) NOT NULL,
    nombre_inst     VARCHAR(50) NOT NULL,
    ranking         NUMBER(5) NOT NULL,
    url_inst        VARCHAR(50) NOT NULL,
    duracion        NUMBER(5) NOT NULL,
    id_pais         NUMBER(3) NOT NULL
);

ALTER TABLE info_insti_extra ADD CONSTRAINT info_insti_extra_pk PRIMARY KEY ( id_inst_extra );

CREATE TABLE documentos_obligatorios (
    id_documentos       NUMBER(3) NOT NULL,
    copia_ced_ident     VARCHAR(50) NOT NULL,
    cert_perma_chilen   VARCHAR(50) NOT NULL,
    notas_pregrado      VARCHAR(50) NOT NULL,
    cert_titulo         VARCHAR(50) NOT NULL,
    cert_idioma         VARCHAR(50) NOT NULL,
    cert_laboral        VARCHAR(50) NOT NULL
);

ALTER TABLE documentos_obligatorios ADD CONSTRAINT documentos_obligatorios_pk PRIMARY KEY ( id_documentos );

CREATE TABLE postulacion_beca (
    id_beca                 NUMBER(3) NOT NULL,
    postulacion_linea       CHAR NOT NULL,
    veracidad_postulacion   CHAR NOT NULL,
    total_antc_obli         CHAR NOT NULL,
    id_documentos           NUMBER(3) NOT NULL
);

ALTER TABLE postulacion_beca ADD CONSTRAINT postulacion_beca_pk PRIMARY KEY ( id_beca );

CREATE TABLE req_min_postulacion (
    id_req_min           NUMBER(3) NOT NULL,
    nacionalidad         CHAR NOT NULL,
    titulo_cirujano      CHAR NOT NULL,
    ejercer_legal_prof   CHAR NOT NULL,
    cert_espec_medica    CHAR NOT NULL,
    exp_min_lab          CHAR NOT NULL
);

ALTER TABLE req_min_postulacion ADD CONSTRAINT req_min_postulacion_pk PRIMARY KEY ( id_req_min );

CREATE TABLE criterio_ponderacion (
    id_criterio            NUMBER(3) NOT NULL,
    criterio               VARCHAR(50) NOT NULL,
    descripcion            VARCHAR(50) NOT NULL,
    ptje_obte              NUMBER(5) NOT NULL,
    subcriterio_variable   VARCHAR(50) NOT NULL
);

ALTER TABLE criterio_ponderacion ADD CONSTRAINT criterio_ponderacion_pk PRIMARY KEY ( id_criterio );

CREATE TABLE perfil_acad_prof_bec (
    id_perfil          NUMBER(3) NOT NULL,
    min_exp_laboral    CHAR NOT NULL,
    req_medicina_int   CHAR NOT NULL,
    req_medicina_gen   CHAR NOT NULL
);

ALTER TABLE perfil_acad_prof_bec ADD CONSTRAINT perfil_acad_prof_bec_pk PRIMARY KEY ( id_perfil );

CREATE TABLE participacion_proyect (
    id_participacion   NUMBER(3) NOT NULL,
    financia_conicyt   CHAR NOT NULL,
    financia_inter     CHAR NOT NULL,
    titulo_conicyt     VARCHAR(50) NOT NULL,
    titulo_otro        VARCHAR(50) NOT NULL
);

ALTER TABLE participacion_proyect ADD CONSTRAINT participacion_proyect_pk PRIMARY KEY ( id_participacion );

CREATE TABLE descr_program_perfect (
    id_descripcion_pr   NUMBER(3) NOT NULL,
    cupo_min            NUMBER(5) NOT NULL,
    cupo_max            NUMBER(5) NOT NULL,
    duracion_programa   NUMBER(5) NOT NULL,
    id_modulo           NUMBER(3) NOT NULL
);

ALTER TABLE descr_program_perfect ADD CONSTRAINT descr_program_perfect_pk PRIMARY KEY ( id_descripcion_pr );

CREATE TABLE perfil_acad_prof (
    id_perfil_acad_pr    NUMBER(3) NOT NULL,
    id_formacion         NUMBER(3) NOT NULL,
    id_experiencia_lab   NUMBER(3) NOT NULL
);

ALTER TABLE perfil_acad_prof ADD CONSTRAINT perfil_acad_prof_pk PRIMARY KEY ( id_perfil_acad_pr );

CREATE TABLE dato_contact (
    id_contacto   NUMBER(3) NOT NULL,
    direccion     VARCHAR(50) NOT NULL,
    numero        NUMBER(10) NOT NULL
);

ALTER TABLE dato_contact ADD CONSTRAINT dato_contact_pk PRIMARY KEY ( id_contacto );

CREATE TABLE formacion_academica (
    id_formacion                 NUMBER(3) NOT NULL,
    nombre_formacion             VARCHAR(50) NOT NULL,
    tipo_ingreso_universitario   VARCHAR(50) NOT NULL,
    id_estudio                   NUMBER(3) NOT NULL,
    id_profesional               NUMBER(3) NOT NULL,
    id_especializacion           NUMBER(3) NOT NULL,
    id_grado                     NUMBER(3) NOT NULL
);

ALTER TABLE formacion_academica ADD CONSTRAINT formacion_academica PRIMARY KEY ( id_formacion );

CREATE TABLE req_formacion_academica (
    id_req_form            NUMBER(3) NOT NULL,
    id_idioma              NUMBER(3) NOT NULL,
    id_formacion           NUMBER(3) NOT NULL,
    id_perfil_acad_pr      NUMBER(3) NOT NULL,
    id_institucion_extra   NUMBER(3) NOT NULL,
    descripcion            VARCHAR(50) NOT NULL,
    id_subespecialidad     NUMBER(3) NOT NULL,
    id_perfil              NUMBER(3) NOT NULL
);

ALTER TABLE req_formacion_academica ADD CONSTRAINT req_formacion_academica_pk PRIMARY KEY ( id_req_form );

CREATE TABLE postulante (
    id_postulante        NUMBER(3) NOT NULL,
    rut                  VARCHAR(50) NOT NULL,
    apell_pat            VARCHAR(50) NOT NULL,
    apell_mat            VARCHAR(50) NOT NULL,
    primer_nombre        VARCHAR(50) NOT NULL,
    segundo_nombre       VARCHAR(50) NOT NULL,
    fecha_nacimiento     DATE NOT NULL,
    sexo                 CHAR NOT NULL,
    pasaporte_visa       VARCHAR(50),
    id_nacionalidad      NUMBER(3) NOT NULL,
    id_formacion         NUMBER(3) NOT NULL,
    id_experiencia_lab   NUMBER(3) NOT NULL,
    id_contacto          NUMBER(3) NOT NULL,
    id_complementaria    NUMBER(3) NOT NULL,
    id_etapa             NUMBER(3) NOT NULL,
    id_ciudad            NUMBER(3) NOT NULL,
    id_req_min           NUMBER(3) NOT NULL,
    id_criterio          NUMBER(3) NOT NULL
);

ALTER TABLE postulante ADD CONSTRAINT postulante_pk PRIMARY KEY ( id_postulante );

CREATE TABLE cv_postulante (
    id_cv                  NUMBER(3) NOT NULL,
    prin_objet_postu       VARCHAR(50) NOT NULL,
    prin_inte_postu        VARCHAR(50) NOT NULL,
    form_aplicar_subespe   VARCHAR(50) NOT NULL,
    id_linea               NUMBER(3) NOT NULL,
    id_jerarquia           NUMBER(3) NOT NULL,
    id_participacion       NUMBER(3) NOT NULL,
    id_req_form            NUMBER(3) NOT NULL,
    id_postulante          NUMBER(3) NOT NULL,
    id_beca                NUMBER(3) NOT NULL
);

ALTER TABLE cv_postulante ADD CONSTRAINT cv_postulante_pk PRIMARY KEY ( id_cv );


---FK

ALTER TABLE region
    ADD CONSTRAINT region_pais_fk FOREIGN KEY ( id_pais )
        REFERENCES pais ( id_pais );

ALTER TABLE ciudad
    ADD CONSTRAINT ciudad_region_fk FOREIGN KEY ( id_pais )
        REFERENCES pais ( id_pais );

ALTER TABLE grado_academico
    ADD CONSTRAINT grado_ins_fk FOREIGN KEY ( id_tipo_estudio )
        REFERENCES tipo_estudio ( id_tipo_estudio );

ALTER TABLE estudios_secundarios
    ADD CONSTRAINT e_pais_fk FOREIGN KEY ( id_pais )
        REFERENCES pais ( id_pais );

ALTER TABLE experiencia_laboral
    ADD CONSTRAINT experiencia_laboral_fk FOREIGN KEY ( id_institucion_pub )
        REFERENCES instituciones_publicas ( id_institucion_pub );

ALTER TABLE info_insti_extra
    ADD CONSTRAINT info_insti_extra_fk FOREIGN KEY ( id_pais )
        REFERENCES pais ( id_pais );

ALTER TABLE postulacion_beca
    ADD CONSTRAINT postulacion_beca_fk FOREIGN KEY ( id_documentos )
        REFERENCES documentos_obligatorios ( id_documentos );

ALTER TABLE descr_program_perfect
    ADD CONSTRAINT id_modulo_fk FOREIGN KEY ( id_modulo )
        REFERENCES modulo ( id_modulo );

ALTER TABLE perfil_acad_prof
    ADD CONSTRAINT perfil_acad_prof_fk FOREIGN KEY ( id_formacion )
        REFERENCES formacion_academica ( id_formacion );

ALTER TABLE perfil_acad_prof
    ADD CONSTRAINT perfil_acad_prof1_fk FOREIGN KEY ( id_experiencia_lab )
        REFERENCES experiencia_laboral ( id_experiencia_lab );

ALTER TABLE formacion_academica
    ADD CONSTRAINT formacion_academica_fk FOREIGN KEY ( id_profesional )
        REFERENCES titulo_profesional ( id_profesional );

ALTER TABLE formacion_academica
    ADD CONSTRAINT formacion_academica1_fk FOREIGN KEY ( id_estudio )
        REFERENCES estudios_secundarios ( id_estudios );

ALTER TABLE formacion_academica
    ADD CONSTRAINT formacion_academica2_fk FOREIGN KEY ( id_especializacion )
        REFERENCES estudios_especializacion ( id_especializacion );

ALTER TABLE formacion_academica
    ADD CONSTRAINT formacion_academica3_fk FOREIGN KEY ( id_grado )
        REFERENCES grado_academico ( id_grado );

ALTER TABLE req_formacion_academica
    ADD CONSTRAINT req_formacion_academica_fk FOREIGN KEY ( id_idioma )
        REFERENCES idioma_requerido ( id_idioma );

ALTER TABLE req_formacion_academica
    ADD CONSTRAINT req_formacion_academica1_fk FOREIGN KEY ( id_formacion )
        REFERENCES formacion_academica ( id_formacion );

ALTER TABLE req_formacion_academica
    ADD CONSTRAINT req_formacion_academica2_fk FOREIGN KEY ( id_perfil_acad_pr )
        REFERENCES perfil_acad_prof ( id_perfil_acad_pr );

ALTER TABLE req_formacion_academica
    ADD CONSTRAINT req_formacion_academica3_fk FOREIGN KEY ( id_institucion_extra )
        REFERENCES info_insti_extra ( id_inst_extra );

ALTER TABLE req_formacion_academica
    ADD CONSTRAINT req_formacion_academica4_fk FOREIGN KEY ( id_subespecialidad )
        REFERENCES subespecialidad ( id_subespecialidad );

ALTER TABLE req_formacion_academica
    ADD CONSTRAINT req_formacion_academica5_fk FOREIGN KEY ( id_perfil )
        REFERENCES perfil_acad_prof_bec ( id_perfil );

ALTER TABLE postulante
    ADD CONSTRAINT postulante_fk FOREIGN KEY ( id_nacionalidad )
        REFERENCES nacionalidad ( id_nacionalidad );

ALTER TABLE postulante
    ADD CONSTRAINT postulante1_fk FOREIGN KEY ( id_formacion )
        REFERENCES formacion_academica ( id_formacion );

ALTER TABLE postulante
    ADD CONSTRAINT postulante2_fk FOREIGN KEY ( id_experiencia_lab )
        REFERENCES experiencia_laboral ( id_experiencia_lab );

ALTER TABLE postulante
    ADD CONSTRAINT postulante32_fk FOREIGN KEY ( id_contacto )
        REFERENCES dato_contact ( id_contacto );

ALTER TABLE postulante
    ADD CONSTRAINT postulante4_fk FOREIGN KEY ( id_complementaria )
        REFERENCES informacion_complementaria ( id_complementaria );

ALTER TABLE postulante
    ADD CONSTRAINT postulante5_fk FOREIGN KEY ( id_etapa )
        REFERENCES etapas_postulacion ( id_etapa );

ALTER TABLE postulante
    ADD CONSTRAINT postulante6_fk FOREIGN KEY ( id_ciudad )
        REFERENCES ciudad ( id_ciudad );

ALTER TABLE postulante
    ADD CONSTRAINT postulante7_fk FOREIGN KEY ( id_req_min )
        REFERENCES req_min_postulacion ( id_req_min );

ALTER TABLE postulante
    ADD CONSTRAINT postulante8_fk FOREIGN KEY ( id_criterio )
        REFERENCES criterio_ponderacion ( id_criterio );

ALTER TABLE cv_postulante
    ADD CONSTRAINT cv_postulante_fk FOREIGN KEY ( id_linea )
        REFERENCES linea_investigacion ( id_linea );

ALTER TABLE cv_postulante
    ADD CONSTRAINT cv_postulante1_fk FOREIGN KEY ( id_jerarquia )
        REFERENCES jerarquia_academica ( id_jerarquia );

ALTER TABLE cv_postulante
    ADD CONSTRAINT cv_postulante2_fk FOREIGN KEY ( id_participacion )
        REFERENCES participacion_proyect ( id_participacion );

ALTER TABLE cv_postulante
    ADD CONSTRAINT cv_postulante3_fk FOREIGN KEY ( id_req_form )
        REFERENCES req_formacion_academica ( id_req_form );

ALTER TABLE cv_postulante
    ADD CONSTRAINT cv_postulante4_fk FOREIGN KEY ( id_postulante )
        REFERENCES postulante ( id_postulante );

ALTER TABLE cv_postulante
    ADD CONSTRAINT cv_postulante5_fk FOREIGN KEY ( id_beca )
        REFERENCES postulacion_beca ( id_beca );

ALTER TABLE estudios_especializacion
    ADD CONSTRAINT estudios_especializacion2_fk FOREIGN KEY ( id_tipo_estudio )
        REFERENCES tipo_estudio ( id_tipo_estudio );

ALTER TABLE titulo_profesional
    ADD CONSTRAINT titulo_profesional_fk FOREIGN KEY ( id_tipo_estudio )
        REFERENCES tipo_estudio ( id_tipo_estudio );
	
	              
      
		
/**************************************/

ALTER TABLE jerarquia_academica
    ADD CONSTRAINT jerarquia_academica_fk FOREIGN KEY ( id_institucion )
        REFERENCES institucion ( id_institucion );

ALTER TABLE estudios_especializacion
    ADD CONSTRAINT estudios_ins0_fk FOREIGN KEY ( id_institucion )
        REFERENCES institucion ( id_institucion );

ALTER TABLE titulo_profesional
    ADD CONSTRAINT titulo_profesional1_fk FOREIGN KEY ( id_institucion )
        REFERENCES institucion ( id_institucion );

ALTER TABLE grado_academico
    ADD CONSTRAINT grado_ins2_fk FOREIGN KEY ( id_institucion )
        REFERENCES institucion ( id_institucion );