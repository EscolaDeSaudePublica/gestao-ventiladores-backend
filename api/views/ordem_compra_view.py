import json
from flask import Response, request, jsonify, make_response
from flask_restful import Resource
from ..services import ordem_compra_service, log_service
from flasgger import swag_from


class OrdemCompraList(Resource):
    @swag_from("../../documentacao/ordem_compra/ordem_compras_get.yml")
    def get(self):
        """ Retorna todas as ordens de compra """
        ordem_compra_registrada = ordem_compra_service \
            .listar_ordem_compras().to_json()
        return Response(ordem_compra_registrada,
                        mimetype="application/json",
                        status=200)

    @swag_from("../../documentacao/ordem_compra/ordem_compra_post.yml")
    def post(self):
        """
         Cadastra uma nova ordem de compra caso a requisição venha sem "_id"
         Atualiza a ordem de compra caso a requisição venha com "_id"
         Retorna um erro caso a lista esteja vazia.
        """
        body = request.json
        existe_id = body.get("_id")

        if existe_id and existe_id != "":
            # Atualiza a ordem de compra
            ordem_compra = ordem_compra_service.listar_ordem_compra_by_id(
                body["_id"])
            if not ordem_compra:
                return make_response(
                    jsonify("Ordem de compra não encontrada..."), 404)

            ordem_compra_service.atualizar_ordem_compra(body["_id"], body)
            nova_ordem_compra = ordem_compra_service.listar_ordem_compra_by_id(
                body["_id"]
            )
        else:
            try:
                del body["_id"]
            except KeyError:
                print("_id não está presente no body")

            # Registra uma ordem de compra
            nova_ordem_compra = ordem_compra_service.registar_ordem_compra(
                body)
            if "error" in nova_ordem_compra:
                return jsonify(nova_ordem_compra)

        return jsonify({"_id": str(nova_ordem_compra.id)})


class OrdemCompraDetail(Resource):
    @swag_from("../../documentacao/ordem_compra/ordem_compra_get.yml")
    def get(self, _id):
        """ Retorna uma ordem de compra específica conforme o id passado """
        ordem_compra = ordem_compra_service.listar_ordem_compra_by_id(
            _id).to_json()
        return Response(ordem_compra, mimetype="application/json", status=200)

    @swag_from("../../documentacao/ordem_compra/ordem_compra_put.yml")
    def put(self, _id):
        """ Atualiza a ordem de compra """
        body = request.json
        ordem_compra = ordem_compra_service.listar_ordem_compra_by_id(_id)
        if ordem_compra is None:
            return make_response(
                jsonify("Ordem de compra não encontrada..."), 404)

        updated_body = json.loads(
            ordem_compra_service.deserealize_ordem_compra(body).to_json()
        )
        old_body = json.loads(ordem_compra.to_json())
        log_service.registerLog(
            "ordem_compra",
            old_body,
            updated_body,
            ignored_fields=["numero_ordem_compra", "created_at", "updated_at"],
            all_fields=False,
        )

        ordem_compra_service.atualizar_ordem_compra(_id, body)
        nova_ordem_compra = ordem_compra_service.listar_ordem_compra_by_id(_id)
        return jsonify({"_id": str(nova_ordem_compra.id)})

    @swag_from("../../documentacao/ordem_compra/ordem_compra_delete.yml")
    def delete(self, _id):
        """ Remover uma ordem de compra """
        ordem_compra_service.deletar_ordem_compra(_id)
        return jsonify({"ok": True})


class OrdemCompraQuery(Resource):
    #  @swag_from('../../documentacao/ordem_compra/ordem_compra_find.yml')
    def post(self, _id):
        """ Retorna os dados da ordem de compra
            conforme os campos passados no body """
        body = request.json
        dados_filtrados = ordem_compra_service.ordem_compra_queries(body)
        return Response(
            dados_filtrados,
            mimetype="application/json",
            status=200)
