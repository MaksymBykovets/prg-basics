person = {
   "name": "Marek",
   "surname": "Banach",
   "age": 25,
   "hobby": ["swimming","excursions"],
   "married": True,
   "phone":{"landline":"123444321","mobile":"777888999"}
}
## 1 
name = 0 
for key,value in person.items() : 
    name += 1 
    if name == 1 : 
        print(f"{key} : {value}")

## 2 
hobby = ""
for item in person["hobby"] : 
    hobby += item + " "
print(f"hobby : {hobby}")

## 3 
for key,value in person.items() : 
    print(f"{key} : {value}")

## 4 
new = {"surname": "Nowak"}
person.update(new)

## 5 
marr = {"married": False}
person.update(marr)

## 6 
gend = {"gender": "Male"}
person.update(gend)

## 7 
person["hobby"].append("bicycle")

##  8 
person["phone"]["work"] = "313131444"

##  9 
for key,value in person.items() : 
    print(f"{key} : {value}")