from django.shortcuts import render,redirect
from .models import User,Member,Chairman,Watchman,Event,Notice,Visitor
from django.conf import settings
from django.core.mail import send_mail
import random
from django.http import JsonResponse
# Create your views here.
def index(request):
	return render(request,'index.html')

def signup(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.session['email'])
			msg1 = "email alredy exist..."
			return render(request,'signup.html',{'msg1':msg1})
		except:
			if request.POST['pswd'] == request.POST['cpswd']:
				user=User.objects.create(
				name=request.POST['name'],
				email=request.POST['email'],
				pswd=request.POST['pswd'],
				)
				msg="signup successfuly..."
				return render(request,'login.html',{'msg':msg})
			else:
				msg1="password and confirm password are not matched...."
				return render(request,'signup.html',{'msg1':msg1})
	else:
		return render(request,'signup.html')

def e_verify(request):
	email=request.GET.get('email')
	print(">>>>>>>>>>>>>>>>AJAX DATA : ",email)
	data={'is_taken':User.objects.filter(email__iexact=email).exists()}
	return JsonResponse(data)


def login(request):
	if request.method=='POST':
		try:
			user=User.objects.get(email=request.POST['email'],pswd=request.POST['pswd'])
			msg="Login successfully.."
			request.session['email']=user.email
			request.session['pswd']=user.pswd
			return render(request,'index.html')
		except:
			msg1="email doesn't exist..."
			return render(request,'login.html',{'msg1':msg1})
	else:
		return render(request,'login.html')

def logout(request):
	del request.session['email']
	return redirect('login')

