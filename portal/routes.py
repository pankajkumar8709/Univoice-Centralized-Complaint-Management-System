from flask import render_template,request,redirect,url_for,flash,session
from portal import app,teachers,admins,students,db,engine
from sqlalchemy import select
from portal.models import acad,mess,hostel,sports,s_anonymous,s_suggest,basic,buses,T_Anonymous,T_Complaints,T_Suggestion

import json
from flask import jsonify

from datetime import datetime
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/index')
def index():
    return render_template('index.html')

# Student login
@app.route('/student_login', methods=['GET', 'POST'])
def s_login():
    if request.method == 'POST':
        roll = request.form['roll']
        password = request.form['password']

        with engine.connect() as conn:
            query = select(students).where(students.c.roll_number == roll)
            result = conn.execute(query).fetchone()

            if result:
                db_password = result[1]  # 2nd column = password
                name = result[2]         # 3rd column = name

                if password == db_password:
                    session['name'] = name   # ✅ store in session['name']
                    session['roll'] = roll   # optional
                    flash("✅ Login successful")
                    return redirect(url_for('s_interface'))  # redirect to interface
                else:
                    flash("❌ Incorrect password")
            else:
                flash("❌ Roll number not found")

    return render_template('s_login.html')


# Student interface/dashboard
@app.route('/student', methods=['GET', 'POST'])
def s_interface():
    name = session.get('name')
    if not name:
        flash("Please login first.")
        return redirect(url_for('s_login'))

    return render_template('s_interface.html', name=name)


# Logout
@app.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out.")
    return redirect(url_for('index'))


@app.route('/academics',methods=['GET','POST'])
def acad_page():
    return render_template('acad.html')

@app.route('/submit_academic_complaint',methods=['GET','POST'])
def a_add():
    if request.method=='POST':
        complaint=request.form['complaint']
        semester=request.form['semester']
        course=request.form['course']
        section=request.form['section']
        date=request.form['date']

        date_obj = datetime.strptime(date, '%Y-%m-%d').date()




        a1=acad(complaint=complaint,semester=semester,course=course,section=section,date=date_obj)

        db.session.add(a1)
        db.session.commit()
        flash("Form submitted succesfully",category='success')
        return redirect(url_for('acad_page'))

@app.route('/hostel',methods=['GET','POST'])
def hostel_page():
    return render_template('hostel.html')
@app.route('/submit_hostel_complaint',methods=['POST'])
def h_add():
    complaint=request.form['complaint']
    h_no=request.form['hostel']
    r_no=request.form['room']
    date=request.form['date']

    date_obj = datetime.strptime(date, '%Y-%m-%d').date()

    h1=hostel(complaint=complaint,hostel_no=h_no,room_no=r_no,date=date_obj)
    db.session.add(h1)
    db.session.commit()
    flash("Form Submitted successfully",category='success')
    return redirect(url_for('hostel_page'))

@app.route('/mess',methods=['GET','POST'])
def mess_page():
    return render_template('mess.html')

@app.route('/submit_mess_complaint',methods=['POST'])
def m_add():
    complaint=request.form['complaint']
    day=request.form['day']
    meal=request.form['meal']
    date=request.form['date']

    date_obj = datetime.strptime(date, '%Y-%m-%d').date()



    m1=mess(complaint=complaint,day=day,meal=meal,date=date_obj)
    db.session.add(m1)
    db.session.commit()

    flash("Form Submitted successfully",category='success')
    return redirect(url_for('mess_page'))

@app.route('/sports',methods=['GET','POST'])
def sports_page():
    return render_template('sports.html')

@app.route('/submit_sports_complaint',methods=['POST'])
def sp_add():
    complaint=request.form['complaint']
    t_sport=request.form['sport']
    date=request.form['date']

    date_obj = datetime.strptime(date, '%Y-%m-%d').date()

    sp1=sports(complaint=complaint,type=t_sport,date=date_obj)
    db.session.add(sp1)
    db.session.commit()
    flash("form submitted successfully",category='success')
    return redirect(url_for('sports_page'))

@app.route('/buses',methods=['GET','POST'])
def buses_page():
    return render_template('buses.html')

@app.route('/submit_bus_complaint',methods=['POST'])
def b_add():
    complaint=request.form['complaint']
    b_no=request.form['bus']
    date=request.form['date']
    date_obj = datetime.strptime(date, '%Y-%m-%d').date()

    b1=buses(complaint=complaint,bus_no=b_no,date=date_obj)
    db.session.add(b1)
    db.session.commit()
    flash("form submitted successfully",category='success')
    return redirect(url_for('buses_page'))

