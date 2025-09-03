from bs4 import BeautifulSoup


with open("basic/home.html", "r") as html_file:
    content = html_file.read()  # read the content of the file
    soup = BeautifulSoup(
        content, "lxml"
    )  # parse the content of the file using BeautifulSoup and lxml parser
    courses = soup.find_all(
        "div", class_="card"
    )  # find all h5 tags on the page, and retuurn as a list
    for course in courses:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]
        print(f"{course_name} costs {course_price}")
