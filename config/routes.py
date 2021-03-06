from api.views import (
    ordem_servico_view,
    fabricante_view,
    importador_view,
    foto_view,
    equipamento_view,
    ordem_compra_view,
    movimentacao_view,
    log_view,
    calibragem_view,
    diagnostico_view, utils_view
)


def initialize_routes(api):
    api.add_resource(equipamento_view.EquipamentoList,
                     '/api/equipamentos')
    api.add_resource(equipamento_view.EquipamentoBulk,
                     '/api/equipamentos/bulk')
    api.add_resource(equipamento_view.EquipamentoDetail,
                     '/api/equipamento/<_id>')

    api.add_resource(ordem_servico_view.OrdemServicoList,
                     '/api/ordem_servicos')
    api.add_resource(ordem_servico_view.OrdemServicoDetail,
                     '/api/ordem_servico/<_id>')
    api.add_resource(ordem_servico_view.OrdemServicoQuery,
                     '/api/ordem_servico/find')

    api.add_resource(
        importador_view.TriagemImportacao, '/api/importar/triagem')
    api.add_resource(importador_view.DiagnosticoImportacao,
                     '/api/importar/diagnostico')
    api.add_resource(foto_view.TriagemImagem, '/api/importar/imagem')

    api.add_resource(fabricante_view.FabricanteList, '/api/fabricantes')
    api.add_resource(fabricante_view.FabricanteDetail,
                     '/api/fabricante/<fabricante_nome>')

    api.add_resource(ordem_compra_view.OrdemCompraList, '/api/ordem_compra')
    api.add_resource(ordem_compra_view.OrdemCompraDetail,
                     '/api/ordem_compra/<_id>')
    api.add_resource(ordem_compra_view.OrdemCompraQuery,
                     '/api/ordem_compra/find')

    api.add_resource(movimentacao_view.MovimentacaoList, '/api/movimentacao')
    api.add_resource(movimentacao_view.MovimentacaoDetail,
                     '/api/movimentacao/<_id>')
    api.add_resource(movimentacao_view.MovimentacaoQuery,
                     '/api/movimentacao/')

    api.add_resource(log_view.LogQuery, '/api/logs/find')

    api.add_resource(calibragem_view.CalibragemCrud, '/api/calibragem')
    api.add_resource(diagnostico_view.DiagnosticoCrud, '/api/diagnosticos')
    api.add_resource(utils_view.VersaoView, '/api/')