@app.route('/basics',methods=['GET','POST'])
def basics_page():
    return render_template('basics.html')

@app.route('/submit_amenities_complaint',methods=['POST'])
def bs_add():
    complaint=request.form['complaint']
    category=request.form['category']
    date=request.form['date']
    date_obj = datetime.strptime(date, '%Y-%m-%d').date()

    ba1=basic(complaint=complaint,category=category,date=date_obj)
    db.session.add(ba1)
    db.session.commit()
    flash("form submitted successfully",category='success')
    return redirect(url_for('basics_page'))

@app.route('/anonymous',methods=['GET','POST'])
def anonymous_page():
    return render_template('anonymous.html')

@app.route('/submit_anonymous_complaint',methods=['POST'])
def an_add():
    complaint=request.form['complaint']
    category=request.form['category']
    date=request.form['date']
    date_obj = datetime.strptime(date, '%Y-%m-%d').date()

    an1=s_anonymous(complaint=complaint,category=category,date=date_obj)
    db.session.add(an1)
    db.session.commit()
    flash("form submitted successfully",category='success')
    return redirect(url_for('basics_page'))

@app.route('/suggest',methods=['GET','POST'])
def suggestion_page():
    return render_template('suggestion.html') 

@app.route('/submit_suggestion',methods=['POST'])
def sg_add():
    suggestion=request.form['suggestion']
    date=request.form['date']
    date_obj = datetime.strptime(date, '%Y-%m-%d').date()

    sg1=s_suggest(suggestion=suggestion,date=date_obj)
    db.session.add(sg1)
    db.session.commit()
    flash("form submitted successfully",category='success')
    return redirect(url_for('suggestion_page'))

@app.route('/view_complaints')
def view_complaint():
    complaints=acad.query.all()
    hostels=hostel.query.all()
    mes=mess.query.all()
    sp=sports.query.all()
    bs=buses.query.all()
    sg=s_suggest.query.all()
    an=s_anonymous.query.all()
    bas=basic.query.all()

    return render_template('s_complaints.html',complaints=complaints,hostels=hostels,mes=mes,sp=sp,bs=bs,sg=sg,an=an,bas=bas)



#teacher login
@app.route('/teacher_login', methods=['GET', 'POST'])
def t_login():
    if request.method == 'POST':
        empid = request.form['empid']
        password = request.form['password']

        with engine.connect() as conn:
            query = select(teachers).where(teachers.c.employee_id == empid)
            result = conn.execute(query).fetchone()

            if result:
                db_password = result[1]  # Assuming 2nd column is password
                name = result[2]         # Assuming 3rd column is name

                if password == db_password:
                    session['user'] = name
                    return render_template('t_interface.html')
                else:
                    flash("Invalid password")
            else:
                flash("Employee ID not found")

    return render_template('t_login.html')

@app.route('/t_interface',methods=['GET','POST'])
def t_interface():
    name=session.get('user')
    return render_template('t_interface.html',name=name)

@app.route('/t_complaint',methods=['GET','POST'])
def t_complaint():
    return render_template('t_complaint.html')
@app.route('/t_anonymous',methods=['GET','POST'])
def t_anonymous():
    return render_template('t_anonymous.html')
@app.route('/t_suggestion',methods=['GET','POST'])
def t_suggestion():
    return render_template('t_suggest.html')
@app.route('/t_view',methods=['GET','POST'])
def t_view_page():
    

    complaints=T_Complaints.query.all()
    suggest=T_Suggestion.query.all()
    anonymous=T_Anonymous.query.all()


    return render_template('t_view_complaints.html',complaints=complaints,suggestion=suggest,anonymous=anonymous)



@app.route('/submit_teacher_complaint',methods=['POST'])
def submit_t_complaints():
    title=request.form['title']
    desc=request.form['details']
    category=request.form['category']
    date=request.form['date']
    others=request.form['others']

    date_obj=datetime.strptime(date,'%Y-%m-%d').date()
    st1=T_Complaints(title=title,complaint=desc,category=category,date=date_obj,others=others)
    db.session.add(st1)
    db.session.commit()

    flash("Form Submitted Successfully",category='success')
    return redirect(url_for('t_complaint'))

