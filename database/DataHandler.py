import pymysql
import uuid

host = "localhost"
port = 3306
username = 'root'
password = "root"
database = "test_demo"
charset = "utf8"


def connect_local_db():
    return pymysql.connect(host=host, port=port, user=username, password=password, database=database,
                           charset=charset)

# 查询
def query():
    sql_str = "SELECT id,name,password,CAST(create_time AS CHAR) AS create_time FROM t_user"

    db = connect_local_db()
    cursor = db.cursor()
    # 执行sql
    cursor.execute(sql_str)
    data = cursor.fetchall()

    # 关闭游标
    cursor.close()
    # 关闭数据库连接
    db.close()
    return data


# 主函数入口
if __name__ == "__main__":
    print(query())
    userList = list(query())

    it = iter(userList)
    for x in it:
        print(x)

    print("张三")

    print(uuid.uuid1())