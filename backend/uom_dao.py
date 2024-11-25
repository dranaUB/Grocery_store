from models import UOM,Product,Order,OrderDetail
from app import db
connection = db.session()

def get_uoms(connection):
    # cursor = connection.cursor()
    # query = ("select * from uom")
    # cursor.execute(query)
    # response = []
    # for (uom_id, uom_name) in cursor:
    #     response.append({
    #         'uom_id': uom_id,
    #         'uom_name': uom_name
    #     })
    response=[{'uom_id':1,'uom_name':'Rice'}]
    return response


if __name__ == '__main__':
    # print(get_all_products(connection))
    print(get_uoms(connection))