@app.route('/submit_teacher_suggestion',methods=['POST'])
def submit_t_suggest():
    title=request.form['title']
    category=request.form['category']
    desc=request.form['details']
    date=request.form['date']

    date_obj=datetime.strptime(date,'%Y-%m-%d').date()
    st1=T_Suggestion(title=title,category=category,complaint=desc,date=date_obj)
    db.session.add(st1)
    db.session.commit()

    flash("Form Submitted Successfully",category='success')
    return redirect(url_for('t_suggestion'))

@app.route('/submit_anonymous_teacher',methods=['POST'])
def submit_t_anonymous():
    category=request.form['category']
    desc=request.form['details']
    st1=T_Anonymous(category=category,complaint=desc)
    db.session.add(st1)
    db.session.commit()

    flash("Form Submitted Successfully",category='success')
    return redirect(url_for('t_anonymous'))

#admin login
@app.route('/admin_login',methods=['GET','POST'])
def admin_login():
    if request.method=='POST':
        userid=request.form['username']
        password=request.form['password']

        with engine.connect() as conn:
            query=select(admins).where(admins.c.admin_id==userid)
            result=conn.execute(query).fetchone()

            if result:
                db_password=result[1]
                name=result[2]
                category=result[3]

                if password==db_password:
                    session['user']=name
                    session['category']=category
                    if category=='Hostel':
                        flash("✅ Login successful",category='success')
                        return redirect(url_for('admin_h_complaints'))
                    elif category=='Sports':
                        flash("✅ Login successful",category='success')
                        return redirect(url_for('admin_sp_complaints'))
                    elif category=='Bus':
                        flash("✅ Login successful",category='success')
                        return redirect(url_for('admin_bus_complaints'))
                    elif category=='Mess':
                        flash("✅ Login successful",category='success')
                        return redirect(url_for('admin_m_complaints'))
                    elif category=='Academics':
                        flash("✅ Login successful",category='success')
                        return redirect(url_for('admin_a_complaints'))
                    elif category=='Basic Amenities':
                        flash("✅ Login successful",category='success')
                        return redirect(url_for('admin_bas_complaints'))
                    elif category=='Officials':
                        flash("✅ Login successful",category='success')
                        return redirect(url_for('view_admin_complaint'))
                    else:
                        flash("Anauthorised Access!!!!!!",category='Danger')
                    
                else:
                    flash("Invalid Password")
            else:
                flash("Admin Id not found !!!!",category='Danger')

    return render_template('admin_login.html')

@app.route('/admin_a_complaints', methods=['GET', 'POST'])
def admin_a_complaints():
    name = session.get('user')
    category = session.get('category')

    if request.method == 'POST':
        complaint_id = request.form.get('complaint_id')
        new_status = request.form.get('status')
        response_text = request.form.get('response')

        complaint = acad.query.get(complaint_id)
        if complaint:
            complaint.status = new_status
            complaint.response = response_text

            # Set date_resolved only when marked as resolved
            if new_status.lower() == 'resolved':
                complaint.date_resolved = datetime.now()
            else:
                complaint.date_resolved = None

            db.session.commit()

    complaints = acad.query.all()
    return render_template('ad_ac_inter.html', complaints=complaints, name=name, category=category)





@app.route('/admin_h_complaints')
def admin_h_complaints():
    name = session.get('user')
    category=session.get('category')

    if request.method == 'POST':
        complaint_id = request.form.get('complaint_id')
        new_status = request.form.get('status')
        response_text = request.form.get('response')

        complaint = hostel.query.get(complaint_id)
        if complaint:
            complaint.status = new_status
            complaint.response = response_text

            # Set date_resolved only when marked as resolved
            if new_status.lower() == 'resolved':
                complaint.date_resolved = datetime.now()
            else:
                complaint.date_resolved = None

            db.session.commit()
    complaints=hostel.query.all()
    return render_template('ad_h_inter.html',complaints=complaints,name=name,category=category)

@app.route('/admin_m_complaints')
def admin_m_complaints():
    name = session.get('user')
    category=session.get('category')

    if request.method == 'POST':
        complaint_id = request.form.get('complaint_id')
        new_status = request.form.get('status')
        response_text = request.form.get('response')

        complaint = mess.query.get(complaint_id)
        if complaint:
            complaint.status = new_status
            complaint.response = response_text

            # Set date_resolved only when marked as resolved
            if new_status.lower() == 'resolved':
                complaint.date_resolved = datetime.now()
            else:
                complaint.date_resolved = None

            db.session.commit()
    complaints=mess.query.all()
    return render_template('ad_mes_inter.html',complaints=complaints,name=name,category=category)

