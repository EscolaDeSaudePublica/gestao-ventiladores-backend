from copy import deepcopy

from api.v2.services.item_service import ItemService
import api.v2.repositories.service_order_repository as service_order_repository
from api.v2.services.service_order_service import ServiceOrderService
from api.v2.utils.service_order_util import (has_accessories_service_order, has_items_service_order)
from .service_base import ServiceBase
from ..helpers.helper_update import pop_id


class ItemsMergeService(ServiceBase):
    def create_new_item_from_to_update(self, item):
        return ItemService().register_item(item)

    def handle_update_service_order(self, service_order, items_to_remove, new_item_id):
        to_update = False
        to_update_diagnostico = False
        to_update_triagem = False

        for item_to_remove in items_to_remove:
            if has_items_service_order(service_order):
                to_update_diagnostico = self.loop_and_update(('diagnostico', 'itens'), service_order, item_to_remove,
                                                             new_item_id)

            if has_accessories_service_order(service_order):
                to_update_triagem = self.loop_and_update(('triagem', 'acessorios'), service_order, item_to_remove,
                                                         new_item_id)

        if to_update_diagnostico or to_update_triagem:
            to_update = to_update_diagnostico
        return to_update, service_order

    def loop_and_update(self, key_names, service_order, item_to_remove, new_item_id):
        for i in range(len(service_order[key_names[0]][key_names[1]])):
            item = service_order[key_names[0]][key_names[1]][i]
            if item["item_id"] == item_to_remove:
                item["item_id"] = new_item_id
                service_order[key_names[0]][[key_names[1]][i]] = item
                return True

    def delete_items_to_remove(self, to_remove):
        for item_id in to_remove:
            ItemService().delete_item(item_id)

    def handle_removed_items(self, to_remove, new_item_id):
        ordens_servico = service_order_repository.fetch_all()
        for service_order in self.convert_mongo_to_dict(ordens_servico):
            service_order_copy = deepcopy(service_order)
            self.remove_oid(service_order_copy)
            to_update, data = self.handle_update_service_order(service_order_copy, to_remove, new_item_id)
            if to_update:
                _id = pop_id(data)
                ServiceOrderService().update(_id, data)

    def register_items(self, body):
        new_item_id = self.create_new_item_from_to_update(body["content"]["toUpdate"])
        self.handle_removed_items(body["content"]["toRemove"], new_item_id)
        self.delete_items_to_remove(body["content"]["toRemove"])
        return True, new_item_id
