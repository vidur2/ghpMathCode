import sys
from flask import Flask, request
import smtpStuff
from afterResponse import AfterResponse

sys.path.insert(0, "../")
sys.path.insert(0, "../dcolor")

import dcolorUse

app = Flask(__name__)

@app.route('/get_plot', methods=["POST"])
def getPlot():
    data = request.form
    print(data)
    dcolorUse.calcRoots(float(data["endRange"]), float(data["interval"]))
    smtpStuff.sendMail(data["emailAddr"])
    return "Done"

if __name__ == "__main__":
    app.run(port=5001, threaded=True)

