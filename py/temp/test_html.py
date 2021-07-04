# 
# from mako.template import Template
from jinja2 import Template
# mytemplate = Template(filename='test1.html')

# print(mytemplate.render(topics=("Python GUIs","Python IDEs","Python web scrapers")))

report_template = None
with open("test_report.html", mode='r') as fh:
    report_template = Template(fh.read())

def create_test_record(test_group:str, test_name:str, test_status:str, lower_limit:str, upper_limit:str, measurement:str, measure_unit:str, cost_time:str):
    return dict(test_group=test_group, 
                test_name=test_name, 
                test_status=test_status, 
                lower_limit=lower_limit,
                upper_limit=upper_limit,
                measurement=measurement,
                measure_unit=measure_unit,
                cost_time=cost_time)

table_rows = []
table_rows.append(create_test_record("Voltage Test", "TP62(3.5V)", "FAIL", "3.325", "3.675", "-0.001", "V", "19.886183"))
table_rows.append(create_test_record("Voltage 2", "TP62(3.5V)", "FAIL", "3.325", "3.675", "-0.001", "V", "19.886183"))
table_rows.append(create_test_record("Voltage 5", "TP62(3.5V)", "FAIL", "3.325", "3.675", "-0.001", "V", "19.886183"))

data = {title:"Test Results For Serial Number: 6a443f Executed At 2021-05-24 09:27:32",
serial_num:"6a443f",
start_time="2021-05-24 09:27:32",
stop_time="2021-05-24 09:28:20",
test_station="UN",
test_operator="TEST",
test_cell="0",
test_result="ABORT",
test_script="D:/yang/testcode/TestScipt/EpdsTestPlatform_V0.0.5/TestScript/Wireless_in_Scale_V1.0.2.py",
elapsed_time="47.124538s",
total_execu_time=" 47.124538",
table_rows=table_rows}

rst = report_template.render()

# =[{test_group: "Voltage Test", test_name: "TP62(3.5V)"},
# {test_group: "Voltage Test2", test_name: "TP62(3.5V)2"}]

with open('report.html', 'w') as fh:
    fh.write(rst)




