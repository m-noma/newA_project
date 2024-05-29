from inspect import _void
from typing import Self
import mysql.connector

class VendingMachine:
    def __init__(self) -> None:
        mysql.connector.connect(
            host = "3306",
            user = "m-noma",
            password="m-noma"
        )

    def get_cursor(self) -> Self:
        return self.cursor()
    
    def operations_on_database(self,handl: str) -> _void:
        self.excute("{}".format(handl))

vm = VendingMachine()
db = vm.get_cursor()
db.operations_on_database("SHOW TABLES FROM `product_db`")