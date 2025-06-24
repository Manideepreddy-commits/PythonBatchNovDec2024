let student={
    name:"Ramu",
    phoneNo : 7816077275,
    address :{
        city: "kalwakurthy",
        district :"Nagar Kurnool"
    },
    wish : function(){
        console.log("Happy Journey")
    }
}

console.log(student.name);
console.log(student.address.city);
let student1 ={...student}
student1.name="jhon smith"
console.log(student1.name);
