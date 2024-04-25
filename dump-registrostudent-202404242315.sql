PGDMP  6                    |            registrostudent    16.2    16.2 %    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    32988    registrostudent    DATABASE     �   CREATE DATABASE registrostudent WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Spanish_Bolivia.1252';
    DROP DATABASE registrostudent;
                postgres    false                        2615    2200    public    SCHEMA        CREATE SCHEMA public;
    DROP SCHEMA public;
                pg_database_owner    false            �           0    0    SCHEMA public    COMMENT     6   COMMENT ON SCHEMA public IS 'standard public schema';
                   pg_database_owner    false    4            �            1259    32990    estudiantes    TABLE     �   CREATE TABLE public.estudiantes (
    id_estudiante integer NOT NULL,
    nombre_completo character varying(300) NOT NULL,
    fecha_nacimiento date NOT NULL,
    carrera character varying(300) NOT NULL
);
    DROP TABLE public.estudiantes;
       public         heap    postgres    false    4            �            1259    32989    estudiantes_id_estudiante_seq    SEQUENCE     �   CREATE SEQUENCE public.estudiantes_id_estudiante_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.estudiantes_id_estudiante_seq;
       public          postgres    false    216    4            �           0    0    estudiantes_id_estudiante_seq    SEQUENCE OWNED BY     _   ALTER SEQUENCE public.estudiantes_id_estudiante_seq OWNED BY public.estudiantes.id_estudiante;
          public          postgres    false    215            �            1259    33006    inscripciones    TABLE     �   CREATE TABLE public.inscripciones (
    id_inscripcion integer NOT NULL,
    id_estudiante integer NOT NULL,
    id_materia integer NOT NULL
);
 !   DROP TABLE public.inscripciones;
       public         heap    postgres    false    4            �            1259    33005     inscripciones_id_inscripcion_seq    SEQUENCE     �   CREATE SEQUENCE public.inscripciones_id_inscripcion_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 7   DROP SEQUENCE public.inscripciones_id_inscripcion_seq;
       public          postgres    false    4    220            �           0    0     inscripciones_id_inscripcion_seq    SEQUENCE OWNED BY     e   ALTER SEQUENCE public.inscripciones_id_inscripcion_seq OWNED BY public.inscripciones.id_inscripcion;
          public          postgres    false    219            �            1259    32999    materias    TABLE     �   CREATE TABLE public.materias (
    id_materia integer NOT NULL,
    nombre_materia character varying(300) NOT NULL,
    creditos integer NOT NULL
);
    DROP TABLE public.materias;
       public         heap    postgres    false    4            �            1259    32998    materias_id_materia_seq    SEQUENCE     �   CREATE SEQUENCE public.materias_id_materia_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.materias_id_materia_seq;
       public          postgres    false    218    4            �           0    0    materias_id_materia_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.materias_id_materia_seq OWNED BY public.materias.id_materia;
          public          postgres    false    217            �            1259    41009    notas    TABLE     |   CREATE TABLE public.notas (
    id_nota integer NOT NULL,
    nota numeric NOT NULL,
    id_inscripcion integer NOT NULL
);
    DROP TABLE public.notas;
       public         heap    postgres    false    4            �            1259    41008    notas_id_nota_seq    SEQUENCE     �   CREATE SEQUENCE public.notas_id_nota_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.notas_id_nota_seq;
       public          postgres    false    222    4            �           0    0    notas_id_nota_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.notas_id_nota_seq OWNED BY public.notas.id_nota;
          public          postgres    false    221            )           2604    40985    estudiantes id_estudiante    DEFAULT     �   ALTER TABLE ONLY public.estudiantes ALTER COLUMN id_estudiante SET DEFAULT nextval('public.estudiantes_id_estudiante_seq'::regclass);
 H   ALTER TABLE public.estudiantes ALTER COLUMN id_estudiante DROP DEFAULT;
       public          postgres    false    216    215    216            +           2604    40986    inscripciones id_inscripcion    DEFAULT     �   ALTER TABLE ONLY public.inscripciones ALTER COLUMN id_inscripcion SET DEFAULT nextval('public.inscripciones_id_inscripcion_seq'::regclass);
 K   ALTER TABLE public.inscripciones ALTER COLUMN id_inscripcion DROP DEFAULT;
       public          postgres    false    219    220    220            *           2604    40987    materias id_materia    DEFAULT     z   ALTER TABLE ONLY public.materias ALTER COLUMN id_materia SET DEFAULT nextval('public.materias_id_materia_seq'::regclass);
 B   ALTER TABLE public.materias ALTER COLUMN id_materia DROP DEFAULT;
       public          postgres    false    218    217    218            ,           2604    41012    notas id_nota    DEFAULT     n   ALTER TABLE ONLY public.notas ALTER COLUMN id_nota SET DEFAULT nextval('public.notas_id_nota_seq'::regclass);
 <   ALTER TABLE public.notas ALTER COLUMN id_nota DROP DEFAULT;
       public          postgres    false    221    222    222            �          0    32990    estudiantes 
   TABLE DATA           `   COPY public.estudiantes (id_estudiante, nombre_completo, fecha_nacimiento, carrera) FROM stdin;
    public          postgres    false    216   *       �          0    33006    inscripciones 
   TABLE DATA           R   COPY public.inscripciones (id_inscripcion, id_estudiante, id_materia) FROM stdin;
    public          postgres    false    220   �+       �          0    32999    materias 
   TABLE DATA           H   COPY public.materias (id_materia, nombre_materia, creditos) FROM stdin;
    public          postgres    false    218   �,       �          0    41009    notas 
   TABLE DATA           >   COPY public.notas (id_nota, nota, id_inscripcion) FROM stdin;
    public          postgres    false    222   �-       �           0    0    estudiantes_id_estudiante_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.estudiantes_id_estudiante_seq', 29, true);
          public          postgres    false    215            �           0    0     inscripciones_id_inscripcion_seq    SEQUENCE SET     O   SELECT pg_catalog.setval('public.inscripciones_id_inscripcion_seq', 43, true);
          public          postgres    false    219            �           0    0    materias_id_materia_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.materias_id_materia_seq', 49, true);
          public          postgres    false    217            �           0    0    notas_id_nota_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.notas_id_nota_seq', 4, true);
          public          postgres    false    221            .           2606    32997    estudiantes estudiantes_pkey 
   CONSTRAINT     e   ALTER TABLE ONLY public.estudiantes
    ADD CONSTRAINT estudiantes_pkey PRIMARY KEY (id_estudiante);
 F   ALTER TABLE ONLY public.estudiantes DROP CONSTRAINT estudiantes_pkey;
       public            postgres    false    216            2           2606    33011     inscripciones inscripciones_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.inscripciones
    ADD CONSTRAINT inscripciones_pkey PRIMARY KEY (id_inscripcion);
 J   ALTER TABLE ONLY public.inscripciones DROP CONSTRAINT inscripciones_pkey;
       public            postgres    false    220            0           2606    33004    materias materias_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.materias
    ADD CONSTRAINT materias_pkey PRIMARY KEY (id_materia);
 @   ALTER TABLE ONLY public.materias DROP CONSTRAINT materias_pkey;
       public            postgres    false    218            4           2606    41016    notas notas_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY public.notas
    ADD CONSTRAINT notas_pkey PRIMARY KEY (id_nota);
 :   ALTER TABLE ONLY public.notas DROP CONSTRAINT notas_pkey;
       public            postgres    false    222            5           2606    33012 .   inscripciones inscripciones_id_estudiante_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.inscripciones
    ADD CONSTRAINT inscripciones_id_estudiante_fkey FOREIGN KEY (id_estudiante) REFERENCES public.estudiantes(id_estudiante);
 X   ALTER TABLE ONLY public.inscripciones DROP CONSTRAINT inscripciones_id_estudiante_fkey;
       public          postgres    false    220    216    4654            6           2606    33017 +   inscripciones inscripciones_id_materia_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.inscripciones
    ADD CONSTRAINT inscripciones_id_materia_fkey FOREIGN KEY (id_materia) REFERENCES public.materias(id_materia);
 U   ALTER TABLE ONLY public.inscripciones DROP CONSTRAINT inscripciones_id_materia_fkey;
       public          postgres    false    218    4656    220            7           2606    41017    notas notas_id_inscripcion_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.notas
    ADD CONSTRAINT notas_id_inscripcion_fkey FOREIGN KEY (id_inscripcion) REFERENCES public.inscripciones(id_inscripcion);
 I   ALTER TABLE ONLY public.notas DROP CONSTRAINT notas_id_inscripcion_fkey;
       public          postgres    false    222    4658    220            �   �  x�MR�n�0=���p�1	�c������{��,X�[c+Tm�~��@`$�f��潇�Rta �T%����DӞ����FRk/�PAz[KN졧h	���D�X���h[���%&,�T:����I�љO�]��UR�T�Ȑ5��#�1WP:O <[O��&�h�e"�G�i�Z�������c��S��	m'��V�>0��"�,KХ>f��S�CjV �lxB˹�)��:��L���P��eﹶ�*��侲&�w��C��M�w�y�:ɩ�&�l�߅#Z"3�'���}y���k6��c1<	�@q��G6r]@k�|_���m�o��D�=�g�%Xg�d��s,�_���\�P[�
��&[2�����[ntu4ܛA��@o�3W���َ��#S�Ơ�]&�e�c�x5���aKO��⃷��yB�>@�A      �   �   x��ˑD1Cѵ̔�C.����u
���Xh",n�L��oj_~c����ͅc��	��zJ��P�lj�:T.����5�����ڃ���HQw���[!7s3��`!���F-��L/JL*�oP�l�����,+�����/�      �   4  x�5��n� ���)��Y�?e~�+"]"�KC8r�d���]..��f�Y0h�~�������%�X<�"|��� e��)s�����zz~���滧�K,1�rs������\���F�V#~�JsR���pVi}�Zi¶��ιZ�|�ҷ�.]�;��eD��ruB�!ȲJ-.��l�B$DBF��<ϚOLV�����}j�w�9�_S#�(!�2H�h���i�c*���hy��S�C���T��ǵ-x()�ᯥމ%�K�5/�!I�P���n�$�QYy�|-~�!�E�s��_�Ј�x�+��R�<9~Z      �      x�3�4�41�2�F\&`ژ+F��� >0     