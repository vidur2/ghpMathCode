import sys
from flask import Flask, request
import smtpStuff
from afterResponse import AfterResponse

sys.path.insert(0, "../")
sys.path.insert(0, "../dcolor")

import dcolorUse

app = Flask(__name__)
AfterResponse(app)

endRange = 0
interval = 0

@app.route('/get_plot', methods=["POST"])
def getPlot():
    data = request.form
    global endRange
    global interval
    endRange = data["endRange"]
    interval = data["interval"]
    return "Done"

@app.after_response
def runDcolor():
    dcolorUse.calcRoots(data["endRange"], data["interval"])
    smtpStuff.sendEmail(data["emailAddr"])

if __name__ == "__main__":
    app.run(port=5001)

