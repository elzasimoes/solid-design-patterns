from pagamento.pagamento_cartao import PagamentoCartao
from pagamento.pagamento_pix import PagamentoPIX
from cliente import Cliente
from item import Item
from pedido.pedido_retirada import PedidoRetirada
from pedido.pedido_delivery import PedidoDelivery

cliente = Cliente("Laís", "Alura")
item_um = Item("Pizza", 30.0)
item_dois = Item("Refrigerante", 5.0)
itens = [item_um, item_dois]

taxa_entrega = 10.0
pedido_retirada = PedidoRetirada(cliente, itens)
pedido_delivery = PedidoDelivery(cliente, itens, taxa_entrega)
print(f"Preço do Pedido Delivery: {pedido_delivery.calcular_total():.2f}")


valor_pedido = pedido_delivery.calcular_total()
pagamento_cartao = PagamentoCartao().processar(valor_pedido)
pagamento_pix = PagamentoPIX()
pagamento_pix.processar(valor_pedido)