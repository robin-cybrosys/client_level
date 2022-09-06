import xmlrpc.client

print("CHECKING FOR RECORDS.....")
records_v1 = []
records_v2 = []
url_15 = 'http://localhost:8015'
db_15 = 'odoo15_com'
login_15 = 'admin'
pwd_15 = 'admin'
common_15 = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url_15))
uid_15 = common_15.authenticate(db_15, login_15, pwd_15, {})
models_15 = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url_15))
records_15 = models_15.execute_kw(db_15, uid_15, pwd_15, 'product.product',
                                  'search_read', [],
                                  {'fields': ['name', 'id', 'detailed_type',
                                              'default_code',
                                              'lst_price', 'standard_price',
                                              ]})
print("<<<<", len(records_15), "DUPLICATE RECORDS EXISTS ON V15 >>>>")

url_14 = 'http://localhost:8014'
db_14 = "odoo14_com"
login_14 = 'admin'
pwd_14 = 'admin'
common_14 = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url_14))
uid_14 = common_14.authenticate(db_14, login_14, pwd_14, {})
models_14 = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url_14))

attrs_14 = models_14.execute_kw(db_14, uid_14, pwd_14,
                                'product.attribute',
                                'search_read', [],
                                {'fields': ['name', 'id', 'product_tmpl_ids']})
records_14 = models_14.execute_kw(db_14, uid_14, pwd_14, 'product.product',
                                  'search_read', [],
                                  {'fields': ['name', 'id', 'type',
                                              'default_code',
                                              'lst_price', 'standard_price',
                                              'image_1920'
                                              ]})

print("<<<<", len(records_14), "RECORDS TO BE MIGRATED FROM V14 >>>>")

change_list = []
target = []

for x in records_15:
    change_list.append(x['default_code'])
for y in records_14:
    if not y['default_code'] in change_list:
        target.append(y)
models_15.execute_kw(
    db_15, uid_15, pwd_15, 'product.product', 'create', [target])
print("<<<<", len(records_14), "RECORDS MIGRATED TO 15.0! >>>>")

print("<<<<<<<<<<<< MIGRATION COMPLETED! >>>>>>>>>>>>")
