# Internship_work
# Demo 

## Introduction

Demo 1 uses Chinese medical datasets from GitHub since it's hard to find English datasets. Demo 1 can prove the state-of-the-art of rasa in controlling mutli-rounds of conversation. Demo 2 use English datasets to show how to define form action in rasa to implement some Task-based conversation.

## Demo 1

### neo4j

#### access url:

http://119.45.121.125:7474/browser/

user/password: neo4j/123456

#### server access:

119.45.121.125

root/password: root/6Bp.}G%S7kV,mj

pwd: /neo4j/bin and execute: ./neo4j  start/stop/status

### Datasets Introduction
#### Nodes:
Diseases
Department
Drug
Symptom
Food
Producer
#### relation
has_neopathy(Diseases -- Diseases)
has_symptom(Disease --Symptom)
can_use_drug(Disease -- Drug)
belongs_to(Department -- Department)
belongs_to(Disease -- Department)
can_eat(Disease-- Food)
not_eat(Disease-- Food)
drug_producer(Drug -- Producer)
![1](https://raw.github.com/Chriszhangmw/Internship_work/master/pic/image-20200619071734697.png)

![2](https://raw.github.com/Chriszhangmw/Internship_work/master/pic/image-20200619072507739.png)


### Running

1. inputs: what kind of drug ia suggested having hepatitis(请问肝炎应该吃什么药)
   ![3](https://raw.github.com/Chriszhangmw/Internship_work/master/pic/image-20200620065214545.png)

2. system will require you select one of sepecifc hepatitis, then I choose number 2(2:丙型病毒性肝炎)
   ![4](https://raw.github.com/Chriszhangmw/Internship_work/master/pic/image-20200620065500739.png)

3. system execute the intend's action, search the durg for the disease from knowledge graph
   ![5](https://raw.github.com/Chriszhangmw/Internship_work/master/pic/image-20200620065627161.png)

4. then user ask the complications, even the sentence does not have disease name, but rasa can get the entity from tracker and use the disease as the main entity for the current conversation.
   ![6](https://raw.github.com/Chriszhangmw/Internship_work/master/pic/image-20200620070227987.png)

5. use can contibue ask questions ....

6. use command: , and use the service by restful API







## Demo 2

### Introduction

assert that if user want to know the weather, uses must provide location and date time to the system, and we can extend our business logical to other scenarios, for example, if you want search  how to solve a repair order, you must provide the position of the problem, the time of the problem occurs, the type of network element, only the user fill all these three slots in the conversation, the system will execute the search function, we call these process is task based conversation.

![7](https://raw.github.com/Chriszhangmw/Internship_work/master/pic/image-20200620111619400.png)




## Requirements

rasa==1.9.4

tensorflow==2.1.0
tensorflow-addons==0.8.3
tensorflow-estimator==2.1.0
tensorflow-hub==0.7.0
