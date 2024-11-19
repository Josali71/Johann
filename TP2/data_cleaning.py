class DataCleaning :
    def clean_data(data) :
        dictionnaire = {
            "id" : data['id'],
            "name" : data ['name'],
            "height" : data ['height'],
            "weight" : data ['weight'],
            "types" : [t['type'] for t in data['types']]
            }

        return dictionnaire

