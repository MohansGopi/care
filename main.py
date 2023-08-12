from flask import Flask,render_template,request,redirect,flash
import json
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

app.secret_key = "super secret key"


is_logged = False

@app.route("/")
def main():
    return render_template('index.html')

# next are the submission area of all the dept

# engineering sym system

@app.route("/eng_sym_upload")
def eng_sym_upload():
    return render_template('engineering+sym+upload.html')


# arts sym sys

@app.route("/art_sym_upload")
def art_sym_upload():
    return render_template('arts+science+sym+upload.html')


#arche sym sys

@app.route("/arch_sym_upload")
def arch_sym_upload():
    return render_template('arch+sym+upload.html')

# server for both blogs

@app.route("/campus_event")
def campus_event():
    webcode = ''

    for n in range(1, 28):
        response = requests.get(url=f"https://care.ac.in/engineering/category/engineering-events/page/{n}")

        webcode += response.text

    soup = BeautifulSoup(webcode, "html.parser")

    content = soup.find_all(class_="entry-title")

    titles = []

    for tag in content:
        titles.append(tag.getText())


    para = soup.find_all(class_="entry-content")

    cont = []

    for tag in para:
        cont.append(tag.getText())
    date = soup.find_all(class_="entry-date")

    dates = []

    for tag in date:
        dates.append(tag.getText())

    soup = BeautifulSoup(webcode, "html.parser")

    date = soup.find_all(class_="Thumbnail thumbnail loop")

    images = []

    for tag in date:
        images.append(tag['src'])

    date = soup.find_all(class_="entry-title")

    links = []

    for tag in date:
        links.append(tag.a['href'])

    return render_template('campus_event.html', title=titles,content=cont ,len=len(titles),dates= dates,images=images,links=links)

@app.route("/campus_symposium")
def campus_symposium():
    return render_template("campus_symposium.html")

# login credentials for all the dept

@app.route("/login")
def login():
    global is_logged
    is_logged = False
    return render_template("login.html")

# admin verification

is_eng_logged = False
is_arts_logged = False
is_arche_logged = False

@app.route("/login",methods=['POST'])
def verify():
    global is_logged
    user_name = request.form['user_name']
    passwd = request.form['passwd']
    with open("static/adim_credential.json") as datafile:
        data = json.load(datafile)
        eng_data_user = data['users']['Eng']
        arts_data_user = data['users']['Arts']
        arche_data_user = data['users']['Arche']
    eng_user_list = [data for data in eng_data_user]
    arts_user_list = [data for data in arts_data_user]
    arche_user_list = [data for data in arche_data_user]

    if user_name in eng_user_list and passwd == eng_data_user[user_name]:
        global is_eng_logged
        is_eng_logged = True
        return redirect("/eng_admin")
    elif user_name in arts_user_list and passwd == arts_data_user[user_name]:
        global is_arts_logged
        is_arts_logged = True
        return redirect("/Arts_admin")
    elif user_name in arche_user_list and passwd == arche_data_user[user_name]:
        global is_arche_logged
        is_arche_logged = True
        return redirect("/Arche_admin")
    else:
        flash(message="Invalid Input")
        return redirect("/")


