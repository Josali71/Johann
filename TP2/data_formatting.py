class DataFormatting :
    def format_data(cleaned_data) :
        if cleaned_data ['weight'] != 0 and cleaned_data ['height'] != 0 :
            cleaned_data['bmi'] = cleaned_data ['weight']/(cleaned_data ['height']**2)
        else :
            print ('BMI ne peut être calculée')


        list_type = []
        for t in cleaned_data['types'] :
            list_type.append(t['name'])
        
        concat = ", ".join(list_type)
        print (concat)

        cleaned_data['types'] = concat
          
       

        return cleaned_data
