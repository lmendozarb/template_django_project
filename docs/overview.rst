=============
Architecture
=============

Monolith Services
-----------------

Currently the monolith is divided in the following apps, wich more or less map to services.

-CLIENTS (CONTACTS , BANK CLIENTS)
-PROVIDERS (CONTATS , BANK PROVIDER)
-SERVICES(SHIPPING, )
-WAREHOUSE(STOCK , KARDEX, PRODUCTS)
-COMMERCE(VENTA Y COMPRA-ORDEN DE COMPRA)
-FINANCE(
    CIERRE DE MES , CIERE DE AÑO , MOVIMIENTOS(DEBITO Y CREDITO),/
    CAJA CHICA Y GASTOS,SUNAT SUNAT)
-SETTINGS(TAXES,LANGUAGE, PLACES, MEASUREMENT,FXRATES, COMPANY INFORMATION)
-CRM


Nomenclature
-------------
    NAME VALUES:
        example: date_recived_mail
    NAME FUNCION:
        example: def createclient():
    NAME CLASS:
        example: class ApiConnectSpider():


    MODEL EXAMPLE:
        name = Char.field("Nombre del Cliente", max_lenght=150,default="")
    