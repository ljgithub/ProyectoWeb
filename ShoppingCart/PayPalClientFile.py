from idna import unicode
from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment

import sys

class PayPalClient:
    def __init__(self):
        self.client_id = "AajqarWQaB3MyISiGqJLnlGr8o0JQaCUa7_SYfL1qOLGw4wI9CWuJZUgeKK_JdJgWmmY9pDZdkL7sAoW"
        self.client_secret = "ELxfThep755pKigWC0Sg9i9TmBXqSd2b0LudhCkRj74d3tb9ZevsfsODXU9d43wrYuF3aL_EJGdlqobZ"


        """
            1. EJecutamos el SDK
            Hay que tener en cuenta que 
            Test = SandboxEnvironment
            Produccion = LiveEnvironment    
        """

        self.environment = SandboxEnvironment(client_id=self.client_id,
                                              client_secret=self.client_secret)

        # 2. Retorna un cliente HTTP con el ambiente al que se accedio con las credenciales de PayPal

        self.client = PayPalHttpClient(self.environment)

    def object_to_json(self, json_data):
        """
        Function to print all json data in an organized readable manner
        """
        result = {}
        if sys.version_info[0] < 3:
            itr = json_data.__dict__.iteritems()
        else:
            itr = json_data.__dict__.items()

        for key,value in itr:
            # Skip internal attributes.
            if key.startswith("__"):
                continue
            result[key] = self.array_to_json_array(value) if isinstance(value, list) else \
                self.object_to_json(value) if not self.is_primittive(value) else \
                value

        return result

    def array_to_json_array(self, json_array):
        result =[]

        if isinstance(json_array, list):
            for item in json_array:
                result.append(self.object_to_json(item) if  not self.is_primittive(item) \
                                  else self.array_to_json_array(item) if isinstance(item, list) else item)

        return result

    def is_primittive(self, data):
        return isinstance(data, str) or isinstance(data, unicode) or isinstance(data, int)



