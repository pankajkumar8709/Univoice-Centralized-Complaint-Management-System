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
    user_id = session.get('name')
    if not user_id:
        flash("You must log in first!", 401)
        return redirect(url_for('s_login'))
    return render_template('acad.html')

@app.route('/submit_academic_complaint',methods=['GET','POST'])
def a_add():
    user_id = session.get('name')
    if not user_id:
        flash("You must log in first!", 401)
        return redirect(url_for('s_login'))
    if request.method=='POST':
        complaint=request.form['complaint']
        semester=request.form['semester']
        course=request.form['course']
        section=request.form['section']
        date=request.form['date']

        date_obj = datetime.strptime(date, '%Y-%m-%d').date()




        a1=acad(name=session['name'],complaint=complaint,semester=semester,course=course,section=section,date=date_obj)

        db.session.add(a1)
        db.session.commit()
        flash("Form submitted succesfully",category='success')
        return redirect(url_for('s_interface'))

@app.route('/hostel',methods=['GET','POST'])
def hostel_page():
    user_id = session.get('name')
    if not user_id:
        flash("You must log in first!", 401)
        return redirect(url_for('s_login'))
    return render_template('hostel.html')
@app.route('/submit_hostel_complaint',methods=['POST'])
def h_add():
    user_id = session.get('name')
    if not user_id:
        flash("You must log in first!", 401)
        return redirect(url_for('s_login'))
    complaint=request.form['complaint']
    h_no=request.form['hostel']
    r_no=request.form['room']
    date=request.form['date']

    date_obj = datetime.strptime(date, '%Y-%m-%d').date()

    h1=hostel(name=session['name'],complaint=complaint,hostel_no=h_no,room_no=r_no,date=date_obj)
    db.session.add(h1)
    db.session.commit()
    flash("Form Submitted successfully",category='success')
    return redirect(url_for('s_interface'))

@app.route('/mess',methods=['GET','POST'])
def mess_page():
    user_id = session.get('name')
    if not user_id:
        flash("You must log in first!", 401)
        return redirect(url_for('s_login'))
    return render_template('mess.html')

@app.route('/submit_mess_complaint',methods=['POST'])
def m_add():
    user_id = session.get('name')
    if not user_id:
        flash("You must log in first!", 401)
        return redirect(url_for('s_login'))
    complaint=request.form['complaint']
    day=request.form['day']
    meal=request.form['meal']
    date=request.form['date']

    date_obj = datetime.strptime(date, '%Y-%m-%d').date()



    m1=mess(name=session['name'],complaint=complaint,day=day,meal=meal,date=date_obj)
    db.session.add(m1)
    db.session.commit()

    flash("Form Submitted successfully",category='success')
    return redirect(url_for('s_interface'))

@app.route('/sports',methods=['GET','POST'])
def sports_page():
    user_id = session.get('name')
    if not user_id:
        flash("You must log in first!", 401)
        return redirect(url_for('s_login'))
    return render_template('sports.html')

@app.route('/submit_sports_complaint',methods=['POST'])
def sp_add():
    user_id = session.get('name')
    if not user_id:
        flash("You must log in first!", 401)
        return redirect(url_for('s_login'))
    complaint=request.form['complaint']
    t_sport=request.form['sport']
    date=request.form['date']

    date_obj = datetime.strptime(date, '%Y-%m-%d').date()

    sp1=sports(name=session['name'],complaint=complaint,type=t_sport,date=date_obj)
    db.session.add(sp1)
    db.session.commit()
    flash("form submitted successfully",category='success')
    return redirect(url_for('s_interface'))

@app.route('/buses',methods=['GET','POST'])
def buses_page():
    user_id = session.get('name')
    if not user_id:
        flash("You must log in first!", 401)
        return redirect(url_for('s_login'))
    return render_template('buses.html')

@app.route('/submit_bus_complaint',methods=['POST'])
def b_add():
    user_id = session.get('name')
    if not user_id:
        flash("You must log in first!", 401)
        return redirect(url_for('s_login'))
    complaint=request.form['complaint']
    b_no=request.form['bus']
    date=request.form['date']
    date_obj = datetime.strptime(date, '%Y-%m-%d').date()

    b1=buses(name=session['name'],complaint=complaint,bus_no=b_no,date=date_obj)
    db.session.add(b1)
    db.session.commit()
    flash("form submitted successfully",category='success')
    return redirect(url_for('s_interface'))

