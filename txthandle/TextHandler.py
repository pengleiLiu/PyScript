import json


# 读取文件
def import_data():
    with open("/Users/xingshulin/Desktop/orderid.json", "r") as f:
        data = f.read();
        # data = json.load(f)
        # data = json.dumps(data)
        data = json.loads(data)
        return data;


# 拼接sql,输出到指定文件中
def build_sql_str():
    dicts = import_data();
    f = open("/Users/xingshulin/Desktop/update.sql", "w")
    for order in dicts:
        sql_str = "update t_order set failId = '" + order['failedOrderId'] + "', successOrderId = '" + order[
            'successOrderId'] + "' where accountNum = '" + order['accountNum'] + "';"
        f.write("\n" + sql_str)


if __name__ == '__main__':
    build_sql_str()
