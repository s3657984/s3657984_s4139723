import pyhtml
import student_b_level_1
import student_b_level_2
import student_b_level_3


pyhtml.need_debugging_help=True
# hi
#All pages that you want on the site need to be added as below
pyhtml.MyRequestHandler.pages["/"]=student_b_level_1   #Page to show when someone accesses "http://localhost/"
pyhtml.MyRequestHandler.pages["/b_level_2"]=student_b_level_2   #Page to show when someone accesses "http://localhost/studenty"
pyhtml.MyRequestHandler.pages["/b_level_3"]=student_b_level_3   #Page to show when someone accesses "http://localhost/"

#Host the site!
pyhtml.host_site()