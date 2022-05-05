high_score = True
credit_score = False
student = False
if (high_score or credit_score) and not student:
    print("eligible")
else:
    print("not eligible")
