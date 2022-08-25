

school_student_dict = \
    {
        1: 'Name',
        2: 'SirName',
        3: 'Sex',
        4: 'Birth Day',
        5: 'Class',
        6: 'Class_type',
        7: 'Mark Status',
        8: 'Урок - кабинет - место'
    }

class_dict = \
    {
        1: 'A',
        2: 'B',
        3: 'C',
       
    }
Uroki_dit = \
    {
        1: 'Английский',
        2: 'Математика',
        3: 'История'
    }

cabin_dit = \
    {
        1: '101',
        2: '102',
        3: '103',
        4: '104'
    }

sex_dic = \
    {
        1: 'male',
        2:'female',
        3:'n/d'
    }

def sit_place_dic_creation():
    sit_place={}
    colum = {}
    place = {}
    for i in range (1,6):
        for y in range (1,4):
            for n in range (1,3):
                place [n]="-"
            colum[y]=place
        sit_place[i]=colum
    return sit_place

