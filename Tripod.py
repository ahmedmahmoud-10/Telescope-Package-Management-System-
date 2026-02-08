from Mount import Mount

class Tripod(Mount):
    def __init__(self,p_code,m_code,mp_code,weight_rating,goto):
        super().__init__(p_code,m_code,mp_code,weight_rating,goto)