@app.route("/input_eng" , methods=['POST'])
def input_eng():
    name = request.form['stu_name']
    rag_no = request.form['register_no']
    det = request.form['dept']
    cur_year = request.form['cur_year']
    clg_name = request.form['clg_name']
    eve_name = request.form['eve_name']
    eve_date = request.form['eve_date']
    stu_pos_in_eve = request.form['stu-pos_in_eve']
    with open("static/engineering/eng_data.csv", 'a') as datafile:
        datafile.write(f"\n{name},{rag_no},{det},{cur_year},{clg_name},{eve_name},{eve_date},{stu_pos_in_eve}")
    import json
    import pandas as pd
    if det == 'B.tech AI&DS':
        with open("static/engineering/btech_ai&ds/btech_ai&ds.csv", 'a') as datafile:
            datafile.write(f"\n{name},{rag_no},{det},{cur_year},{clg_name},{eve_name},{eve_date},{stu_pos_in_eve}")
        df = pd.read_csv("static/engineering/btech_ai&ds/btech_ai&ds.csv")
        data = df.to_dict()
        with open("static/engineering/btech_ai&ds/btech_ai&ds.json",'w') as data_file:
            json.dump(data, data_file, indent=4)

    elif det == 'B.E CSE':
        with open("static/engineering/be_cse/be_cse.csv", 'a') as datafile:
            datafile.write(f"\n{name},{rag_no},{det},{cur_year},{clg_name},{eve_name},{eve_date},{stu_pos_in_eve}")
        df = pd.read_csv("static/engineering/be_cse/be_cse.csv")
        data = df.to_dict()
        with open("static/engineering/be_cse/be_cse.json",'w') as data_file:
            json.dump(data, data_file, indent=4)

    elif det == 'B.E Mechanical':
        with open("static/engineering/be_mech/be_mech.csv", 'a') as datafile:
            datafile.write(f"\n{name},{rag_no},{det},{cur_year},{clg_name},{eve_name},{eve_date},{stu_pos_in_eve}")
        df = pd.read_csv("static/engineering/be_mech/be_mech.csv")
        data = df.to_dict()
        with open("static/engineering/be_mech/be_mech.json", 'w') as data_file:
            json.dump(data, data_file, indent=4)

    elif det == 'B.E ECE':
        with open("static/engineering/be_ece/be_ece.csv", 'a') as datafile:
            datafile.write(f"\n{name},{rag_no},{det},{cur_year},{clg_name},{eve_name},{eve_date},{stu_pos_in_eve}")
        df = pd.read_csv("static/engineering/be_ece/be_ece.csv")
        data = df.to_dict()
        with open("static/engineering/be_ece/be_ece.json", 'w') as data_file:
            json.dump(data, data_file, indent=4)

    elif det == 'B.E Civil':
        with open("static/engineering/be_civil/be_civil.csv", 'a') as datafile:
            datafile.write(f"\n{name},{rag_no},{det},{cur_year},{clg_name},{eve_name},{eve_date},{stu_pos_in_eve}")
        df = pd.read_csv("static/engineering/be_civil/be_civil.csv")
        data = df.to_dict()
        with open("static/engineering/be_civil/be_civil.json", 'w') as data_file:
            json.dump(data, data_file, indent=4)

    elif det == 'M.E CSE(AI&ML)':
        with open("static/engineering/me_cse_ai&ml/me_cse_ai&ds.csv", 'a') as datafile:
            datafile.write(f"\n{name},{rag_no},{det},{cur_year},{clg_name},{eve_name},{eve_date},{stu_pos_in_eve}")
        df = pd.read_csv("static/engineering/me_cse_ai&ml/me_cse_ai&ds.csv")
        data = df.to_dict()
        with open("static/engineering/me_cse_ai&ml/me_cse_ai&ds.json", 'w') as data_file:
            json.dump(data, data_file, indent=4)

    elif det == 'M.E Construction and Management':
        with open("static/engineering/me_construction_eng_managment/me_contruct.csv", 'a') as datafile:
            datafile.write(f"\n{name},{rag_no},{det},{cur_year},{clg_name},{eve_name},{eve_date},{stu_pos_in_eve}")
        df = pd.read_csv("static/engineering/me_construction_eng_managment/me_contruct.csv")
        data = df.to_dict()
        with open("static/engineering/me_construction_eng_managment/me_contruct.json", 'w') as data_file:
            json.dump(data, data_file, indent=4)

    elif det == 'M.E Computer Design':
        with open("static/engineering/me_cd/me_cd.csv", 'a') as datafile:
            datafile.write(f"\n{name},{rag_no},{det},{cur_year},{clg_name},{eve_name},{eve_date},{stu_pos_in_eve}")
        df = pd.read_csv("static/engineering/me_cd/me_cd.csv")
        data = df.to_dict()
        with open("static/engineering/me_cd/me_cd.json", 'w') as data_file:
            json.dump(data, data_file, indent=4)

    elif det == 'MBA':
        with open("static/engineering/mba/mba.csv", 'a') as datafile:
            datafile.write(f"\n{name},{rag_no},{det},{cur_year},{clg_name},{eve_name},{eve_date},{stu_pos_in_eve}")
        df = pd.read_csv("static/engineering/mba/mba.csv")
        data = df.to_dict()
        with open("static/engineering/mba/mba.json", 'w') as data_file:
            json.dump(data, data_file, indent=4)

    return redirect("/")


