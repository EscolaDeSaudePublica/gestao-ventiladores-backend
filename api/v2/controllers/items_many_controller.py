from flask_restful import Resource
from flask import make_response, jsonify, request
from ..helpers.helper_response import error_response, get_response, post_response
from ..helpers.helper_update import pop_id
from ..services.item_service import ItemService
from ..validation.schemas.item_schema import ItemSchema
from ..validation.validation_request import (
    validate_request,
    validate_post,
    invalid_deleted_parameter,
    validate_request_dict_id,
    validate_request_id,
    validate_is_list
)
import json


class ItemsManyController(Resource):
    def get(self):
        args_deleted = request.args.get("deleted")
        if invalid_deleted_parameter(args_deleted):
            return error_response("Parameter deleted is not equal true.", 400)

        content = ItemService().fetch_items_list(args_deleted)

        return get_response(content, args_deleted)

    def post(self):
        body = request.get_json()

        validate, message = validate_request(body)
        if not validate:
            return error_response(message)

        errors = []
        for index, item in enumerate(body["content"]):
            validate, message = validate_post(item)
            if not validate:
                errors.append({index: message})
                continue

            erro_schema = ItemSchema().validate(item)
            if erro_schema:
                errors.append({index: erro_schema})

        if errors:
            return error_response(errors)

        content = []
        for item in body["content"]:
            content.append(ItemService().register_item(item))

        return post_response(content)

    def put(self):
        body = request.get_json()
        validate, message = validate_request(body)
        if not validate:
            return error_response(message)

        errors = []
        for index, item in enumerate(body['content']):
            validate, message = validate_id(item)
            if not validate:
                errors.append({index: message})
                continue

            erro_schema = ItemSchema().validate(item)
            if erro_schema:
                errors.append({index: erro_schema})

        if errors:
            return error_response(errors)

        for index, item in enumerate(body['content']):
            id = pop_id(item)
            ItemService().replace_fields(id, item)

        return '', 200

    def patch(self):
        body = request.get_json()
        validate, message = validate_request(body)
        if not validate:
            return error_response(message)

        errors = []
        for index, item in enumerate(body["content"]):
            validate, message = validate_request_dict_id(item)
            if not validate:
                errors.append({index: message})
                continue

            erro_schema = ItemSchema().validate_updates(item, index)
            if erro_schema:
                errors.append({index: erro_schema})

        if errors:
            return error_response(errors)

        for index, item in enumerate(body["content"]):
            id = pop_id(item)
            ItemService().update_item_only_fields(data=item, id=id)

        return "", 200

    def delete(self):
        body = request.get_json()
        validate, message = validate_request(body)
        if not validate:
            return error_response(message)

        validate, message = validate_is_list(body['content'])
        if not validate:
            return error_response(message)

        errors = []
        for index, _id in enumerate(body['content']):
            validate, message = validate_request_id(_id)

            if not validate:
                errors.append({index: message})

        if errors:
            return error_response(errors)


        for _id in body['content']: 
            ItemService().delete_item(_id)

        return "", 200
