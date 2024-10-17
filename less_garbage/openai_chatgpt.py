from flask import Flask,request,jsonify
from gpt_bot import GPTBot
# from metaprompt.scene_analyzer import metaprompt as metaSA
from less_garbage.metaprompt.scene_analyzer2 import metaprompt as metaSA
#from metaprompt.code_instructor import metaprompt as metaCI
from metaprompt.code_instructon_body import metaprompt as metaCI
from metaprompt.code_generator import metaprompt as metaCG

app = Flask(__name__)
botcodeGenerator = GPTBot(role=metaCG, historyAmount=2)
bot1 = GPTBot()
botSceneAnalyzer = GPTBot(role=metaSA)
botCodeInstructor = GPTBot(role=metaCI)

@app.route("/chatgpt/codeGenerator",methods=["POST"])
def codeGenerator():
    prompt = request.json
    question = prompt["question"]

    response = botcodeGenerator.ask(question)
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