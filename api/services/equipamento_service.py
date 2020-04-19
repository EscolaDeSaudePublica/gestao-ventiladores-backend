from api.models import equipamento_model


def listar_equipamentos():
    return equipamento_model.Equipamento.objects.to_json()


def listar_equipamento(_id):
    try:
        equipamento = equipamento_model.Equipamento.objects.get(id=_id).to_json()
    except:
        equipamento = None
    finally:
        return equipamento


def consultar_numero_de_serie(numero_de_serie):
    return equipamento_model.Equipamento.objects(
        numero_de_serie=numero_de_serie
    ).only(
        'id', 'numero_de_serie'
    ).first()


def registar_equipamento(body):
    equipamento = equipamento_model.Equipamento(**body).save()
    return str(equipamento.id)


def atualizar_equipamento(atualizacao, _id):
    equipamento_model.Equipamento.objects.get(id=_id).update(**atualizacao)


def deletar_equipamento(id):
    equipamento_model.Equipamento.objects.get(id=id).delete()
