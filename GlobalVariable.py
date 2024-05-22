from sqlalchemy import Row
def formatSelectedData (data) :
        if type(data) is list :
            isRow = False
            for i in data :
                if type(i) is Row :
                    isRow = True
                    break
            if isRow is False :
                result  = [i.__dict__ for i in data]
                for i in result :  i.pop('_sa_instance_state')
            else :
                result = []
                for i in data :
                    temp_dict = {}
                    temp_indx  = 1
                    if type(i) is Row :
                        for x in i :
                            if len(temp_dict) == 0 :
                                temp_dict = x.__dict__
                                temp_dict.pop('_sa_instance_state')
                            else :
                                for y in x.__dict__ : 
                                    if y in temp_dict :
                                        temp_attr_name = y+'_'+str(temp_indx)
                                        temp_dict.update({temp_attr_name:x.__dict__[y]})
                                        temp_thisrowduplicate = True
                                    else :
                                        temp_dict.update({y:x.__dict__[y]})
                        if temp_thisrowduplicate is True :
                            temp_indx+=1
                    temp_dict.pop('_sa_instance_state')
                    result.append(temp_dict)
        elif type(data) is Row:
            temp_dict = {}
            temp_indx  = 1
            temp_thisrowduplicate = False
            if type(data) is Row :
                for i in data :
                    if len(temp_dict) == 0 :
                        temp_dict = i.__dict__
                        temp_dict.pop('_sa_instance_state')
                    else :
                        for x in i.__dict__ : 
                            if x in temp_dict :
                                temp_attr_name = x+'_'+str(temp_indx)
                                temp_dict.update({temp_attr_name:i.__dict__[x]})
                                temp_thisrowduplicate = True
                            else :
                                temp_dict.update({x:i.__dict__[x]})
                    if temp_thisrowduplicate is True :
                        temp_indx+=1
                        # temp_dict.update(i.__dict__)
            temp_dict.pop('_sa_instance_state')
            result = temp_dict
        else :
            result = data.__dict__
            result.pop('_sa_instance_state')
        return result