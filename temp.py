
import xmlrpc.client

records_v1 = []
records_v2 = []
url_15 = 'http://localhost:8015'
db_15 = "odoo15_com"
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
print(records_15, "************ records_15 ***************")

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
                                {'fields': ['name', 'display_type',
                                             'attribute_line_ids',
                                            'product_tmpl_ids',
                                            ]})
attr_val_14 = models_14.execute_kw(db_14, uid_14, pwd_14,
                                   'product.attribute.value',
                                   'search_read', [],
                                   {'fields': ['attribute_id',
                                               'pav_attribute_line_ids',
                                               'is_used_on_products',
                                               'name', 'is_custom',
                                               'display_type']})
# attr_line_14 = models_14.execute_kw(db_14, uid_14, pwd_14,
#                                     'product.template.attribute.line',
#                                     'search_read', [],
#                                     {'fields': [ 'attribute_id',
#                                                 'product_tmpl_id',
#                                                 'product_template_value_ids']})
# attr_line_val_14 = models_14.execute_kw(db_14, uid_14, pwd_14,
#                                         'product.template.attribute.value',
#                                         'search_read', [],
#                                         {'fields': ['name',
#                                                     'product_attribute_value_id',
#                                                     'attribute_line_id',
#                                                     'price_extra',
#                                                     'product_tmpl_id',
#                                                     'attribute_id',
#                                                     'ptav_product_variant_ids']})
template_14 = models_14.execute_kw(db_14, uid_14, pwd_14,
                                   'product.template',
                                   'search_read', [],
                                   {'fields': ['name', 'list_price',
                                               'is_product_variant',
                                               'valid_product_template_attribute_line_ids',
                                               'product_variant_ids',
                                               'product_variant_id',
                                               'barcode',
                                               'has_configurable_attributes',
                                               'attribute_line_ids'
                                               ]})
# attr_val_14_rel = models_14.execute_kw(db_14, uid_14, pwd_14,
#                                        'product.template.attribute.line',
#                                        'search_read', [],
#                                        {'fields': ['attribute_id',
#                                                    'product_tmpl_id'
#                                                    ]})
records_14 = models_14.execute_kw(db_14, uid_14, pwd_14, 'product.product',
                                  'search_read', [],
                                  {'fields': ['name', 'id', 'type',
                                              'price',
                                              'lst_price', 'default_code',
                                              'code',
                                              'product_tmpl_id',
                                              'barcode',
                                              'product_template_attribute_value_ids',
                                              'combination_indices',
                                              'is_product_variant',
                                              'standard_price',
                                              # 'image_1920'
                                              ]})

print(records_14, "************  records_14  ***************")

for i in records_14:
    if i.get('name') or i.get('default_code'):
        records_v1.append({'default_code': i['default_code'], 'name': i['name'],
                           'lst_price': i['lst_price'],
                           'standard_price': i['standard_price'],
                           # 'image_1920': i['image_1920'],
                           # 'product_template_attribute_value_ids':
                           #     i['product_template_attribute_value_ids']
                           })
print(len(records_v1), "<<<<<<<<<<<< <<<<<<<<<<< V1 >>>>>>>>>>> >>>>>>>>>>>>")

for i in records_15:
    if i.get('name') or i.get('default_code'):
        records_v2.append({'default_code': i['default_code'], 'name': i['name'],
                           'lst_price': i['lst_price'],
                           'standard_price': i['standard_price']})
print(len(records_v2), "<<<<<<<<<< <<<<<<<<<<<<< v2 >>>>>>>>>>>>> >>>>>>>>>>")

change_list = []
target = []

for x in records_15:
    # print(x['default_code'], "x")
    change_list.append(x['default_code'])
for y in records_14:
    # print(y, "y")
    if not y['default_code'] in change_list:
        target.append(y)
models_15.execute_kw(
    db_15, uid_15, pwd_15, 'product.attribute', 'create', [attrs_14])
models_15.execute_kw(
    db_15, uid_15, pwd_15, 'product.attribute.value', 'create', [attr_val_14])
# models_15.execute_kw(
#     db_15, uid_15, pwd_15, 'product.template.attribute.line', 'create', [attr_val_14_rel])
# models_15.execute_kw(
#     db_15, uid_15, pwd_15, 'product.product', 'create', [target])
# print("success", target)
print("done!")

# for i in records_14: if i.get('name') or i.get('default_code'):
# records_v1.append({'default_code': i['default_code'], 'name': i['name'],
# 'lst_price': i['lst_price'], 'standard_price': i['standard_price'],
# 'image_1920': i['image_1920'] }) print(len(records_v1), "<<<<<<<<<<<<
# <<<<<<<<<<< V1 >>>>>>>>>>> >>>>>>>>>>>>")
#
# for i in records_15:
#     if i.get('name') or i.get('default_code'):
#   records_v2.append({'default_code': i['default_code'], 'name': i['name'],
#                            'lst_price': i['lst_price'],
#                            'standard_price': i['standard_price']})
# print(len(records_v2), "<<<<<<<<<< <<<<<<<<<<<<< v2 >>>>>>>>>>>>> >>>>>>>>>>")


