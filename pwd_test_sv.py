import ocpsecurity

usr_name = 'Wednesday22017'
pwd = 'Password7*'
sec = ocpsecurity.security()

response = sec.SignIn(usr_name,pwd)
print('pwd:',pwd,'response:',response)
