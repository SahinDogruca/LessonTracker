var question_table = document.querySelectorAll("#question-table tbody tr.border-bottom")

var math_total = [0,0,0,0]
var physics_total = [0,0,0,0]
var chemistry_total = [0,0,0,0]
var biology_total = [0,0,0,0]
var question_true = 0;
var question_false = 0;
var question_blank = 0;
var question_clear = 0;

question_table.forEach((el) => {

    var math = el.children[2].textContent.split(" | ")
    for (let index = 0; index < math.length; index++) {
        math_total[index] += Number(math[index]);
    }


    var physics = el.children[3].textContent.split(" | ")
    for (let index = 0; index < physics.length; index++) {
        physics_total[index] += Number(physics[index]);
    }


    var chemistry = el.children[4].textContent.split(" | ")
    for (let index = 0; index < chemistry.length; index++) {
        chemistry_total[index] += Number(chemistry[index]);
    }



    var biology = el.children[5].textContent.split(" | ")
    for (let index = 0; index < biology.length; index++) {
        biology_total[index] += Number(biology[index]);
    }



    question_true += Number(el.children[6].textContent.split(" "))
    question_false += Number(el.children[7].textContent.split(" "))
    question_blank += Number(el.children[8].textContent.split(" "))
    question_clear += Number(el.children[9].textContent.split(" "))

})



for (let index = 0; index < math_total.length; index++) {
    
    math_total[index] = Math.round(math_total[index] / question_table.length * 10) / 10;
}

for (let index = 0; index < physics_total.length; index++) {
    
    physics_total[index] = Math.round(physics_total[index] / question_table.length * 10) / 10;
}

for (let index = 0; index < chemistry_total.length; index++) {
    
    chemistry_total[index] = Math.round(chemistry_total[index] / question_table.length * 10) / 10;
}
for (let index = 0; index < biology_total.length; index++) {
    
    biology_total[index] = Math.round(biology_total[index] / question_table.length * 10) / 10;
}



result_list = [0,0,
    String(math_total).replace(/,/g," | "),
    String(physics_total).replace(/,/g," | "),
    String(chemistry_total).replace(/,/g," | "),
    String(biology_total).replace(/,/g," | "),
    Math.round(question_true / question_table.length * 100) / 100,
    Math.round(question_false / question_table.length * 100) / 100,
    Math.round(question_blank / question_table.length * 100) / 100,
    Math.round(question_clear / question_table.length * 100) / 100
]


var result_col = document.querySelector(".col-mean-ayt")

for (t = 2; t < 10; t++) {
    result_col.children[t].textContent = result_list[t]
}