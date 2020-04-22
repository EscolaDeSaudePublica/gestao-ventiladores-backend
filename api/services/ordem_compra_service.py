from api.models import ordem_compra_model

def listar_ordem_compras():
    """
        Retorna todas as ordens de compra
    """
    return ordem_compra_model.OrdemCompra.objects


def listar_ordem_compra_by_id(id):
    """
        Retorna a ordem de compra pelo 'id'
    """
    try:
        return ordem_compra_model.OrdemCompra.objects.get(id=id)
    except:
        return None


def listar_ordem_compra_by_numero_ordem_compra(numero_ordem_compra):
    """
        Retorna a ordem de compra pelo 'numero_ordem_compra'
    """
    try:
        return ordem_compra_model.OrdemCompra.objects.get(numero_ordem_compra=numero_ordem_compra)
    except:
        return None


def registar_ordem_compra(body):
    """
        Se a lista de itens for vazia retorna um erro, se não, cria um
        'número_ordem_compra' baseado na quantidade de documentos no banco
         e cadastra uma nova ordem de compra.
    """
    quantidade_itens = len(body['itens'])
    if quantidade_itens == 0:
        return {"numero_ordem_compra": body["numero_ordem_compra"], "itens": ["array"]}
    else:
        qtd_ordem_compra = ordem_compra_model.OrdemCompra.objects.count()
        numero_ordem_compra = str(qtd_ordem_compra + 1).zfill(4)
        body['numero_ordem_compra'] = numero_ordem_compra
        return ordem_compra_model.OrdemCompra(**body).save()


