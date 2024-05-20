def formatSelectedData (data) :
        if type(data) is list :
            result  = [u.__dict__ for u in data]
            for u in result :  u.pop('_sa_instance_state')
        else :
            result = data.__dict__
            print(result)
            result.pop('_sa_instance_state')
        return result