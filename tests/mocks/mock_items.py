# Nome unidade e quantidade (obrigatórios)
mock_items = {
    "valido": {
        "nome": "teste",
        "unidade_medida": "und",
        "quantidade": 1,
        "tipo": "",
        "fabricante": "",
        "codigo": "",
        "descricao": "",
        "created_at": "2020-06-05T15:46:37.204Z",
        "updated_at": "2020-06-05T15:46:37.204Z",
    },
    "com_deleted": {
        "nome": "teste",
        "unidade_medida": "und",
        "quantidade": 1,
        "tipo": "",
        "fabricante": "",
        "codigo": "",
        "descricao": "",
        "created_at": "$date",
        "updated_at": "$date",
        "deleted_at": "$date",
    },
    "sem_um_obrigatorio": {
        "nome": "",
        "unidade_medida": "und",
        "quantidade": 5,
        "tipo": "",
        "fabricante": "",
        "codigo": "",
        "descricao": "",
        "created_at": "$date",
        "updated_at": "$date",
    },
    "valido_sem_datas": {
        "nome": "teste",
        "unidade_medida": "und",
        "quantidade": 1,
        "tipo": "",
        "fabricante": "",
        "codigo": "",
        "descricao": "",
    },
    "valido_patch": {
        "nome": "teste",
        "tipo": "teste_patch",
        "descricao": "Estou testando",
    },
    "somente_obrigatorios": {
        "nome": "teste",
        "unidade_medida": "teste_patch",
        "quantidade": 5,
    },
    "invalido_patch": {"unidade": 5},
    "campo_errado_put": {
        "nome": "teste",
        "unidade_medida": "und",
        "quantidade": 1,
        "tipo": "",
        "fabricante": "",
        "codigo": "",
        "descricao_blabla": "",
        "created_at": "2020-06-05T15:46:37.204Z",
        "updated_at": "2020-06-05T15:46:37.204Z",
    },
    "campo_extra_errado": {
        "blabla": "blabla",
        "nome": "teste",
        "unidade_medida": "und",
        "quantidade": 1,
        "tipo": "",
        "fabricante": "",
        "codigo": "",
        "descricao": "",
        "created_at": "2020-06-05T15:46:37.204Z",
        "updated_at": "2020-06-05T15:46:37.204Z",
    },
    "invalido_id": {
        "_id": "aa202020",
        "nome": "teste",
        "unidade_medida": "und",
        "quantidade": 1,
        "tipo": "",
        "fabricante": "",
        "codigo": "",
        "descricao": "",
        "created_at": "2020-06-05T15:46:37.204Z",
        "updated_at": "2020-06-05T15:46:37.204Z",
    },
    "inexistente_id": {
        "_id": "5ecc5e521ef64069c005338a",
        "nome": "teste",
        "unidade_medida": "und",
        "quantidade": 1,
        "tipo": "",
        "fabricante": "",
        "codigo": "",
        "descricao": "",
        "created_at": "2020-06-05T15:46:37.204Z",
        "updated_at": "2020-06-05T15:46:37.204Z",
    },
    "triagem_um": {
        "descricao": "Mangueira de Oxigênio (verde)",
        "acompanha": "true",
        "quantidade": 1,
        "estado_de_conservacao": "",
    },
    "triagem_formatado": {
        "traqueias": {
            "descricao": "Traquéias",
            "acompanha": True,
            "quantidade": 49,
            "estado_de_conservacao": "",
            "reference_key": "traqueias",
        }
    },
    "objeto_item": {
        "nome": "Traquéias",
        "quantidade": 49,
        "unidade_medida": "und",
        "reference_key": "traqueias",
    },
    "item_collection": {
        "tipo": "",
        "fabricante": "",
        "codigo": "",
        "nome": "Traquéias",
        "unidade_medida": "und",
        "quantidade": 1,
        "descricao": "",
        "reference_key": "traqueias",
    },
    "diagnostico": {
        "tipo": "insumo",
        "fabricante": "",
        "codigo": "",
        "nome": "Mangueira PU 6mm",
        "unidade_medida": "Metro",
        "quantidade": 1,
        "descricao": "",
    },
    "diagnostico_formatado": {
        "mangueirapu6mm": {
            "tipo": "insumo",
            "fabricante": "",
            "codigo": "",
            "nome": "Mangueira PU 6mm",
            "unidade_medida": "Metro",
            "quantidade": 3,
            "descricao": "",
            "reference_key": "mangueirapu6mm",
        }
    },
    "itens_validos_para_merge": {
        "content": {
            "toUpdate": {
                "tipo": "acessorio",
                "fabricante": "u9bpp30a7v-6rouwqv084",
                "codigo": "tow2kxy7sgi-emml55687w",
                "nome": "Umidificador",
                "unidade_medida": "e6rpwrfudyv-g80pwqru0x",
                "quantidade": 5,
                "descricao": "wks6rg7o7r-fae0aoo9ehl",
                "created_at": "2020-06-30T11:20:20.568Z",
                "updated_at": "2020-07-01T12:38:04.613Z",
            },
            "toRemove": [
                {
                    "_id": "5efb47e83ba34949f5e22e0c",
                    "codigo": "tow2kxy7sgi-emml55687w",
                    "created_at": "2020-06-30T11:20:20.568Z",
                    "descricao": "wks6rg7o7r-fae0aoo9ehl",
                    "fabricante": "u9bpp30a7v-6rouwqv084",
                    "nome": "Umidificador",
                    "quantidade": 4,
                    "tipo": "acessorio",
                    "unidade_medida": "e6rpwrfudyv-g80pwqru0x",
                    "updated_at": "2020-07-01T12:38:04.613Z",
                },
                {
                    "_id": "5efb47e83ba34949f5e22e0d",
                    "codigo": "gcxo5f6lnhm-w43jnsu7d1c",
                    "created_at": "2020-06-30T11:20:20.568Z",
                    "descricao": "u37lm583n78-7cbj14mvoj9",
                    "fabricante": "yyqtomn30jc-ouy5nj7a6bk",
                    "nome": "Jarra",
                    "quantidade": 1,
                    "tipo": "acessorio",
                    "unidade_medida": "92ipw19b5h9-cw00rye96am",
                    "updated_at": "2020-06-30T11:20:20.568Z",
                },
            ],
        }
    },
    "itens_merge_sem_toUpdate": {
        "content": {
            "toRemove": [
                {
                    "_id": "5efb47e83ba34949f5e22e0c",
                    "codigo": "tow2kxy7sgi-emml55687w",
                    "created_at": "2020-06-30T11:20:20.568Z",
                    "descricao": "wks6rg7o7r-fae0aoo9ehl",
                    "fabricante": "u9bpp30a7v-6rouwqv084",
                    "nome": "Umidificador",
                    "quantidade": 4,
                    "tipo": "acessorio",
                    "unidade_medida": "e6rpwrfudyv-g80pwqru0x",
                    "updated_at": "2020-07-01T12:38:04.613Z",
                }
            ]
        }
    },
    "itens_merge_com_toUpdate_vazio": {
        "content": {
            "toUpdate": {},
            "toRemove": [
                {
                    "_id": "5efb47e83ba34949f5e22e0c",
                    "codigo": "tow2kxy7sgi-emml55687w",
                    "created_at": "2020-06-30T11:20:20.568Z",
                    "descricao": "wks6rg7o7r-fae0aoo9ehl",
                    "fabricante": "u9bpp30a7v-6rouwqv084",
                    "nome": "Umidificador",
                    "quantidade": 4,
                    "tipo": "acessorio",
                    "unidade_medida": "e6rpwrfudyv-g80pwqru0x",
                    "updated_at": "2020-07-01T12:38:04.613Z",
                }
            ],
        }
    },
    "itens_merge_sem_toRemove": {
        "content": {
            "toUpdate": {
                "tipo": "acessorio",
                "fabricante": "u9bpp30a7v-6rouwqv084",
                "codigo": "tow2kxy7sgi-emml55687w",
                "nome": "Umidificador",
                "unidade_medida": "e6rpwrfudyv-g80pwqru0x",
                "quantidade": 5,
                "descricao": "wks6rg7o7r-fae0aoo9ehl",
                "created_at": "2020-06-30T11:20:20.568Z",
                "updated_at": "2020-07-01T12:38:04.613Z",
            }
        }
    },
    "lista_vazia_toRemove": {
        "content": {
            "toUpdate": {
                "tipo": "acessorio",
                "fabricante": "u9bpp30a7v-6rouwqv084",
                "codigo": "tow2kxy7sgi-emml55687w",
                "nome": "Umidificador",
                "unidade_medida": "e6rpwrfudyv-g80pwqru0x",
                "quantidade": 5,
                "descricao": "wks6rg7o7r-fae0aoo9ehl",
                "_id": "5efb47e83ba34949f5e22e0c",
                "created_at": "2020-06-30T11:20:20.568Z",
                "updated_at": "2020-07-01T12:38:04.613Z",
            },
            "toRemove": [],
        }
    },
    "item_invalido_em_toUpdate": {
        "content": {
            "toUpdate": {
                "fabricante": None,
                "codigo": 0,
                "nome": False,
                "unidade_medida": 0,
                "quantidade": 0,
                "descricao": True,
                "created_at": 1593516020568,
                "updated_at": 1593607084613
            },
            "toRemove": [
                {
                    "_id": "5efb47e83ba34949f5e22e0c",
                    "codigo": "tow2kxy7sgi-emml55687w",
                    "created_at": "2020-06-30T11:20:20.568Z",
                    "descricao": "wks6rg7o7r-fae0aoo9ehl",
                    "fabricante": "u9bpp30a7v-6rouwqv084",
                    "nome": "Umidificador",
                    "quantidade": 4,
                    "tipo": "acessorio",
                    "unidade_medida": "e6rpwrfudyv-g80pwqru0x",
                    "updated_at": "2020-07-01T12:38:04.613Z"
                }
            ]
        }
    },
    "item_invalido_em_toRemove": {
        "content": {
            "toUpdate": {
                "codigo": "tow2kxy7sgi-emml55687w",
                "created_at": "2020-06-30T11:20:20.568Z",
                "descricao": "wks6rg7o7r-fae0aoo9ehl",
                "fabricante": "u9bpp30a7v-6rouwqv084",
                "nome": "Umidificador",
                "quantidade": 4,
                "tipo": "acessorio",
                "unidade_medida": "e6rpwrfudyv-g80pwqru0x",
                "updated_at": "2020-07-01T12:38:04.613Z"
            },
            "toRemove": [
                {
                    "fabricante": None,
                    "codigo": 0,
                    "nome": False,
                    "unidade_medida": 0,
                    "quantidade": 0,
                    "descricao": True,
                    "_id": 0,
                    "created_at": 1593516020568,
                    "updated_at": 1593607084613
                }
            ]
        }
    },
    "item_inexistente": {
            "_id": "0000000000000000000000",
            "tipo": "acessorio",
            "fabricante": "u9bpp30a7v-6rouwqv084",
            "codigo": "tow2kxy7sgi-emml55687w",
            "nome": "Umidificador",
            "unidade_medida": "e6rpwrfudyv-g80pwqru0x",
            "quantidade": 4,
            "descricao": "wks6rg7o7r-fae0aoo9ehl",
            "created_at": "2020-06-30T11:20:20.568Z",
            "updated_at": "2020-07-01T12:38:04.613Z",
    },
    "collection_items": [
        {
            "_id": "5efb47e83ba34949f5e22e0c",
            "tipo": "acessorio",
            "fabricante": "u9bpp30a7v-6rouwqv084",
            "codigo": "tow2kxy7sgi-emml55687w",
            "nome": "Umidificador",
            "unidade_medida": "e6rpwrfudyv-g80pwqru0x",
            "quantidade": 4,
            "descricao": "wks6rg7o7r-fae0aoo9ehl",
            "created_at": "2020-06-30T11:20:20.568Z",
            "updated_at": "2020-07-01T12:38:04.613Z",
        },
        {
            "_id": "5efb47e83ba34949f5e22e0d",
            "tipo": "acessorio",
            "fabricante": "yyqtomn30jc-ouy5nj7a6bk",
            "codigo": "gcxo5f6lnhm-w43jnsu7d1c",
            "nome": "Jarra",
            "unidade_medida": "92ipw19b5h9-cw00rye96am",
            "quantidade": 1,
            "descricao": "u37lm583n78-7cbj14mvoj9",
            "created_at": "2020-06-30T11:20:20.568Z",
            "updated_at": "2020-06-30T11:20:20.568Z",
        },
        {
            "_id": "5efb47e83ba34949f5e22e0e",
            "tipo": "acessorio",
            "fabricante": "cwocantub-iyyvalzikuf",
            "codigo": "xar7k5w9ir8-6rgz8tlrcf",
            "nome": "Válvula exalatória",
            "unidade_medida": "g5a7ez7pyra-3x4ih2qre6v",
            "quantidade": 2,
            "descricao": "52tzna0e5oe-35z7086q1r9",
            "created_at": "2020-06-30T11:20:20.568Z",
            "updated_at": "2020-06-30T11:20:20.568Z",
        },
        {
            "_id": "5efb47e83ba34949f5e22e0f",
            "tipo": "acessorio",
            "fabricante": "b29r9ux3n2o-lpj3l3a8eps",
            "codigo": "s071asp99wn-tkqoj2pw9f",
            "nome": "Membrana",
            "unidade_medida": "y0tgdpadau-rfi8sqo1hda",
            "quantidade": 8,
            "descricao": "nrrcu37lrhl-ewtmi3ocedi",
            "created_at": "2020-06-30T11:20:20.568Z",
            "updated_at": "2020-06-30T11:20:20.568Z",
        },
    ],
}
