class ShoppingCart:
    """单例模式"""
    __instance = None
    __has_init = False

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self) -> None:
        """初始化函数"""
        if not self.__has_init:
            self.total_price = 0
            self.__has_init = True


cart1 = ShoppingCart()
cart1.total_price = 100

cart2 = ShoppingCart()
cart3 = ShoppingCart()

print(cart1.total_price)
print(cart2.total_price)