@app.route('/basics',methods=['GET','POST'])
def basics_page():
    user_id = session.get('name')
    if not user_id:
        flash("You must log in first!", 401)
        return redirect(url_for('s_login'))
    return render_template('basics.html')

@app.route('/submit_amenities_complaint',methods=['POST'])
def bs_add():
    user_id = session.get('name')
    if not user_id:
        flash("You must log in first!", 401)
        return redirect(url_for('s_login'))
    complaint=request.form['complaint']
    category=request.form['category']
    date=request.form['date']
    date_obj = datetime.strptime(date, '%Y-%m-%d').date()

    ba1=basic(name=session['name'],complaint=complaint,category=category,date=date_obj)
    db.session.add(ba1)
    db.session.commit()
    flash("form submitted successfully",category='success')
    return redirect(url_for('s_interface'))

@app.route('/anonymous',methods=['GET','POST'])
def anonymous_page():
    user_id = session.get('name')
    if not user_id:
        flash("You must log in first!", 401)
        return redirect(url_for('s_login'))
    return render_template('anonymous.html')

@app.route('/submit_anonymous_complaint',methods=['POST'])
def an_add():
    user_id = session.get('name')
    if not user_id:
        flash("You must log in first!", 401)
        return redirect(url_for('s_login'))
    complaint=request.form['complaint']
    category=request.form['category']
    date=request.form['date']
    date_obj = datetime.strptime(date, '%Y-%m-%d').date()

    an1=s_anonymous(name=session['name'],complaint=complaint,category=category,date=date_obj)
    db.session.add(an1)
    db.session.commit()
    flash("form submitted successfully",category='success')
    return redirect(url_for('s_interface'))

@app.route('/suggest',methods=['GET','POST'])
def suggestion_page():
    user_id = session.get('name')
    if not user_id:
        flash("You must log in first!", 401)
        return redirect(url_for('s_login'))
    return render_template('suggestion.html') 

@app.route('/submit_suggestion',methods=['POST'])
def sg_add():
    user_id = session.get('name')
    if not user_id:
        flash("You must log in first!", 401)
        return redirect(url_for('s_login'))
    suggestion=request.form['suggestion']
    date=request.form['date']
    date_obj = datetime.strptime(date, '%Y-%m-%d').date()

    sg1=s_suggest(name=session['name'],suggestion=suggestion,date=date_obj)
    db.session.add(sg1)
    db.session.commit()
    flash("form submitted successfully",category='success')
    return redirect(url_for('s_interface'))

@app.route('/view_complaints')
def view_complaint():
    user_id = session.get('name')
    if not user_id:
        flash("You must log in first!", 401)
        return redirect(url_for('s_login'))
    # Fetch all complaints related to the user

    complaints = acad.query.filter_by(name=user_id).all()
    hostels = hostel.query.filter_by(name=user_id).all()
    mes = mess.query.filter_by(name=user_id).all()
    sp = sports.query.filter_by(name=user_id).all()
    bs = buses.query.filter_by(name=user_id).all()
    sg = s_suggest.query.filter_by(name=user_id).all()
    an = s_anonymous.query.filter_by(name=user_id).all()
    bas = basic.query.filter_by(name=user_id).all()

    return render_template(
        's_complaints.html',
        complaints=complaints,
        hostels=hostels,
        mes=mes,
        sp=sp,
        bs=bs,
        sg=sg,
        an=an,
        bas=bas
    )





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
                    flash("Login successful", category='success')
                    return redirect(url_for('t_interface'))
                else:
                    flash("Invalid password")
            else:
                flash("Employee ID not found")

    return render_template('t_login.html')

@app.route('/t_interface')
def t_interface():
    name=session.get('user')
    if not name:
        flash("Please login first.")
        return redirect(url_for('t_login'))
    return render_template('t_interface.html',name=name)

@app.route('/t_complaint',methods=['GET','POST'])
def t_complaint():
    name=session.get('user')
    if not name:
        flash("Please login first.")
        return redirect(url_for('t_login'))
    return render_template('t_complaint.html')
