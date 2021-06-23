import calendar

while True:


    day = int(input("Jump To day : "))
    month = int(input("Jump to month : "))
    year = int(input("Jump to year : "))

    gotodate = calendar.weekday(year, month, day)

    if gotodate == 1:
        print("দিনটি মঙ্গলবার")
    elif gotodate == 2:
        print('দিনটি বুধবার')
    elif gotodate == 3:
        print('দিনটি বৃহস্পতিবার')

    elif gotodate == 4:
        print('দিনটি শুক্রবার')
    elif gotodate == 5:
        print('দিনটি শনিবার')

    elif gotodate == 6:
        print('দিনটি রবিবার')

    else:
        print('দিনটি সোমবার')
