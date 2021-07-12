from flask import Flask, render_template, request

aplikasi = Flask(__name__)

@aplikasi.route("/")
def app():
    return render_template("belahketupat.html")

@aplikasi.route("/send", methods=["POST"])
def send(sum=sum):
    if request.method == "POST":
        belahketupat = request.form["belahketupat"]
        belahketupat2 = request.form["belahketupat2"]
        belahketupat3 = request.form["belahketupat3"]
        sum = float(belahketupat)
        sum2= float(belahketupat2)
        sum3 = float(belahketupat3)
        result = (0.5 * sum2 * sum3)
        result2 = sum * 4
        return render_template("belahketupat.html", sum=result, sum2=result2, sum3=sum2)
    else:
        return render_template("belahketupat.html")

if __name__ == '__main__':
    aplikasi.run(debug=True)