@app.route('/admin_sp_complaints')
def admin_sp_complaints():
    name = session.get('user')
    category=session.get('category')

    if request.method == 'POST':
        complaint_id = request.form.get('complaint_id')
        new_status = request.form.get('status')
        response_text = request.form.get('response')

        complaint = sports.query.get(complaint_id)
        if complaint:
            complaint.status = new_status
            complaint.response = response_text

            # Set date_resolved only when marked as resolved
            if new_status.lower() == 'resolved':
                complaint.date_resolved = datetime.now()
            else:
                complaint.date_resolved = None

            db.session.commit()
    
    complaints=sports.query.all()
    return render_template('ad_spo_inter.html',complaints=complaints,name=name,category=category)

@app.route('/admin_bas_complaints')
def admin_bas_complaints():
    name = session.get('user')
    category=session.get('category')

    if request.method == 'POST':
        complaint_id = request.form.get('complaint_id')
        new_status = request.form.get('status')
        response_text = request.form.get('response')

        complaint = basic.query.get(complaint_id)
        if complaint:
            complaint.status = new_status
            complaint.response = response_text

            # Set date_resolved only when marked as resolved
            if new_status.lower() == 'resolved':
                complaint.date_resolved = datetime.now()
            else:
                complaint.date_resolved = None

            db.session.commit()

    complaints=basic.query.all()
    return render_template('ad_bas_inter.html',complaints=complaints,name=name,category=category)

@app.route('/admin_bus_complaints')
def admin_bus_complaints():
    name = session.get('user')
    category=session.get('category')

    if request.method == 'POST':
        complaint_id = request.form.get('complaint_id')
        new_status = request.form.get('status')
        response_text = request.form.get('response')

        complaint = buses.query.get(complaint_id)
        if complaint:
            complaint.status = new_status
            complaint.response = response_text

            # Set date_resolved only when marked as resolved
            if new_status.lower() == 'resolved':
                complaint.date_resolved = datetime.now()
            else:
                complaint.date_resolved = None

            db.session.commit()
    complaints=buses.query.all()
    return render_template('ad_bus_inter.html',complaints=complaints,name=name,category=category)


@app.route('/off_view_complaints')
def view_admin_complaint():
    name = session.get('user')
    category=session.get('category')
    return render_template('ad_off_inter.html',name=name,category=category)

@app.route('/view_teacher_complaints')
def view_teacher_complaints():
    name = session.get('user')
    category=session.get('category')
    complaints=T_Complaints.query.all()
    suggest=T_Suggestion.query.all()
    anonymous=T_Anonymous.query.all()
    # Add your logic to show teacher complaints
    return render_template('ad_teachers_complaints.html',complaints=complaints,suggest=suggest,anonymous=anonymous,name=name,category=category)



@app.route('/view_student_complaints')
def view_student_complaints():
    complaints=acad.query.all()
    hostels=hostel.query.all()
    mes=mess.query.all()
    sp=sports.query.all()
    bs=buses.query.all()
    sg=s_suggest.query.all()
    an=s_anonymous.query.all()
    bas=basic.query.all()
    # Add your logic to show student complaints
    return render_template('ad_students_complaints.html',complaints=complaints,hostels=hostels,mes=mes,sp=sp,bs=bs,sg=sg,an=an,bas=bas)



    # new code to handle admin complaints for changing status and response js
@app.route('/api/complaints/<int:complaint_id>')
def get_complaint_details(complaint_id):
    # Fetch complaint from your database
    complaint = db.session.query(hostel).filter_by(id=complaint_id).first()
    
    if not complaint:
        return jsonify({'error': 'Complaint not found'}), 404    
    # Convert complaint to dictionary
    complaint_data = {
        'id': complaint.id,
        'complaint': complaint.complaint,
        'hostel_no': complaint.hostel_no,
        'room_no': complaint.room_no,
        'date': complaint.date.strftime('%Y-%m-%d') if complaint.date else None,
        'status': complaint.status,
        'response': complaint.response,
        'date_resolved': complaint.date_resolved.strftime('%Y-%m-%d') if complaint.date_resolved else None,
        
}
    
    return jsonify(complaint_data)


