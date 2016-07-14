from flask import Flask, render_template, flash, request, url_for, redirect

from flask_misaka import Misaka

from contentmanagement import Content

from physicianlib import Phy

from publicationlib import Pub

TOPIC_DICT = Content()
user_name = "pmangalath"
PHY_DICT = Phy()
PUB_DICT = Pub()

app = Flask(__name__)

# adding markdown parser support: https://flask-misaka.readthedocs.io/en/latest/
Misaka(app)

@app.route("/", methods=['GET', 'POST'])
@app.route("/dashboard/", methods=['GET', 'POST'])
def main():
	return render_template('index.html', TOPIC_DICT = TOPIC_DICT, PHY_DICT = PHY_DICT, PUB_DICT = PUB_DICT)

# @app.route("/dashboard/")
# def dashboard():
# 	return render_template('dashboard.html', TOPIC_DICT = TOPIC_DICT)

# Paste the output of html_creator here

###datasets list here
@app.route("/datasets/prognosis-criteria-calculation", methods=['GET', 'POST'])
def Calculation_and_Criteria_for_Prognosis():
    return render_template("/datasets/prognosis-criteria-calculation.html", post_date = TOPIC_DICT["datasets"][0][0], post_title = TOPIC_DICT["datasets"][0][1], post_url = TOPIC_DICT["datasets"][0][2], user_name = user_name)




@app.route("/datasets/cdc-interactive-cancer-atlas", methods=['GET', 'POST'])
def CDC_Interactive_Cancer_Atlas():
    return render_template("/datasets/cdc-interactive-cancer-atlas.html", post_date = TOPIC_DICT["datasets"][1][0], post_title = TOPIC_DICT["datasets"][1][1], post_url = TOPIC_DICT["datasets"][1][2], user_name = user_name)




@app.route("/datasets/ncdb-participant-user-file", methods=['GET', 'POST'])
def NCDB_Cancer_Participant_User_Files():
    return render_template("/datasets/ncdb-participant-user-file.html", post_date = TOPIC_DICT["datasets"][2][0], post_title = TOPIC_DICT["datasets"][2][1], post_url = TOPIC_DICT["datasets"][2][2], user_name = user_name)




@app.route("/datasets/cancer-incidence-mortality-explained", methods=['GET', 'POST'])
def Cancer_Incidence_and_Mortality_Data_Explained():
    return render_template("/datasets/cancer-incidence-mortality-explained.html", post_date = TOPIC_DICT["datasets"][3][0], post_title = TOPIC_DICT["datasets"][3][1], post_url = TOPIC_DICT["datasets"][3][2], user_name = user_name)




@app.route("/datasets/seer", methods=['GET', 'POST'])
def SEER_Dataset():
    return render_template("/datasets/seer.html", post_date = TOPIC_DICT["datasets"][4][0], post_title = TOPIC_DICT["datasets"][4][1], post_url = TOPIC_DICT["datasets"][4][2], user_name = user_name)



###Publications list here

@app.route("/publications/multiplatform-analysis-of-12-cancer-types", methods=['GET', 'POST'])
def Multiplatform_Analysis_of_12_Cancer_Types_Reveals_Molecular_Classification_within_and_across_Tissues_of_Origin():
    return render_template("/publications/multiplatform-analysis-of-12-cancer-types.html", post_date = TOPIC_DICT["publications"][1][0], post_title = TOPIC_DICT["publications"][0][1], post_url = TOPIC_DICT["publications"][0][2], user_name = user_name)


###Media list here

@app.route("/media/sample1", methods=['GET', 'POST'])
def New_Promise_For_Immunotherapy_Cancer_Drugs():
    return render_template("/media/sample1.html", post_date = TOPIC_DICT["media"][0][0], post_title = TOPIC_DICT["media"][0][1], post_url = TOPIC_DICT["media"][0][2], user_name = user_name)

###Organizations list here

@app.route("/organizations/fastercures", methods=['GET', 'POST'])
def FasterCures():
    return render_template("/organizations/fastercures.html", post_date = TOPIC_DICT["organizations"][0][0], post_title = TOPIC_DICT["organizations"][0][1], post_url = TOPIC_DICT["organizations"][0][2], user_name = user_name)




@app.route("/organizations/2-PREVENT", methods=['GET', 'POST'])
def PREVENT_TCE_Breast_Cancer_Translational_Center_of_Excellence_at_UPENN():
    return render_template("/organizations/2-PREVENT.html", post_date = TOPIC_DICT["organizations"][1][0], post_title = TOPIC_DICT["organizations"][1][1], post_url = TOPIC_DICT["organizations"][1][2], user_name = user_name)




@app.route("/organizations/NBCC", methods=['GET', 'POST'])
def NBCC___National_Breast_Cancer_Coalition___2020_Deadline():
    return render_template("/organizations/NBCC.html", post_date = TOPIC_DICT["organizations"][2][0], post_title = TOPIC_DICT["organizations"][2][1], post_url = TOPIC_DICT["organizations"][2][2], user_name = user_name)




@app.route("/organizations/AANCART", methods=['GET', 'POST'])
def AANCART___The_Asian_American_Network_for_Cancer_Awareness_Research_and_Training():
    return render_template("/organizations/AANCART.html", post_date = TOPIC_DICT["organizations"][3][0], post_title = TOPIC_DICT["organizations"][3][1], post_url = TOPIC_DICT["organizations"][3][2], user_name = user_name)

# End of output from html_creator - select until this section

"""
@app.route("/publications/1/")
def pub_1():
	return render_template('/publications/multiplatform-analysis-of-12-cancer-types.html', user_name = user_name, post_date = TOPIC_DICT["Publications"][0][0], post_title = TOPIC_DICT["Publications"][0][1])
"""

@app.route("/login_page/", methods = ["GET","POST"])
def login():
	error = ''
	try:
		if request.method == "POST":
			u_name = request.form["username"]
			p_name = request.form["password"]

			#print(u_name)
			#print(p_name)

			if u_name == "admin" and p_name == "password":
				return redirect(url_for('dashboard'))
			else:
				error = "Invalid credentials"
		return render_template("login.html", error=error)
	except Exception as e:
		return render_template("login.html", error=error)

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html', error = e)

if __name__ == "__main__":
	app.run()