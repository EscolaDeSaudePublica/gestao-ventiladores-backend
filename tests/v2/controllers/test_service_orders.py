import json
from run import app
from unittest import TestCase
from mockito import when, mock
from api.v2.services.service_order_service import ServiceOrderService
from http import HTTPStatus


class ServiceOrdersController(TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_returns_service_orders_on_successful_request(self):
        service_orders = [{'equipamento_id': 1, 'numero_ordem_servico': '0400'}]
        when(ServiceOrderService).fetch_active().thenReturn(service_orders)

        response = self.client.get('/v2/service_orders')

        self.assertEqual(response.status_code, HTTPStatus.OK)
        content = response.json['content']
        self.assertEqual(type(content), list)
        self.assertIn('content', response.json)
        self.assertIn('equipamento_id', content[0])
        self.assertEqual(content[0]['equipamento_id'], service_orders[0]['equipamento_id'])


    def test_returns_empty_list(self):
        service_orders = []
        when(ServiceOrderService).fetch_active().thenReturn(service_orders)

        response = self.client.get('/v2/service_orders')

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.json['content'], [])

    def test_returns_deleted_service_orders_on_successful_request(self):
        service_orders = [{'equipamento_id': 1, 'numero_ordem_servico': '0400'}]
        when(ServiceOrderService).fetch_all().thenReturn(service_orders)

        response = self.client.get('/v2/service_orders?deleted=true')

        self.assertEqual(response.status_code, HTTPStatus.OK)
        content = response.json['content']
        self.assertEqual(content[0]['equipamento_id'], service_orders[0]['equipamento_id'])

    def test_return_invalid_param_error(self):
        response = self.client.get('/v2/service_orders?deleted=trueee')
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)
        self.assertEqual(response.json['error'], 'Parameter deleted is not equal true.')