@app.route("/B.tech_ai+ds")
def  B_tech_ai_ds():
    if is_eng_logged:
        Name = "B.TECH AI&DS"
        with open("static/engineering/btech_ai&ds/btech_ai&ds.json") as data_file:
            data = json.load(data_file)
        return  render_template("eng_data_tables_all_dept.html",name = Name,data = data)
    else:
        return redirect("/login")

@app.route("/BE_cse")
def  BE_cse():
    if is_eng_logged:
        with open("static/engineering/be_cse/be_cse.json") as data_file:
            data = json.load(data_file)
        Name = "B.E CSE"
        return  render_template("eng_data_tables_all_dept.html",name = Name,data=data)
    else:
        return redirect("/login")

@app.route("/BE_ece")
def  BE_ece():
    if is_eng_logged:
        Name = "B.E ECE"
        with open("static/engineering/be_ece/be_ece.json") as data_file:
            data = json.load(data_file)
        return  render_template("eng_data_tables_all_dept.html",name = Name,data=data)
    else:
        return redirect("/login")

@app.route("/BE_mech")
def  BE_mech():
    if is_eng_logged:
        Name = "B.E MECH"
        with open("static/engineering/be_mech/be_mech.json") as data_file:
            data = json.load(data_file)
        return  render_template("eng_data_tables_all_dept.html",name = Name,data=data)
    else:
        return redirect("/login")

@app.route("/MBA")
def MBA():
    if is_eng_logged:
        Name = "MBA"
        with open("static/engineering/mba/mba.json") as data_file:
            data = json.load(data_file)
        return  render_template("eng_data_tables_all_dept.html",name = Name,data=data)
    else:
        return redirect("/login")

@app.route("/ME_cd")
def  ME_cd():
    if is_eng_logged:
        Name = "M.E COMPUTER DESIGN"
        with open("static/engineering/me_cd/me_cd.json") as data_file:
            data = json.load(data_file)
        return  render_template("eng_data_tables_all_dept.html",name = Name,data=data)
    else:
        return redirect("/login")

@app.route("/ME_construction_eng_manage")
def  ME_construction_eng_manage():
    if is_eng_logged:
        Name = "M.E CONSTRUCTION ENG AND MANAGEMENT"
        with open("static/engineering/me_construction_eng_managment/me_contruct.json") as data_file:
            data = json.load(data_file)
        return  render_template("eng_data_tables_all_dept.html",name = Name,data=data)
    else:
        return redirect("/login")

@app.route("/ME_cse_ai_ml")
def  ME_cse_ai_ml():
    if is_eng_logged:
        Name = "M.E CSE(AI&ML)"
        with open("static/engineering/me_cse_ai&ml/me_cse_ai&ds.json") as data_file:
            data = json.load(data_file)
        return  render_template("eng_data_tables_all_dept.html",name = Name,data=data)
    else:
        return redirect("/login")

@app.route("/BE_civil")
def BE_civil():
    if is_eng_logged:
        Name = "B.E CIVIL"
        with open("static/engineering/be_civil/be_civil.json") as data_file:
            data = json.load(data_file)
        return  render_template("eng_data_tables_all_dept.html",name = Name,data=data)
    else:
        return redirect("/login")


# Arts input and its data management......

