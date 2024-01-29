$(document).ready(function() {
	var area = document.querySelector("select[name='area']")
	var lessonInlines = document.querySelectorAll(".field-lesson select")
	var countInlines = document.querySelectorAll(".field-total_question > input")
	
	var tyt = [[5,40], [1,40], [2,7], [3,7], [4,6], [7,5], [6,5], [8,5], [9,5]]
	var ayt = [[1,40], [2,14], [3,13], [4,13]]

	
	area.addEventListener("change", function() {
		
		for (let i = 0; i < tyt.length; i++) {
			lessonInlines[i].value = null
			countInlines[i].value = null
		}
		
		if (area.value == 1) { //tyt
			for (let i = 0; i < tyt.length ; i++) {
				lessonInlines[i].value = tyt[i][0]
				countInlines[i].value = tyt[i][1]
			}
		}else if (area.value == 2) {
			for (let i = 0; i < ayt.length ; i++) {
				lessonInlines[i].value = ayt[i][0]
				countInlines[i].value = ayt[i][1]
			}
		}
		
	})
	
})

