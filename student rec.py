temp_rec = dict()
final_rec = dict()

def add_students():
    global temp_rec
    roll = int(input())
    q1,m1,q2,es,lw,p,valid = read_marks()
    if valid:
        gpa = compute_GPA(q1,m1,q2,es,lw,p)
    gr,val = read_gpa()
    if valid:
        grade = assign_Grade(gr)
    temp_rec[roll] = [[q1,m1,q2,es,lw,p], gpa, grade]
    
def generate_records():
    global final_rec
    for x in temp_rec:
        final_rec[x] = temp_rec[x]
    temp_rec = {}
                      
def display_records():
    global final_rec
    roll = int(input())
    if roll in final_rec.keys():
        print(final_rec[roll][0],end =" ")
        print(final_rec[roll][1],end =" ")
        print(final_rec[roll][2],end =" ")
    else:
        print("ERROR")
        

def compute_GPA(q1,m1,q2,es,lw,p):
    x = round((0.05*q1/20+0.05*q2/20+0.2*m1/50+0.2*lw/100+0.2*p/50+0.3*es/100)*10,2)
    return x

def assign_Grade(n):
    float(n)
    if n==10:
        print("O")
    elif n>9 and n<10:
        print("A")
    elif n>8 and n<9:
        print("B")
    elif n>7 and n<8:
        print("C")
    elif n>6 and n<7:
        print("D")
    elif n>5.5:
        print("Pass")
    else:
        print("Fail")
        
def read_marks():
    global temp_rec
    roll = int(input())
    if roll in temp_rec.keys():
        q1,m1,q2,es,lw,p = temp_rec[roll][0]
        valid = True
    else:
        q1,m1,q2,es,lw,p = [int(x) for x in input().split()]
        if q1>0 and q1<=20 and q2>0 and q2<=20 and m1>0 and m1<=50 and es>0 and es<=100 and lw>0 and lw<=100 and p>0 and p<=50:
            valid = True
        else:
            valid = False
    return q1,m1,q2,es,lw,p,valid

def read_gpa():
    global temp_rec
    roll = int(input())
    if roll in temp_rec.keys():
        gp = temp_rec[roll][1]
    else:
        gp = float(input())
        if gp<0 or gp>10:
            valid = False
        else:
            valid = True
    return gp,valid
        
while True:
    print("Menu:\n1. Add Students \n2. Compute GPA\n3. Compute GPA and Assign Grade\n4. Assign Grade\n5. Generate Records\n6. Display Records\n7. Exit")
    ans = input("Enter Your choice:")
    if ans == "7":
        break
    elif ans =="1":
        add_students()
    elif ans == "2":
        q1,m1,q2,es,lw,p,valid = read_marks()
        if valid:
            print(compute_GPA(q1,m1,q2,es,lw,p))
        else:
            print("ERROR")
    elif ans == "3":
        q1,m1,q2,es,lw,p,valid = read_marks()
        if valid:
            gr = compute_GPA(q1,m1,q2,es,lw,p)
            print(gr, end=" ")
            assign_Grade(gr)
        else:
            print("ERROR")
    elif ans=="4":
        gr,valid = read_gpa()
        if valid:
            assign_Grade(gr)
        else:
            print("ERROR")
    elif ans == "5":
        generate_records()
    elif ans == "6":
        display_records()