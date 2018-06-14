#coding:utf8
from flask import Flask,url_for,redirect
#导入配置文件conf，配置文件名字可以随便起，但必须是py文件
import conf
app=Flask(__name__)
#把配置文件和app绑定
app.config.from_object(conf)
with open("/var/www/html/index.html","r") as f:
    file_index=f.read()
#app.route装饰器，接收的值是从浏览器发来的值，而装饰函数的返回值是返回给浏览器的页面
@app.route("/")
def hello():
    '''url_for第一个参数接收视图函数名的字符串，
    第二个参数用关键字传值是视图函数参数键值对
    他会返回视图函数对应的url'''
    print(url_for("jj",gg="abc"))
    return file_index 
@app.route("/test") 
def test():
    jj_url=url_for("jj",gg='hhh')
    '''redirect重定向，这个函数接收一个url地址，并发给浏览器此地址所代表
    的视图函数内容，可以用url_for函数将视图函数转成地址'''

    return redirect(jj_url)
#浏览器发来的id,通过<id>作为函数jj的id参数
@app.route("/<gg>")
def jj(gg):
    return "你请求的参数是：%s"%id
if __name__ == "__main__":
#app.run 表示持续监听
    app.run(host="0.0.0.0",port=8000,debug=True)
