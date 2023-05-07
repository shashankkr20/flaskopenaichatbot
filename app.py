from flask import Flask,render_template,request,redirect,url_for
 
import gpt


app=Flask(__name__)

@app.route("/",methods=["POST","GET"])
def home():
    if request.method=="POST":
        prompt=request.form["promptmsg"]
        gptreply="The largest animal in the world is the blue whale (Balaenoptera musculus). These magnificent creatures can grow up to 100 feet (30 meters) in length and weigh as much as 200 tons (181 metric tons). Despite their enormous size, blue whales feed mostly on tiny shrimp-like animals called krill, which they filter from the water using a specialized structure called baleen. Blue whales are found in oceans around the world, and are considered an endangered species due to past hunting and current threats such as climate change and habitat loss."
        #gpt.gpt_reply(prompt)
        # print(gptreply)
        return redirect(url_for("result",result=gptreply))
    else:
        return render_template('index.html')
    
@app.route("/<result>")
def result(result):
        return render_template('result.html',prompt=result)

if __name__ == '__main__':
    app.run(debug=True)