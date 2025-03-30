from pagamento.pagamento_pix import PagamentoPIX
from pagamento.pagamento_cartao import PagamentoCartao

class PagamentoFactory:
    """
    A factory class for creating payment instances.

    This class provides a static method to create instances of different
    payment types based on the specified type. Supported types are "pix"
    and "cartao". Raises a ValueError if an unsupported type is provided.

    Methods:
        criar_pagamento(tipo): Returns an instance of PagamentoPIX or
        PagamentoCartao based on the provided type.
    """
    @staticmethod
    def criar_pagamento(tipo):
        if tipo == "pix":
            return PagamentoPIX()
        elif tipo == "cartao":
            return PagamentoCartao()
        else:
            raise ValueError(f"Tipo de pagamento '{tipo}' não suportado")