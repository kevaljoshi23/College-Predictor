import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model1 = pickle.load(open('model1.pkl', 'rb'))
model2 = pickle.load(open('model2.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/msform')
def msform():
    return render_template('msform.html')

@app.route('/collegeform')
def collegeform():
    return render_template('collegeform.html')

@app.route('/contactus')
def contactus():
    return render_template('contactus.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/university')
def university():
    return render_template('university.html')

@app.route('/5star')
def star5():
    return render_template('5star.html')

@app.route('/4star')
def star4():
    return render_template('4star.html')

@app.route('/3star')
def star3():
    return render_template('3star.html')

@app.route('/2star')
def star2():
    return render_template('2star.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    c = model1.predict(final_features)

    l=int(c)
    o=round(l)
    if o==8:
        return render_template('collegeform.html', prediction_text='College is : IIT BOMBAY')
    if o==10:
        return render_template('collegeform.html', prediction_text='College is : IIT DELHI')
    if o==17:
        return render_template('collegeform.html', prediction_text='College is : IIT KANPUR')
    if o==18:
        return render_template('collegeform.html', prediction_text='College is : IIT KHARAGPUR')
    if o==12:
        return render_template('collegeform.html', prediction_text='College is : IIT GUWAHATI')
    if o==13:
        return render_template('collegeform.html', prediction_text='College is : IIT HYDRABAD')
    if o==32:
        return render_template('collegeform.html', prediction_text='College is : Netaji Subhash IT')
    if o==29:
        return render_template('collegeform.html', prediction_text='College is : NIT TRICHY')
    if o==14:
        return render_template('collegeform.html', prediction_text='College is : IIT INDORE')
    if o==2:
        return render_template('collegeform.html', prediction_text='College is : BITS PILLANI')
    if o==23:
        return render_template('collegeform.html', prediction_text='College is : JADAVPUR UNIVERSITY')
    if o==37:
        return render_template('collegeform.html', prediction_text='College is : VIT VELLORE')
    if o==4:
        return render_template('collegeform.html', prediction_text='College is : DTU DELHI')
    if o==21:
        return render_template('collegeform.html', prediction_text='College is : IIT ROPAR')
    if o==19:
        return render_template('collegeform.html', prediction_text='College is : IIT MANDI')
    if o==7:
        return render_template('collegeform.html', prediction_text='College is : IIIT HYDRABAD')
    if o==30:
        return render_template('collegeform.html', prediction_text='College is : NIT WARANGAL')
    if o==22:
        return render_template('collegeform.html', prediction_text='College is : IIT TIRUPATI')
    if o==5:
        return render_template('collegeform.html', prediction_text='College is : HBU KANPUR')
    if o==26:
        return render_template('collegeform.html', prediction_text='College is : MNNIT ALLAHABAD')
    if o==11:
        return render_template('collegeform.html', prediction_text='College is : IIT GOA')
    if o==28:
        return render_template('collegeform.html', prediction_text='College is : MANIPAL IT')
    if o==20:
        return render_template('collegeform.html', prediction_text='College is : IIT PALAKKAD')
    if o==0:
        return render_template('collegeform.html', prediction_text='College is : AHEMEDABAD IT')
    if o==33:
        return render_template('collegeform.html', prediction_text='College is : SOA UNIVERSITY')
    if o==34:
        return render_template('collegeform.html', prediction_text='College is : SRM CHENNAI')
    if o==9:
        return render_template('collegeform.html', prediction_text='College is : IIT BHILLAI')
    if o==15:
        return render_template('collegeform.html', prediction_text='College is : IIT JAMMU')
    if o==31:
        return render_template('collegeform.html', prediction_text='College is : NMIMS')
    if o==16:
        return render_template('collegeform.html', prediction_text='College is : IIT JODHPUR')
    if o==35:
        return render_template('collegeform.html', prediction_text='College is : SSN COLLEGE OF ENGG')
    if o==6:
        return render_template('collegeform.html', prediction_text='College is : IIEST SHIBPUR')
    if o==24:
        return render_template('collegeform.html', prediction_text='College is : KLEF HYDRABAD')
    if o==36:
        return render_template('collegeform.html', prediction_text='College is : UNIVERSITY COLLEGE OF ENGG')
    if o==1:
        return render_template('collegeform.html', prediction_text='College is : BIT MESRA')
    if o==25:
        return render_template('collegeform.html', prediction_text='College is : MNIT JAIPUR')
    if o==3:
        return render_template('collegeform.html', prediction_text='College is : BMS COLLEGE OF ENGG')
    if o==27:
        return render_template('collegeform.html', prediction_text='College is : MSIT')
    
@app.route('/predictms',methods=['POST'])
def predictms():
    '''
    For rendering results on HTML GUI
    '''
    l = [float(i) for i in request.form.values()]
    u = [np.array(l)]
    a = model2.predict(u)
    return render_template('msform.html', prediction_text="Chances of Admit is : {}".format(a))
    
    
    
@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    c = model1.predict([np.array(list(data.values()))])
    l=int(c)
    o=round(l)

    return jsonify(o)

@app.route('/predict_api_ms',methods=['POST'])
def predict_api_ms():
    '''
    For direct API calls trought request
    '''
    data1 = request.get_json(force=True)
    d = model2.predict([np.array(list(data1.values()))])
    return jsonify(d)


if __name__ == "__main__":
    app.run(debug=True)



