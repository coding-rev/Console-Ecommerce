let name = "Emmanuel";
let age = 23;
let isFineBoy = true;
let myArr = ["emmanuel", "owusu", "Fada", "Michael"]
let myDict = [{
    "name": "Emmanuel Owusu",
    "age": 23, 
    "program": "BSc. Computer Engineering"
}]

// DATA COLLECTION AND PRINTING
// alert("How ");
// let userInput = prompt("What is your name : ");

// console.log(userInput);

// CONDITIONAL STATAEMENTS
// if (isFineBoy == true){
//     console.log("yes");
// }
// else if(isFineBoy ==false){
//     console.log("no");
// }
// else{
//     console.log("none");
// }


// LOOPS
// for (let i = 0; i <= 3; i++){
//     console.log(myArr[i]);
// }
// console.log(myDict[0]);

// FUNCTIONS
// function myFunc(firstNumber, secondNumber){
//     let add = firstNumber + secondNumber;
//     return add;
// }
// let response = myFunc(10, 20);
// console.log(response);

// SPECIAL FUNCS
let buttons = document.getElementsByClassName("btn");
let imageField = document.getElementById("mainimage");
let imageName = document.getElementById("food-image-name");

myFoods = {
    "Jollof": "http://127.0.0.1:5500/image/bible.jpeg",
    "Banku": "http://127.0.0.1:5500/image/django.jpeg"
}

for (let i=0; i<buttons.length; i++){
    buttons[i].addEventListener('click', ()=>{
        let buttonValue = buttons[i].value;
        
        imageField.src = myFoods[buttonValue];
        imageName.innerHTML = buttonValue;
    });

}