from flask import Flask,request,jsonify
from gpt_bot import GPTBot
from metaprompt.scene_analyzer import metaprompt as metaSA
from metaprompt.code_instructor import metaprompt as metaCI

app = Flask(__name__)
bot0 = GPTBot()
bot1 = GPTBot()
botSceneAnalyzer = GPTBot(role=metaSA)
botCodeInstructor = GPTBot(role=metaCI)

@app.route("/chatgpt/question0",methods=["POST"])
def question0():
    prompt = request.json
    question = prompt["question"]

    response = bot0.ask(question)
    print(response)
    return response
    
@app.route("/chatgpt/question1",methods=["POST"])
def question1():
    prompt = request.json
    question = prompt["question"]

    response = bot1.ask(question)
    print(response)
    return response   

@app.route("/chatgpt/sceneAnalyzer",methods=["POST"])
def sceneAnalyzer():
    prompt = request.json
    question = prompt["question"]

    response = botSceneAnalyzer.ask(question)
    print(response)
    return response   

@app.route("/chatgpt/codeInstructor",methods=["POST"])
def codeInstructor():
    prompt = request.json
    question = prompt["question"]

    response = botCodeInstructor.ask(question)
    print(response)
    return response  

@app.route("/chatgpt/status",methods=["GET"])
def status():
    return jsonify(status="ok")

if __name__ == "__main__":
    app.run(threaded=False)