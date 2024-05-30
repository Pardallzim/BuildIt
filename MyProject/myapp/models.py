from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Produto: Representa os diferentes materiais disponíveis na loja. 
# Deve incluir campos como nome, descrição, preço, imagem, e quantidade_em_estoque.


# Pedido: Registra um pedido feito por um cliente.
# Deve incluir uma relação com o modelo User (cliente que fez o pedido) e um campo data_do_pedido.


class Product(models.Model):
    name = models.CharField(max_length=240)
    descript = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    path = models.ImageField(upload_to="imagens/")
    storage = models.IntegerField()


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    members = models.ManyToManyField(
        Product,
        through="ItemsOrder",
        through_fields=("order", "product"),
    )


class ItemsOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()