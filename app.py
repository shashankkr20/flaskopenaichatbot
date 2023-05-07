from flask import Flask,render_template,request,redirect,url_for
 
import gpt


app=Flask(__name__)

@app.route("/",methods=["POST","GET"])
def home():
    if request.method=="POST":
        prompt=request.form["promptmsg"]
        gptreply="In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. Lorem ipsum may be used as a placeholder before final copy is available"
        # print(gptreply)
        return redirect(url_for("result",result=gptreply))
    else:
        return render_template('index.html')
    
@app.route("/<result>")
def result(result):
        return render_template('result.html',prompt=result)

if __name__ == '__main__':
    app.run(debug=True)