@app.route('/t_anonymous',methods=['GET','POST'])
def t_anonymous():
    name=session.get('user')
    if not name:
        flash("Please login first.")
        return redirect(url_for('t_login'))
    return render_template('t_anonymous.html')
@app.route('/t_suggestion',methods=['GET','POST'])
def t_suggestion():
    name=session.get('user')
    if not name:
        flash("Please login first.")
        return redirect(url_for('t_login'))
    return render_template('t_suggest.html')
@app.route('/t_view',methods=['GET','POST'])
def t_view_page():
    
    name= session.get('user')
    if not name:
        flash("Please login first.")
        return redirect(url_for('t_login'))
    complaints=T_Complaints.query.filter_by(name=name).all()
    suggest=T_Suggestion.query.filter_by(name=name).all()
    anonymous=T_Anonymous.query.filter_by(name=name).all()


    return render_template('t_view_complaints.html',complaints=complaints,suggestion=suggest,anonymous=anonymous)



@app.route('/submit_teacher_complaint',methods=['POST'])
def submit_t_complaints():
    name=session.get('user')
    if not name:
        flash("Please login first.")
        return redirect(url_for('t_login'))
    title=request.form['title']
    desc=request.form['details']
    category=request.form['category']
    date=request.form['date']
    others=request.form['others']

    date_obj=datetime.strptime(date,'%Y-%m-%d').date()
    st1=T_Complaints(name=session['user'],title=title,complaint=desc,category=category,date=date_obj,others=others)
    db.session.add(st1)
    db.session.commit()

    flash("Form Submitted Successfully",category='success')
    return redirect(url_for('t_interface'))

@app.route('/submit_teacher_suggestion',methods=['POST'])
def submit_t_suggest():
    name=session.get('user')
    if not name:
        flash("Please login first.")
        return redirect(url_for('t_login'))
    title=request.form['title']
    category=request.form['category']
    desc=request.form['details']
    date=request.form['date']

    date_obj=datetime.strptime(date,'%Y-%m-%d').date()
    st1=T_Suggestion(name=session['user'],title=title,category=category,complaint=desc,date=date_obj)
    db.session.add(st1)
    db.session.commit()

    flash("Form Submitted Successfully",category='success')
    return redirect(url_for('t_interface'))

@app.route('/submit_anonymous_teacher',methods=['POST'])
def submit_t_anonymous():
    name=session.get('user')
    if not name:
        flash("Please login first.")
        return redirect(url_for('t_login'))
    category=request.form['category']
    desc=request.form['details']
    st1=T_Anonymous(name=session['user'],category=category,complaint=desc)
    db.session.add(st1)
    db.session.commit()

    flash("Form Submitted Successfully",category='success')
    return redirect(url_for('t_interface'))

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
                    session['username']=name
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
    name = session.get('username')
    if not name:
        flash("Please login first.")
        return redirect(url_for('admin_login'))
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
    name = session.get('username')
    if not name:
        flash("Please login first.")
        return redirect(url_for('admin_login'))
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
    name = session.get('username')
    if not name:
        flash("Please login first.")
        return redirect(url_for('admin_login'))
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
    name = session.get('username')
    if not name:
        flash("Please login first.")
        return redirect(url_for('admin_login'))
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
    name = session.get('username')
    if not name:
        flash("Please login first.")
        return redirect(url_for('admin_login'))
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
    name = session.get('username')
    if not name:
        flash("Please login first.")
        return redirect(url_for('admin_login'))
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
    name = session.get('username')
    if not name:
        flash("Please login first.")
        return redirect(url_for('admin_login'))
    category=session.get('category')
    return render_template('ad_off_inter.html',name=name,category=category)

@app.route('/view_teacher_complaints')
def view_teacher_complaints():
    name = session.get('username')
    if not name:
        flash("Please login first.")
        return redirect(url_for('admin_login'))
    category=session.get('category')
    complaints=T_Complaints.query.all()
    suggest=T_Suggestion.query.all()
    anonymous=T_Anonymous.query.all()
    return render_template('ad_teachers_complaints.html',complaints=complaints,suggest=suggest,anonymous=anonymous,name=name,category=category)



