import json

from flask import Response, request, make_response, jsonify
from flask_restful import Resource
from ..schemas import ordem_servico_schema
from ..services import ordem_servico_service
from flasgger import swag_from


class OrdemServicoList(Resource):
    # todo Denis atualizar essa url do swag
    @swag_from('../../documentacao/equipamento/equipamentos_get.yml')
    def get(self):
        ordem_servico = ordem_servico_service.listar_ordem_servico().to_json()
        return Response(ordem_servico, mimetype="application/json", status=200)

    # todo Denis atualizar essa url do swag
    @swag_from('../../documentacao/equipamento/equipamentos_post.yml')
    def post(self):
        body = request.json
        ordem_servico_cadastrado = ordem_servico_service.\
            listar_ordem_servico_by_numero_ordem_servico(body['numero_ordem_servico'])

        if ordem_servico_cadastrado:
            return make_response(jsonify("Ordem de Serviço já cadastrada..."), 403)
        es = ordem_servico_schema.OrdemServicoSchema()
        et = ordem_servico_schema.TriagemSchema()
        ea = ordem_servico_schema.AcessorioSchema()
        erro_ordem_servico = es.validate(body)
        erro_triagem = et.validate(body["triagem"])
        if erro_ordem_servico:
            return make_response(jsonify(erro_ordem_servico), 400)
        elif erro_triagem:
            return make_response(jsonify(erro_triagem), 400)
        for acessorio in body["triagem"]["acessorios"]:
            if ea.validate(acessorio):
                return make_response(jsonify(ea.validate(acessorio)), 400)
        novo_ordem_servico = ordem_servico_service.registrar_ordem_servico(body).to_json()
        return Response(novo_ordem_servico, mimetype="application/json", status=201)


class OrdemServicoDetail(Resource):
    # todo Denis atualizar essa url do swag
    @swag_from('../../documentacao/equipamento/equipamento_get.yml')
    def get(self, numero_ordem_servico):
        ordem_servico = ordem_servico_service.listar_ordem_servico_by_numero_ordem_servico(numero_ordem_servico).to_json()
        if ordem_servico is None:
            return make_response(jsonify("Ordem de serviço não encontrada..."), 404)
        return Response(ordem_servico.to_json(), mimetype="application/json", status=200)

    # todo Denis atualizar essa url do swag
    @swag_from('../../documentacao/equipamento/equipamento_put.yml')
    def put(self, _id):
        ordem_servico = ordem_servico_service.listar_ordem_servico_by_id(_id)

        if ordem_servico is None:
            return make_response(jsonify("Ordem de serviço não encontrada..."), 404)
        body = request.get_json()
        if 'diagnostico' in body:
            erro_diagnostico = ordem_servico_schema.DiagnosticoSchema().validate(body['diagnostico'])
            if erro_diagnostico:
                return make_response(jsonify(erro_diagnostico), 400)
            if 'itens' in body['diagnostico']:
                for itens in body['diagnostico']['itens']:
                    item = ordem_servico_schema.ItemSchema().validate(itens)
                    if item:
                        return make_response(jsonify(item), 400)
             # todo denis, essa mesma validacao que tu vai para itens, tu deve fazer para acessorios


        ordem_servico_service.atualizar_ordem_servico(_id, body)
        ordem_servico_atualizado = ordem_servico_service.listar_ordem_servico_by_id(_id)
        return Response(ordem_servico_atualizado.to_json(), mimetype="application/json", status=200)

    # todo Denis atualizar essa url do swag
    @swag_from('../../documentacao/equipamento/equipamento_delete.yml')
    def delete(self, numero_ordem_servico):
        ordem_servico = ordem_servico_service.listar_ordem_servico_by_numero_ordem_servico(numero_ordem_servico)
        if ordem_servico is None:
            return make_response(jsonify("Ordem de serviço não encontrada..."), 404)
        ordem_servico_service.deletar_ordem_servico(numero_ordem_servico)
        return make_response('', 204)


class OrdemServicoFind(Resource):
    # todo Denis atualizar essa url do swag
    @swag_from('../../documentacao/equipamento/equipamento_find.yml')
    def post(self):
        body = request.json
        if "status" not in body:
            return make_response(jsonify("Não existe a chave status no body"), 404)
        ordem_servico_list = ordem_servico_service.listar_ordem_servico_status(body['status'])
        return Response(ordem_servico_list.to_json(), mimetype="application/json", status=200)


class OrdemServicoFiltragem(object):

    def post(self):
        body = request.json
        body_filter = ordem_servico_service.filtering_ordem_servico_queries(body)
        return Response(body_filter, mimetype="application/json", status=200)
