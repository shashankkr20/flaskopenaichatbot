from flask import Flask,render_template,request,redirect,url_for
 
import gpt


app=Flask(__name__)

@app.route("/",methods=["POST","GET"])
def home():
    if request.method=="POST":
        prompt=request.form["promptmsg"]
        gptreply=gpt.gpt_reply(prompt)
        # print(gptreply)
        return redirect(url_for("result",result=gptreply))
    else:
        return render_template('index.html')
    
@app.route("/<result>")
def result(result):
        return render_template('result.html',prompt=result)

if __name__ == '__main__':
    app.run(debug=True)