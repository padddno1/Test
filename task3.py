list_of_students = [
    {
        "Ten": "An", 
        "STT": 1,
        "Gioi tinh": "Nam", 
        "Diem Toan": 8,
        "Diem Van": 8, 
        "Diem tieng Anh": 8,
    },
    {
        "Ten": "Binh", 
        "STT": 2,
        "Gioi tinh": "Nu", 
        "Diem Toan": 7,
        "Diem Van": 8, 
        "Diem tieng Anh": 9.5,
    },
    {
        "Ten": "Chau", 
        "STT": 3,
        "Gioi tinh": "Nu", 
        "Diem Toan": 9,
        "Diem Van": 8.5, 
        "Diem tieng Anh": 8,
    }
    ]

    def view(students):
        for s in list_of_students:
            for num in s:
                print(list_of_students)

    def check(students):
        for s in list_of_students:
            for stu in s:
                if students == stu:
                    return True
        return False