@app.route("/update-acad-complaint", methods=["POST"])
def update_complaint():
    complaint_id = request.form.get("id")
    status = request.form.get("status")
    response = request.form.get("response")
    date_resolved_str = request.form.get("date_resolved")  # string from form

    complaint = acad.query.get(complaint_id)
    if complaint:
        complaint.status = status
        complaint.response = response

        # Convert string to Python date object
        if date_resolved_str:
            try:
                complaint.date_resolved = datetime.strptime(date_resolved_str, "%Y-%m-%d").date()
            except ValueError:
                return jsonify({"success": False, "error": "Invalid date format"}), 400
        else:
            complaint.date_resolved = None

        db.session.commit()
        return jsonify({"success": True})

    return jsonify({"success": False, "error": "Complaint not found"}), 404

@app.route("/update-hostel-complaint", methods=["POST"])
def update_hostel_complaint():  
    complaint_id = request.form.get("id")
    status = request.form.get("status")
    response = request.form.get("response")
    date_resolved_str = request.form.get("date_resolved")
    complaint = hostel.query.get(complaint_id)
    if complaint:
        complaint.status = status
        complaint.response = response

        if date_resolved_str:
            try:
                complaint.date_resolved = datetime.strptime(date_resolved_str, "%Y-%m-%d").date()
            except ValueError:
                return jsonify({"success": False, "error": "Invalid date format"}), 400
        else:
            complaint.date_resolved = None

        db.session.commit()
        return jsonify({"success": True})
    
    return jsonify({"success": False, "error": "Complaint not found"}), 404

@app.route('/update-basic-complaint', methods=['POST'])
def update_basic_complaint():
    complaint_id = request.form.get("id")
    status = request.form.get("status")
    response = request.form.get("response")
    date_resolved_str = request.form.get("date_resolved")

    complaint = basic.query.get(complaint_id)
    if complaint:
        complaint.status = status
        complaint.response = response

        if date_resolved_str:
            try:
                complaint.date_resolved = datetime.strptime(date_resolved_str, "%Y-%m-%d").date()
            except ValueError:
                return jsonify({"success": False, "error": "Invalid date format"}), 400
        else:
            complaint.date_resolved = None

        db.session.commit()
        return jsonify({"success": True})

    return jsonify({"success": False, "error": "Complaint not found"}), 404

@app.route('/update-mess-complaint', methods=['POST'])
def update_mess_complaint():
    complaint_id = request.form.get("id")
    status = request.form.get("status")
    response = request.form.get("response")
    date_resolved_str = request.form.get("date_resolved")

    complaint = mess.query.get(complaint_id)
    if complaint:
        complaint.status = status
        complaint.response = response

        if date_resolved_str:
            try:
                complaint.date_resolved = datetime.strptime(date_resolved_str, "%Y-%m-%d").date()
            except ValueError:
                return jsonify({"success": False, "error": "Invalid date format"}), 400
        else:
            complaint.date_resolved = None

        db.session.commit()
        return jsonify({"success": True})

    return jsonify({"success": False, "error": "Complaint not found"}), 404
@app.route('/update-sports-complaint', methods=['POST'])
def update_sports_complaint():  
    complaint_id = request.form.get("id")
    status = request.form.get("status")
    response = request.form.get("response")
    date_resolved_str = request.form.get("date_resolved")

    complaint = sports.query.get(complaint_id)
    if complaint:
        complaint.status = status
        complaint.response = response

        if date_resolved_str:
            try:
                complaint.date_resolved = datetime.strptime(date_resolved_str, "%Y-%m-%d").date()
            except ValueError:
                return jsonify({"success": False, "error": "Invalid date format"}), 400
        else:
            complaint.date_resolved = None

        db.session.commit()
        return jsonify({"success": True})

    return jsonify({"success": False, "error": "Complaint not found"}), 404

@app.route('/update-bus-complaint', methods=['POST'])
def update_bus_complaint():
    complaint_id = request.form.get("id")
    status = request.form.get("status")
    response = request.form.get("response")
    date_resolved_str = request.form.get("date_resolved")

    complaint = buses.query.get(complaint_id)
    if complaint:
        complaint.status = status
        complaint.response = response

        if date_resolved_str:
            try:
                complaint.date_resolved = datetime.strptime(date_resolved_str, "%Y-%m-%d").date()
            except ValueError:
                return jsonify({"success": False, "error": "Invalid date format"}), 400
        else:
            complaint.date_resolved = None

        db.session.commit()
        return jsonify({"success": True})

    return jsonify({"success": False, "error": "Complaint not found"}), 404