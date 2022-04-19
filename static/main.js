
var navbar = document.getElementById("navclass");
window.onscroll=function(){
    var scrollhieghtnav = navbar.scrollHeight+10;
    console.log("navscroolHieght"+scrollhieghtnav)
    console.log("scrolly"+window.scrollY)
    if(window.scrollY >= scrollhieghtnav ){
        navbar.classList.add("fixedClass")
    }else{
    navbar.classList.remove("fixedClass")
    }

}

var x=10
var y="nnbnbn"
console.log(x)
console.log(y)
var dolists=document.getElementsByClassName("clr")[0];
window.onload=function(){
  console.log(dolists.innerText)
}

// find the sum off all odd no from 1 to 100
   // find the esum of off all even no from 1 to 100

   // find the multiple of all odd no from 1- 10
    // find the multiple of all even no from 1- 10

    ///add three variable a+b+c
    // multiply three variable x*y*z
    /// practice to add dynamics class using javascript


    //while do while if else


function bnm(){

  var dolistele=document.getElementsByClassName("dolist")[0];
  
  dolistele.style.background="red";

}


var btnele=document.getElementById("clkme")





function ld(){

  var dolistele=document.getElementsByClassName("dolist")[0];
  
  dolistele.style.background="yellow";
  dolistele.innerHTML="gogoogogooggogogoogoogogogoogoogogogoogogggogogo"
  var dolistele=document.getElementsByClassName("dolist")[1];
  dolistele.classList.add("dogreenwithRedborder");



}

window.onload = ld;

function logKey(e) {
  log.textContent += ` ${e.code}`;
}



function Person(name, job, yearOfBirth){  
  this.name= name;
  this.job= job;
  this.yearOfBirth= yearOfBirth;
}
// adding calculateAge() method to the Prototype property
Person.prototype.calculateAge= function(){ 
  console.log('The current age is: '+(2019- this.yearOfBirth));
}
console.log(Person.prototype);

// creating Object Person1
let Person1= new Person('Jenni', 'clerk', 1986); 
console.log(Person1)
let Person2= new Person('Madhu', 'Developer', 1997);
console.log(Person2)

Person1.calculateAge();
Person2.calculateAge();










