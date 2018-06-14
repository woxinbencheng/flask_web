from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import conf

app=Flask(__name__)
#app绑定配置文件
app.config.from_object(conf)
#将app配置绑定数据库驱动
db=SQLAlchemy(app)
#数据库的表通过类的映射实现
class Test(db.Model):
    #表名
    __tablename__="test"
    #表id字段
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    #表title字段
    title=db.Column(db.String(100),nullable=False)
    #表content字段
    content=db.Column(db.Text,nullable=False)
#测试有没有报错
db.create_all()


@app.route("/")
def index():
    # 数据库增加数据
    # data=Test(title="aaa",content="bbb")
    # db.session.add(data)
    # db.session.commit()
    #-----------------------------------------------------
    #数据库查数据
    # result=Test.query.filter(Test.title=="aaa").all()
    # print(result[0])
    # print(result[0].title)
    # print(result[0].content)
    #------------------------------------------------------
    #数据库改数据
    # result=Test.query.filter(Test.title=="aaa").first()
    # result.title="222"
    # db.session.commit()
    #-----------------------------------------------------
    #数据库删除数据
     result=Test.query.filter(Test.content=="bbb").first()
     db.session.delete(result)
     db.session.commit()


     return "index"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000,debug=True)
