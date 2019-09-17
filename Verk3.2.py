from flask import Flask
from flask import render_template as template
from flask import request
from flask import make_response

app = Flask(__name__, template_folder='views',static_folder='public/static') 

@app.route("/", methods=['GET', 'POST'])
def index():
    return """
     <p><a href="/a">Lidur 1</a></p> 
     <p><a href="/b">Lidur 2</a></p> """

@app.route("/a", methods=['GET', 'POST'])
def frettirA():
    return template("temp-A.tpl")

@app.route("/sida/<kt>", methods=['GET', 'POST'])
def page(kt):
  summa = 0
  for i in kt: 
    summa = summa + int(i)
  return template("temp-kt.tpl", summa=summa, kt=kt)

frettir = [["Irma veldur usla á Flórída", "Það er bara ... vesen á Irmu í Flórída.  Milljónir manna hafa þurft að yfirgefa heimili sin vegna yfirvofandi eyðileggingar Irmu...", "irma.jpg", "dsg@frettir.is"],
           ["Veiðin er dræm þetta haustið", "Veiðin hefur heldur verið döpur þetta haustið þrátt fyrir ágætis rigninar upp á síðkastið...", "veidi.png", "est@frettir.is"],
           ["Ólafía stendur sig vel", "Ólafía er komin í 65 sæti peningalistans og hefur því tryggt sér keppnisrétt á LPG mótaröðinni á komandi keppnistimabili...", "golf.jpeg", "htg@frettir.is"],
           ["Ísland dottið úr leik", "Íslenska karlalandsliðið í körfubolta er dottið úr leik a Eurobasket þrátt fyrir ágætis spretti inn a milli.  Ísland spilaði lokaleik sinn á mótinu fyrir troðfullri höll gegn heimamönnum Finnum..", "karfa.jpeg", "dsg@frettir.is"]]


@app.route("/static/<skra>", methods=['GET', 'POST'])
def statid_skra(skra):
    return static_file(skra, root="./static")

@app.route("/b", methods=['GET', 'POST'])
def indexTemplate():
    return template("index.tpl", frett = frettir)

@app.route("/frettir/", methods=['GET', 'POST'])
def frettirB():
    frettir = frett
    cnt = 0;
    i = 4;
    for i in frett:
      cnt += 1
    end
    return template("frettir.tpl", frett= frettir[id])

@app.errorhandler(404)
def villa(error):
    return"<h2 style='color:red'>This site cant be found aka 404</h2>"

if __name__ == '__main__':
  app.run(debug=True)