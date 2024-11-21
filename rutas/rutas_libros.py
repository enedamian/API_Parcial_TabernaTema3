from flask import Blueprint, jsonify, request
from modelos.entidades.libroDigital import LibroDigital
from modelos.entidades.libroFisico import LibroFisico
from modelos.repositorios.repositorios import obtenerRepoLibros

repo_libros = obtenerRepoLibros()



@bp_libros.route('/libros', methods=['GET'])
def obtener_libros():
    libros = repo_libros.obtenerLibros()
    lista_libros = []
    for libro in libros:
        lista_libros.append(libro.toDiccionario())
    return jsonify(lista_libros), 200

@bp_libros.route('/libros/<int:ISBN>', methods=['GET'])
def obtener_libro(ISBN):
    libro = repo_libros.obtenerLibroPorISBN(ISBN)
    if libro == None:
        return jsonify({'mensaje': 'Libro no encontrado'}), 404
    return jsonify(libro.toDiccionario()), 400