@app.route("/arts_input",methods=['POST'])
def arts_input():
    name = request.form['stu_name']
    rag_no = request.form['register_no']
    det = request.form['dept']
    cur_year = request.form['cur_year']
    clg_name = request.form['clg_name']
    eve_name = request.form['eve_name']
    eve_date = request.form['eve_date']
    stu_pos_in_eve = request.form['stu-pos_in_eve']
    with open("static/arts/arts_data.csv", 'a') as datafile:
        datafile.write(f"\n{name},{rag_no},{det},{cur_year},{clg_name},{eve_name},{eve_date},{stu_pos_in_eve}")
    import json
    import pandas as pd


    if det == "B.Sc. Interior Design":
        with open("static/arts/B.Sc. Interior Design/b_sc_interior_design.csv", 'a') as datafile:
            datafile.write(f"\n{name},{rag_no},{det},{cur_year},{clg_name},{eve_name},{eve_date},{stu_pos_in_eve}")

        df = pd.read_csv("static/arts/B.Sc. Interior Design/b_sc_interior_design.csv")
        data = df.to_dict()

        with open("static/arts/B.Sc. Interior Design/b_sc_interior_design.json", 'w') as data_file:
            json.dump(data, data_file, indent=4)

    elif det == "B.Sc Visual Communication":
        with open("static/arts/B.Sc Visual Communication/b_sc_visual_communication.csv", 'a') as datafile:
            datafile.write(f"\n{name},{rag_no},{det},{cur_year},{clg_name},{eve_name},{eve_date},{stu_pos_in_eve}")

        df = pd.read_csv("static/arts/B.Sc Visual Communication/b_sc_visual_communication.csv")
        data = df.to_dict()

        with open("static/arts/B.Sc Visual Communication/b_sc_visual_communication.json", 'w') as data_file:
            json.dump(data, data_file, indent=4)

    elif det == "B.Com":
        with open("static/arts/B.Com/b_com.csv", 'a') as datafile:
            datafile.write(f"\n{name},{rag_no},{det},{cur_year},{clg_name},{eve_name},{eve_date},{stu_pos_in_eve}")

        df = pd.read_csv("static/arts/B.Com/b_com.csv")
        data = df.to_dict()

        with open("static/arts/B.Com/b_com.json", 'w') as data_file:
            json.dump(data, data_file, indent=4)

    elif det == "B.Com CA":
        with open("static/arts/B.Com CA/b_com_ca.csv", 'a') as datafile:
            datafile.write(f"\n{name},{rag_no},{det},{cur_year},{clg_name},{eve_name},{eve_date},{stu_pos_in_eve}")

        df = pd.read_csv("static/arts/B.Com CA/b_com_ca.csv")
        data = df.to_dict()

        with open("static/arts/B.Com CA/b_com_ca.json", 'w') as data_file:
            json.dump(data, data_file, indent=4)

    elif det == "BBA":
        with open("static/arts/BBA/bba.csv", 'a') as datafile:
            datafile.write(f"\n{name},{rag_no},{det},{cur_year},{clg_name},{eve_name},{eve_date},{stu_pos_in_eve}")

        df = pd.read_csv("static/arts/BBA/bba.csv")
        data = df.to_dict()

        with open("static/arts/BBA/bba.json", 'w') as data_file:
            json.dump(data, data_file, indent=4)

    return redirect("/")

@app.route("/B_Com")
def B_Com():
    if is_arts_logged:
        name = 'B.COM'
        with open("static/arts/B.Com/b_com.json") as data_file:
            data = json.load(data_file)
        return render_template("arts_data_tables_all_dept.html",name=name,data=data)
    else:
        return redirect("/login")

@app.route("/B_Com_CA")
def B_Com_CA():
    if is_arts_logged:
        name = 'B.COM.CA'
        with open("static/arts/B.Com CA/b_com_ca.json") as data_file:
            data = json.load(data_file)
        return render_template("arts_data_tables_all_dept.html",name=name,data=data)
    else:
        return redirect("/login")

@app.route("/B_Sc_Interior_design")
def B_Sc_Interior_design():
    if is_arts_logged:
        name = 'B.Sc.Interior Design'
        with open("static/arts/B.Sc. Interior Design/b_sc_interior_design.json") as data_file:
            data = json.load(data_file)
        return render_template("arts_data_tables_all_dept.html",name=name,data=data)
    else:
        return redirect("/login")

@app.route("/B_Sc_Visual_Communication")
def B_Sc_Visual_Communication():
    if is_arts_logged:
        name = 'B.Sc.Visual Communication'
        with open("static/arts/B.Sc Visual Communication/b_sc_visual_communication.json") as data_file:
            data = json.load(data_file)
        return render_template("arts_data_tables_all_dept.html",name=name,data=data)
    else:
        return redirect("/login")

@app.route("/BBA")
def BBA():
    if is_arts_logged:
        name = 'BBA'
        with open("static/arts/BBA/bba.json") as data_file:
            data = json.load(data_file)
        return render_template("arts_data_tables_all_dept.html",name=name,data=data)
    else:
        return redirect("/login")



# All admin management.....

@app.route("/eng_admin")
def eng_admin():
    if is_eng_logged:
        return render_template("Eng_sympo_document.html")
    else:
        return redirect("/login")



@app.route("/Arts_admin")
def arts_admin():
    if is_arts_logged:
        return render_template("arts_sympo_document.html")
    else:
        return redirect("/login")


@app.route("/Arche_admin")
def arche_admin():
    if is_arche_logged:
        return 'hello'
    else:
        return redirect("/login")

if __name__=="__main__":
    app.run(debug=True)