def fpswd(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			subject = 'Forgot Password OTP'
			otp=random.randint(1000,9999)
			message = f'Hi {user.name}, thank you for registering in MyApp. Your OTP is : '+str(otp)			
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [user.email, ]
			send_mail( subject, message, email_from, recipient_list)
			print(">>>>till here donne")
			return render(request,'verify_otp.html',{'email':user.email,'otp':str(otp)})
		except:
			msg1 ="you are not a registered user..."
			return render(request,'fpswd.html',{'msg1':msg1})
	else:
		return render(request,'fpswd.html')

def verify_otp(request):
	if request.method=="POST":
		email=request.POST['email']
		otp=request.POST['otp']
		uotp=request.POST['uotp']
		if uotp == otp:
			return render(request,'set_pswd.html',{'email':email})
		else:
			msg1="OTP does not matched.."
			return render(request,'verify_otp.html',{'msg1':msg1})
	else:
		return render(request,'verify_otp.html')

def set_pswd(request):
	if request.method=="POST":

		email=request.POST['email']
		npswd=request.POST['npswd']
		cnpswd=request.POST['cnpswd']

		if npswd==cnpswd:
			user=User.objects.get(email=email)
			user.pswd=npswd
			user.save()
			return redirect('login')
		else:
			msg1 = "password and confirm password both are not matched..."
			return render(request,'set_pswd.html',{'msg1':msg1})
	else:
		return render(request,'set_pswd.html')

def add_member(request):
	if request.method=="POST":
		user=User.objects.get(email=request.session['email'])
		Member.objects.create(
		user=user,
		m_name=request.POST['m_name'],
		m_contact=request.POST['m_contact'],
		m_num=request.POST['m_num'],
		)
		msg="member added successfully..."
		return render(request,'add_member.html',{'msg':msg})
	else:
		return render(request,'add_member.html')

def member(request):
	seller=User.objects.get(email=request.session['email'])
	print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>by method",seller)
	member=Member.objects.filter(user=seller)
	print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",member)
	return render(request,'member.html',{'member':member})

def update_member(request,pk):
	seller=User.objects.get(email=request.session['email'])
	member=Member.objects.get(pk=pk,user=seller)
	if request.method=="POST":
		member.user=seller
		member.m_name=request.POST['m_name']
		member.m_contact=request.POST['m_contact']
		member.m_num=request.POST['m_num']
		member.save()
		return render(request,'member.html',{'member':member})
	else:	
		return render(request,'update_member.html',{'member':member})

def delete_member(request,pk):
	seller=User.objects.get(email=request.session['email'])
	member=Member.objects.get(pk=pk,user=seller)
	member.delete()
	return redirect("index")

def add_chairman(request):
	if request.method=="POST":
		user=User.objects.get(email=request.session['email'])

		Chairman.objects.create(
		user=user,
		c_name=request.POST['c_name'],
		c_contact=request.POST['c_contact'],
		)
		msg="chairman added successfully..."
		return render(request,'add_chairman.html',{'msg':msg})
	else:
		return render(request,'add_chairman.html')

def chairman(request):
	c=User.objects.get(email=request.session['email'])
	print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>by method",c)
	chairman=Chairman.objects.filter(user=c)
	print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",chairman)
	return render(request,'chairman.html',{'chairman':chairman})

def update_chairman(request,pk):
	c=User.objects.get(email=request.session['email'])
	chairman=Chairman.objects.get(pk=pk,user=c)
	if request.method=="POST":
		chairman.user=c
		chairman.c_name=request.POST['c_name']
		chairman.c_contact=request.POST['c_contact']
		chairman.save()
		return render(request,'chairman.html',{'chairman':chairman})
	else:
		return render(request,'update_chairman.html',{'chairman':chairman})

def delete_chairman(request,pk):
	c=User.objects.get(email=request.session['email'])
	chairman=Chairman.objects.get(pk=pk,user=c)
	chairman.delete()
	return redirect("index")

def add_watchman(request):
	if request.method=="POST":
		user=User.objects.get(email=request.session['email'])

		Watchman.objects.create(
		user=user,
		w_name = request.POST['w_name'],
		w_contact = request.POST['w_contact'],
		)
		msg="watchman added successfully..."
		return render(request,'add_watchman.html',{'msg':msg})
	else:
		return render(request,'add_watchman.html')

def watchman(request):
	w=User.objects.get(email=request.session['email'])
	print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>by method",w)
	watchman=Watchman.objects.filter(user=w)
	print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",watchman)
	return render(request,'watchman.html',{'watchman':watchman})

def update_watchman(request,pk):
	w=User.objects.get(email=request.session['email'])
	watchman=Watchman.objects.get(pk=pk,user=w)
	if request.method=="POST":
		watchman.user=w
		watchman.w_name=request.POST['w_name']
		watchman.w_contact=request.POST['w_contact']
		watchman.save()
		return render(request,'watchman.html',{'watchman':watchman})
	else:
		return render(request,'update_watchman.html',{'watchman':watchman})

def delete_watchman(request,pk):
	w=User.objects.get(email=request.session['email'])
	watchman=Watchman.objects.get(pk=pk,user=w)

	watchman.delete()
	return redirect("index")



def add_event(request):
	if request.method=="POST":
		user=User.objects.get(email=request.session['email'])
		Event.objects.create(
		user=user,
		e_name = request.POST['e_name'],
		e_date = request.POST['e_date'],
		)
		msg="event added successfully..."
		return render(request,'add_event.html',{'msg':msg})
	else:
		return render(request,'add_event.html')

def event(request):
	e=User.objects.get(email=request.session['email'])
	print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>by method",e)
	event=Event.objects.filter(user=e)
	print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",event)
	return render(request,'event.html',{'event':event})

def update_event(request,pk):
	e=User.objects.get(email=request.session['email'])
	event=Event.objects.get(pk=pk,user=e)
	if request.method=="POST":
		event.user=e
		event.e_name=request.POST['e_name']
		event.e_date=request.POST['e_date']
		event.save()
		return render(request,'update_event.html',{'event':event})
	else:
		return render(request,'update_event.html',{'event':event})

def delete_event(request,pk):
	e=User.objects.get(email=request.session['email'])
	event=Event.objects.get(pk=pk,user=e)

	event.delete()
	return redirect("index")

def add_notice(request):
	if request.method=="POST":
		user=User.objects.get(email=request.session['email'])

		Notice.objects.create(
			user=user,
			n_name = request.POST['n_name'],
			n_sub = request.POST['n_sub'],
			)
		msg="notice added successfully..."
		return render(request,'add_notice.html',{'msg':msg})	
	else:
		return render(request,'add_notice.html')

def notice(request):
	notice=User.objects.get(email=request.session['email'])
	print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>by method",notice)
	notice=Notice.objects.filter(user=notice)
	print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",notice)
	return render(request,'notice.html',{'notice':notice})

def update_notice(request,pk):
	notice=User.objects.get(email=request.session['email'])
	notice=Notice.objects.get(pk=pk,user=notice)
	if request.method=="POST":
		notice.user=seller
		notice.n_name=request.POST['n_name']
		notice.n_sub=request.POST['n_sub']
		notice.save()
		return render(request,'update_notice.html',{'notice':notice})
	else:
		return render(request,'update_notice.html',{'notice':notice})

def delete_notice(request,pk):
	notice=User.objects.get(email=request.session['email'])
	notice=Notice.objects.get(pk=pk,user=notice)

	notice.delete()
	return redirect("index")

def add_visitor(request) :
	if request.method=="POST":
		Visitor.objects.create(
			name=request.POST['name'],
			contact=request.POST['contact']
			)		
		print("Doneeeee")
		return redirect('visitor')
	else:
		return render(request,'add_visitor.html')

def visitor(request):
	visitor=Visitor.objects.all()
	return render(request,'visitor.html',{'visitor':visitor})

def delete_visitor(request,pk):
	if request.method=="POST":
		visitor=User.objects.get(email=request.session['email'])
		visitor=Visitor.objects.get(pk=pk,user=visitor)

		visitor.delete()
		return redirect('index')
	else:
		return redirect('visitor')





