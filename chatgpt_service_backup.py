from flask import Flask,request,jsonify
from  lwe import ApiBackend

app = Flask(__name__)
bot = ApiBackend()

# @app.route("/chatgpt/question",methods=["POST"])
# def question():
    # args = request.args
    # prompt = request.json
    # question = prompt[]

    # if args.get("debug", default=False, type=bool):
    #     print("ChatGPT Question Received...")
    #     print("ChatGPT Question is : {}".format(question))

    # response = client.chat.completions.create()
    # if args.get("debug", default=False, type=bool):
    #     print("ChatGPT Response Received...")
    #     print(response)

@app.route("/chatgpt/question",methods=["POST"])
def question():
    # args = request.args
    prompt = request.json
    question = prompt["question"]

    success, response, message = bot.ask(question)
    if success:
        print(response)
        return response
    else:
        raise RuntimeError(message)    
   

@app.route("/chatgpt/status",methods=["GET"])
def status():
    return jsonify(status="ok")

if __name__ == "__main__":
    app.run(threaded=False)