var question_table = document.querySelectorAll("#question-table tbody tr.border-bottom")

var liteature_total = [0,0,0,0]
var math_total = [0,0,0,0]
var physics_total = [0,0,0,0]
var chemistry_total = [0,0,0,0]
var biology_total = [0,0,0,0]
var history_total = [0,0,0,0]
var geography_total = [0,0,0,0]
var philosophy_total = [0,0,0,0]
var religion_total = [0,0,0,0]
var question_true = 0;
var question_false = 0;
var question_blank = 0;
var question_clear = 0;
var score = 0;

question_table.forEach((el) => {

    
    
    var liteature = el.children[2].textContent.split(" | ")
    for (let index = 0; index < liteature.length; index++) {
        liteature_total[index] += Number(liteature[index]);
    }

    var math = el.children[3].textContent.split(" | ")
    for (let index = 0; index < math.length; index++) {
        math_total[index] += Number(math[index]);
    }


    var physics = el.children[4].textContent.split(" | ")
    for (let index = 0; index < physics.length; index++) {
        physics_total[index] += Number(physics[index]);
    }


    var chemistry = el.children[5].textContent.split(" | ")
    for (let index = 0; index < chemistry.length; index++) {
        chemistry_total[index] += Number(chemistry[index]);
    }



    var biology = el.children[6].textContent.split(" | ")
    for (let index = 0; index < biology.length; index++) {
        biology_total[index] += Number(biology[index]);
    }



    var history = el.children[7].textContent.split(" | ")
    for (let index = 0; index < history.length; index++) {
        history_total[index] += Number(history[index]);
    }



    var geography = el.children[8].textContent.split(" | ")
    for (let index = 0; index < geography.length; index++) {
        geography_total[index] += Number(geography[index]);
    }



    var philosophy = el.children[9].textContent.split(" | ")
    for (let index = 0; index < philosophy.length; index++) {
        philosophy_total[index] += Number(philosophy[index]);
    }

    var religion = el.children[10].textContent.split(" | ")
    for (let index = 0; index < religion.length; index++) {
        religion_total[index] += Number(religion[index]);
    }


    question_true += Number(el.children[11].textContent.split(" "))
    question_false += Number(el.children[12].textContent.split(" "))
    question_blank += Number(el.children[13].textContent.split(" "))
    question_clear += Number(el.children[14].textContent.split(" "))
    score += Number(el.children[15].textContent.split(" "))

})

for (let index = 0; index < liteature_total.length; index++) {
    
    liteature_total[index] = Math.round(liteature_total[index] / question_table.length * 10) / 10;

}

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
for (let index = 0; index < history_total.length; index++) {
    
    history_total[index] = Math.round(history_total[index] / question_table.length * 10) / 10;
}
for (let index = 0; index < geography_total.length; index++) {
    
    geography_total[index] = Math.round(geography_total[index] / question_table.length * 10) / 10;
}
for (let index = 0; index < philosophy_total.length; index++) {
    
    philosophy_total[index] = Math.round(philosophy_total[index] / question_table.length * 10) / 10;
}
for (let index = 0; index < religion_total.length; index++) {
    
    religion_total[index] = Math.round(religion_total[index] / question_table.length * 10) / 10;
}




result_list = [0,0,
    String(liteature_total).replace(/,/g," |"),
    String(math_total).replace(/,/g," |"),
    String(physics_total).replace(/,/g,"|"),
    String(chemistry_total).replace(/,/g,"|"),
    String(biology_total).replace(/,/g,"|"),
    String(history_total).replace(/,/g,"|"),
    String(geography_total).replace(/,/g,"|"),
    String(philosophy_total).replace(/,/g,"|"),
    String(religion_total).replace(/,/g,"|"),
    Math.round(question_true / question_table.length * 100) / 100,
    Math.round(question_false / question_table.length * 100) / 100,
    Math.round(question_blank / question_table.length * 100) / 100,
    Math.round(question_clear / question_table.length * 100) / 100,
    Math.round(score / question_table.length * 100) / 100]



var result_col = document.querySelector(".col-mean")

for (t = 2; t < 17; t++) {
    result_col.children[t].textContent = result_list[t]
}
