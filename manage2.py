from flask import Flask,render_template

app=Flask(__name__)
class person:
    name="我"
    age="100000"
@app.route("/")
def index():
    '''render_template,此函数接收一个模版文件
    模版文件必须在当前文件夹下的 templates目录
    不用传 templates 目录的名字 render_template 
    会在这个目录下找参数名字的文件
    2.此函数接收一个字典做为参数，参数名在模版文件中
    用{｛参数名｝}，引用
    3,可以接收多个字典
    4.在模版中，可以访问类属性 用"."，也可以用 "."或者["key"]来
    访问字典值'''
    
    context={
            "book":"好好学习"
            }

    context1={"username":"牛",
            "person":person,
            "kk":context}

    context2={"test":"逼"}
    return render_template("./index.html",**context1,**context2)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000,debug=True)
