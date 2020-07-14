






class GraphDatabase():
    def __init__(self):
        self.relation = {"ms1":["1.1.1.1"],
                         "ms2":["1.1.1.1","2.2.2.2"],
                         "1.1.1.1":["ms1","ms2"],
                         "2.2.2.2":["ms2"]}

        self.schema = [
            {
                "ip":["cpu_configuration","cpu_cores","cpu_usage","memory","cpu_status"]
            },
            {
                "microservice":["io"]
            }
        ]
        self.entity_list = ['ip','microservice']
        self.data = {
    "ip":
        {
            "1.1.1.1":{
                "cpu_configuration": "32 cores",
                "cpu_cores": "32 cores",
                "cpu_usage": "30%",
                "cpu_status": "30%",
                "memory": "64G"
            },
            "2.2.2.2":{
                "cpu_configuration": "64 cores",
                "cpu_cores": "64 cores",
                "cpu_usage": "40%",
                "cpu_status": "40%",
                "memory": "32G"
            }
        },
    "microservice": {

            "ms1": {
                "io": "8 pbs",
                "memory":"2GB"
            },
            "ms2": {
                "io": "10 bps",
                "memory":"8GB"
            }
    }
}
    def map_entity_type(self,entity_type):
        if entity_type in ["ip","host","hosts"]:
            return "ip"
        elif entity_type in ["microservice"]:
            return "microservice"
        else:
            return None

    def get_attributes_of_entity(self,entity_type):
        for tmp in self.schema:
            if entity_type in tmp.keys():
                return tmp[entity_type]

    # def get_entity_value(self,entity_type, attributes):
    #     if entity_type == "ip":
    #         return self._get_ip_entities(attributes)
    #     if entity_type == "microservice":
    #         return self._get_microservice_entities(attributes)

    def get_entities(self,entity_type):
        if entity_type == "ip":
            return ['1.1.1.1','2.2.2.2']
        if entity_type == "microservice":
            return ['ms1','ms2']






if __name__ == "__main__":
    g = GraphDatabase()
    print(g.get_attributes_of_entity("ip"))






