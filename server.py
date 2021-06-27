from flask import Flask, render_template,url_for, request, redirect
app = Flask(__name__)
print(__name__)
import csv 

@app.route('/<string:page_name>')
def html_page(page_name):
   return render_template(page_name)

@app.route('/')
def html():
   return render_template('index.html')



def write_to_file(data):
	with open('database.txt', mode='a') as database: 
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		file = database.write(f'\n {email},{subject},{message}')

def write_to_csv(data):
	with open('database.csv', mode='a', newline='') as database2:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		csv_writer = csv.writer(database2, delimiter= ',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email, subject, message])




@app.route('/submited_form', methods=['POST', 'GET'])
def submited_form():
    if request.method == 'POST':
    	data= request.form.to_dict()
    	write_to_csv(data)
    	return render_template('/thanks.html')
    else:
    	return 'something went wrong. Try agian please'


#@app.route('/blog/<username>')
#def blog(username= None):
#   return render_template('blog.html', name= username)






#@app.route('/Skills.html')
#def Skills():
#   return render_template('Skills.html')   

#@app.route('/about.html')
#def about_me():
#   return render_template('about.html') 

   
#@app.route('/contact.html')
#def content():
#   return render_template('contact.html') 


#@app.route('/components.html')
#def components():
#   return render_template('components.html') 