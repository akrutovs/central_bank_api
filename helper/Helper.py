class Check:
    @staticmethod
    def check_values(value, min_value=0, max_value=100):
        try:
            value = int(value)
            if value < min_value or value > max_value:
                print('Число выходит за пределы')
                return False
            else:
                return True
        except:
            print("Значение не является числом")
            return False
