## story 09
* request_weather
    - weather_form
    - form{"name":"weather_form"}
    - slot{"requested_slot":"date_time"}
* form: inform{"date_time":"today"}
    - form: weather_form
    - slot{"date_time":"today"}
    - slot{"requested_slot":"location"}
* weather_form{"location":"Shanghai"}
    - form{"name":"weather_form"}
    - slot{"location":"Shanghai"}
    - form{"name":null}
    - slot{"requested_slot":null}
* goodbye
    - utter_goodbye

## story 09
* request_weather
    - weather_form
    - form{"name":"weather_form"}
    - slot{"requested_slot":"date_time"}
* form: inform{"date_time":"tomorrow"}
    - form: weather_form
    - slot{"date_time":"tomorrow"}
    - slot{"requested_slot":"location"}
* weather_form{"location":"Beijing"}
    - form{"name":"weather_form"}
    - slot{"location":"Beijing"}
    - form{"name":null}
    - slot{"requested_slot":null}
* goodbye
    - utter_goodbye
    
    
## story 09
* request_weather
    - weather_form
    - form{"name":"weather_form"}
    - slot{"requested_slot":"location"}
* form: inform{"location":"Shanghai"}
    - form: weather_form
    - slot{"location":"Shanghai"}
    - slot{"requested_slot":"date_time"}
* weather_form{"date_time":"today"}
    - form{"name":"weather_form"}
    - slot{"date_time":"today"}
    - form{"name":null}
    - slot{"requested_slot":null}
* goodbye
    - utter_goodbye
    
## story 09
* request_weather
    - weather_form
    - form{"name":"weather_form"}
    - slot{"requested_slot":"location"}
* form: inform{"location":"Shanghai"}
    - form: weather_form
    - slot{"location":"Shanghai"}
    - slot{"requested_slot":"date_time"}
* weather_form{"date_time":"today"}
    - form{"name":"weather_form"}
    - slot{"date_time":"today"}
    - form{"name":null}
    - slot{"requested_slot":null}
* goodbye
    - utter_goodbye
    
    
    
    
    
## story 09
* request_cpu
    - cpu_form
    - form{"name":"cpu_form"}
    - slot{"requested_slot":"ip"}
* form: inform{"ip":"11.12.13.14"}
    - form: cpu_form
    - slot{"ip":"11.12.13.14"}
    - slot{"requested_slot":"direction"}
* cpu_form{"direction":"N"}
    - form{"name":"cpu_form"}
    - slot{"direction":"N"}
    - form{"name":null}
    - slot{"requested_slot":null}
* goodbye
    - utter_goodbye

## story 09
* request_cpu
    - cpu_form
    - form{"name":"cpu_form"}
    - slot{"requested_slot":"ip"}
* form: inform{"ip":"11.12.13.15"}
    - form: cpu_form
    - slot{"ip":"11.12.13.15"}
    - slot{"requested_slot":"direction"}
* cpu_form{"direction":"E"}
    - form{"name":"cpu_form"}
    - slot{"direction":"E"}
    - form{"name":null}
    - slot{"requested_slot":null}
* goodbye
    - utter_goodbye
    
    
## story 09
* request_cpu
    - cpu_form
    - form{"name":"cpu_form"}
    - slot{"requested_slot":"ip"}
* form: inform{"ip":"11.12.13.13"}
    - form: cpu_form
    - slot{"ip":"11.12.13.13"}
    - slot{"requested_slot":"direction"}
* cpu_form{"direction":"S"}
    - form{"name":"cpu_form"}
    - slot{"direction":"S"}
    - form{"name":null}
    - slot{"requested_slot":null}
* goodbye
    - utter_goodbye
    
## story 09
* request_cpu
    - cpu_form
    - form{"name":"cpu_form"}
    - slot{"requested_slot":"ip"}
* form: inform{"ip":"11.12.13.16"}
    - form: cpu_form
    - slot{"ip":"11.12.13.16"}
    - slot{"requested_slot":"direction"}
* cpu_form{"direction":"E"}
    - form{"name":"cpu_form"}
    - slot{"direction":"E"}
    - form{"name":null}
    - slot{"requested_slot":null}
* goodbye
    - utter_goodbye