@app.route('/view_student_complaints')
def view_student_complaints():
    name= session.get('username')
    if not name:
        flash("Please login first.")
        return redirect(url_for('admin_login'))
    complaints=acad.query.all()
    hostels=hostel.query.all()
    mes=mess.query.all()
    sp=sports.query.all()
    bs=buses.query.all()
    sg=s_suggest.query.all()
    an=s_anonymous.query.all()
    bas=basic.query.all()
    return render_template('ad_students_complaints.html',complaints=complaints,hostels=hostels,mes=mes,sp=sp,bs=bs,sg=sg,an=an,bas=bas)



@app.route('/api/complaints/<int:complaint_id>')
def get_complaint_details(complaint_id):
    name= session.get('username')
    if not name:
        flash("Please login first.")
        return redirect(url_for('admin_login'))
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
    name= session.get('username')
    if not name:
        flash("Please login first.")
        return redirect(url_for('admin_login'))
    data = request.get_json()
    if not data:
        return jsonify({"success": False, "error": "No data provided"}), 400

    complaint_id = data.get("id")
    status = data.get("status")
    response = data.get("response")
    date_resolved_str = data.get("date_resolved")  

    
    if not all([complaint_id, status]):
        return jsonify({"success": False, "error": "Missing required fields"}), 400

    complaint = acad.query.get(complaint_id)
    if not complaint:
        return jsonify({"success": False, "error": "Complaint not found"}), 404

    try:
        complaint.status = status
        complaint.response = response

        if status.lower() == "resolved" and not date_resolved_str:
            complaint.date_resolved = datetime.utcnow().date()
        elif date_resolved_str:
            try:
                complaint.date_resolved = datetime.strptime(date_resolved_str, "%Y-%m-%d").date()
            except ValueError:
                return jsonify({
                    "success": False,
                    "error": f"Invalid date format. Expected YYYY-MM-DD, got {date_resolved_str}"
                }), 400
        else:
            complaint.date_resolved = None

        db.session.commit()
        return jsonify({
            "success": True,
            "message": "Complaint updated successfully",
            "data": {
                "id": complaint.id,
                "status": complaint.status,
                "date_resolved": complaint.date_resolved.strftime("%Y-%m-%d") if complaint.date_resolved else None
            }
        })

    except Exception as e:
        db.session.rollback()
        return jsonify({
            "success": False,
            "error": str(e),
            "message": "Failed to update complaint"
        }), 500

@app.route('/update-hostel-complaint', methods=['POST'])
def update_hostel_complaint():
    name= session.get('username')
    if not name:
        flash("Please login first.")
        return redirect(url_for('admin_login'))
    try:
        # Get JSON data from request
        data = request.get_json()
        if not data:
            return jsonify({
                'success': False,
                'error': 'No data received'
            }), 400

        # Validate required fields
        complaint_id = data.get('id')
        status = data.get('status')
        
        if not all([complaint_id, status]):
            return jsonify({
                'success': False,
                'error': 'Missing required fields'
            }), 400

        
        complaint = hostel.query.get(complaint_id)
        if not complaint:
            return jsonify({
                'success': False,
                'error': 'Complaint not found'
            }), 404

        # Update fields
        complaint.status = status
        complaint.response = data.get('response', '').strip() or None

        # Handle date_resolved
        if status == 'Resolved':
            date_resolved = data.get('date_resolved')
            if date_resolved:
                try:
                    complaint.date_resolved = datetime.strptime(date_resolved, '%Y-%m-%d').date()
                except ValueError:
                    return jsonify({
                        'success': False,
                        'error': 'Invalid date format (use YYYY-MM-DD)'
                    }), 400
            else:
                complaint.date_resolved = datetime.utcnow().date()
        else:
            complaint.date_resolved = None

        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Complaint updated successfully'
        })

    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'error': str(e),
            'message': 'An error occurred while updating the complaint'
        }), 500

@app.route('/update-basic-complaint', methods=['POST'])
def update_basic_complaint():
    name= session.get('username')
    if not name:
        flash("Please login first.")
        return redirect(url_for('admin_login'))
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
    name= session.get('username')
    if not name:
        flash("Please login first.")
        return redirect(url_for('admin_login'))
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
    name= session.get('username')
    if not name:
        flash("Please login first.")
        return redirect(url_for('admin_login'))
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
    name= session.get('username')
    if not name:
        flash("Please login first.")
        return redirect(url_for('admin_login'))
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