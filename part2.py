import part01
import pandas as pd
import re
class method:
    def __init__(self):
        self.name_and_location="[a-zA-Z]{1,30}"
        self.pincode="[1-9][0-9]{5}"
    def validation(self,pattern,value):
        if pattern == "[a-zA-Z]{1,30}":
            if re.fullmatch(pattern,value):
                return ""
            else:
                return "invalid name and location"
        elif pattern == "[1-9][0-9]{5}":
            if re.fullmatch(pattern,value):
                return ""
            else:
                return "invalid pincode"
    def insert_method(self,data):
        error=""
        for key in data:
            if key == 'name':
                error+=self.validation(self.name_and_location,str(data['name']))
            elif key == 'pincode':
                error+=self.validation(self.pincode,str(data['pincode']))
            elif key == 'location':
                error+=self.validation(self.name_and_location,str(data['location']))
        if error:
            return error
        else:
            script="insert into student(name,pincode,location) values('{}',{},'{}')".format(data['name'],data['pincode'],data['location'])
            part01.database.cursor.execute(script)
            part01.database.connect.commit()
            return ""
    def delete_method(self, data):
        error=""
        for key in data:
            if key=='name':
                error+=self.validation(self.name_and_location,str(data['name']))
        if error:
            return error
        else:
            script="delete from student where name = '{}'".format(data['name'])
            part01.database.cursor.execute(script)
            part01.database.connect.commit()
            return ""

    def update_method(self,data):
        error=""
        for key in data:
            if key == 'name':
                error+=self.validation(self.name_and_location,str(data['name']))
            elif key == 'pincode':
                error += self.validation(self.pincode, str(data['pincode']))
            elif key == 'location':
                error += self.validation(self.name_and_location, str(data['location']))
        if error:
            return error
        else:
            script="update student set pincode={},location='{}' where name='{}'".format(data['pincode'],data['location'],data['name'])
            part01.database.cursor.execute(script)
            part01.database.connect.commit()
            return ""
    def fetch_method(self,data):
        error=""
        for key in data:
            if key == 'name':
                error+=self.validation(self.name_and_location,str(data['name']))
        if error:
            return error
        else:
            script="select pincode,location,name from student where name ='{}'".format(data)
            part01.database.cursor.execute(script)
            result = part01.database.cursor.fetchall()
            df=pd.DataFrame(result)
            #here the column index was 0,1,2 therefore it get change to pincode,location and name
            df=df.rename(columns={0: 'pincode', 1: 'location', 2: 'name'},index={0: 'Data'})
            result = {"data": df.to_dict('records')}
            return result

api=method()




